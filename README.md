# Overview
This project is designed to allow admins to easily start [Splunk](http://splunk.com/) docker [containers](https://hub.docker.com/r/splunk/splunk) for learning purposes. It is written in Python and makes use of the [Docker Python SDK](https://docker-py.readthedocs.io/en/stable/). The intent is to create a library of functions for the basic functionality of creating, listing, and killing containers (in `SplunkLab.py`), wrapping this in a web GUI with [Wooey](https://github.com/wooey/Wooey), and then finally wrapping all of this in a docker image (using the `Dockerfile`) for easy deployment. 
# Todo
 - Write script to set up Splunk Environment
   - ~~Start Container~~
     - ~~Given Username~~
     - ~~Random free port~~
     - ~~New Volumes~~
     - ~~Accept License~~
   - Copy License into container
   - ~~Output URL, username, password~~
 - Write script to retrieve containers/passwords
   - List all Splunk containers
     - URL
     - Usernames
     - Passwords
 - Write script to kill given container
   - Stop, RM container
   - Remove Volumes
 - Add web GUI (Wooey)
 - Containerize all of this
   - Mount docker socket required
   - ~~Install Docker python SDK with PIP~~
   - Install Wooey