import docker
import random 
import secrets
from datetime import datetime
import secrets
import string
import time 
# client = docker.from_env()
# all_containers = client.containers.list()

# print("Found {} running containers:\n\n".format(len(all_containers)))
# for container in all_containers:
#     print("{}\t\t{}".format(container.name, container.image))
# Function to start a new lab
def start_lab(user_name, version="latest"):
    # Uppercase username
    user_name = user_name.upper()
    # Splunk image string
    splunk_image = "splunk/splunk:" + str(version)
    # Init docker client
    print('Getting control of docker environment')
    client = docker.from_env()

    #to-do Add code to ensure that latest image is downloaded. If not pull it and notify user of potential delay.

     # Get a list of which ports are in use
    containers = client.containers.list()
    used_ports = list()
    for container in containers:
        for port in list(container.ports.values()):
            if port != None:
                used_ports.append(port[0]["HostPort"])
    # Generate a random port not already in use:
    found_port = False
    while not found_port:
        new_port = random.randrange(1024,65535)
        found_port = not (new_port in used_ports)
    

    # Tell user we're working on it.
    print('Generating password')
    # Generate a random password
    # Code from https://stackoverflow.com/questions/3854692/generate-password-in-python
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(20))  # for a 20-character password
    # Generate volume for Splunk Environment
    new_volume_name = 'Splunk_Lab_' + str(user_name)
    # Start Container
    print('Starting Splunk Environment - allow 2-5 minutes until it is ready.')
    new_container = client.containers.run(
        splunk_image, # Image 
        detach=True, # Run Detached
        name="Splunk_Lab_" + str(user_name),
        ports = {8000:new_port},
        environment = {
            'SPLUNK_START_ARGS':'--accept-license',
            'SPLUNK_PASSWORD':password
        },
        volumes = {new_volume_name:
        {'bind': '/opt/splunk',
        'mode': 'rw'}}
        )
    
    # Check for log that indicates container is ready
    container_logs = new_container.logs(stream=True)
    for log in container_logs:
        if log == b'Ansible playbook complete, will begin streaming splunkd_stderr.log\n':
            print("Splunk Environment ready")
            break

    # Print out info to user
    # Get container again (the old one isn't updated for some reason)
    new_container = client.containers.get(new_container.id)
    ports = new_container.ports['8000/tcp'][0]['HostPort']
    print("Port:\t\t" + str(ports))
    print("Username:\t" + "admin")
    print("Password:\t" + password)
    # Get port for new container
    