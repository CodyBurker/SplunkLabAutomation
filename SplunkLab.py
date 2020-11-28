import docker
import random 
import secrets
from datetime import datetime
import secrets
import string
# client = docker.from_env()
# all_containers = client.containers.list()

# print("Found {} running containers:\n\n".format(len(all_containers)))
# for container in all_containers:
#     print("{}\t\t{}".format(container.name, container.image))

# Function to start a new lab
def start_lab(user_name, version="latest"):
    # Splunk image string
    splunk_image = "splunk/splunk:" + str(version)
    # Init docker client
    client = docker.from_env()
     # Get a list of which ports are in use
    containers = client.containers.list()
    used_ports = list()
    for container in containers:
        for port in list(container.ports.values()):
            used_ports.append(port[0]["HostPort"])
    # Generate a random port not already in use:
    found_port = False
    while not found_port:
        new_port = random.randrange(1024,65535)
        found_port = not (new_port in used_ports)
    # Generate a random password
    # Code from https://stackoverflow.com/questions/3854692/generate-password-in-python
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(20))  # for a 20-character password
    client.containers.run(
        splunk_image, 
        detach=True,
        name="Splunk_Lab_" + str(user_name),
        ports = {'8000':new_port},
        environment = {
            'SPLUNK_START_ARGS':'--accept-license',
            'SPLUNK_PASSWORD':password
        }
        )
# Test code
start_lab("cody")