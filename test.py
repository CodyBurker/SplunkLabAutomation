import docker
client = docker.from_env()
all_containers = client.containers.list()

print("Found {} running containers:\n\n".format(len(all_containers)))
for container in all_containers:
    print("{}\t\t{}".format(container.name, container.image))