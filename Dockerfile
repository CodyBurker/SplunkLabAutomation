FROM python:3.10.0a2-slim-buster
WORKDIR /usr/
ADD ./SplunkLab.py .
RUN pip install docker
CMD [ "/usr/python3", "./SplunkLab.py" ]