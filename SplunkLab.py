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
    # Splunk image string
    splunk_image = "splunk/splunk:" + str(version)
    # Init docker client
    client = docker.from_env()

    # Add code to ensure that latest image is downloaded. If not pull it and notify user of potential delay.

    # Generate a random password
    # Code from https://stackoverflow.com/questions/3854692/generate-password-in-python
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(20))  # for a 20-character password
    new_volume_name = 'Splunk_Lab_' + str(user_name)
    # Start Container
    new_container = client.containers.run(
        splunk_image, # Image 
        detach=True, # Run Detached
        name="Splunk_Lab_" + str(user_name),
        ports = {8000:None},
        environment = {
            'SPLUNK_START_ARGS':'--accept-license',
            'SPLUNK_PASSWORD':password
        },
        volumes = {new_volume_name:
        {'bind': '/opt/splunk',
        'mode': 'rw'}}
        )
    while True:
        print(new_container.status)
        time.sleep(1000)

    
    # Test code
# start_lab("cody")