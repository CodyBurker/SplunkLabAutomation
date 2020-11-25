import docker
import random 
# client = docker.from_env()
# all_containers = client.containers.list()

# print("Found {} running containers:\n\n".format(len(all_containers)))
# for container in all_containers:
#     print("{}\t\t{}".format(container.name, container.image))

# Function to start a new lab
def start_lab(user_name):
    client = docker.from_env()
     # Get a list of which ports are in use
    containers = client.containers.list()
    used_ports = list()
    for container in containers:
        for port in list(container.ports.values()):
            used_ports.append(port[0]["HostPort"])
    
    

    

# Test code
start_lab("cody")