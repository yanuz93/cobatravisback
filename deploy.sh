#!/bin/bash
sudo docker stop helloworld
sudo docker rm helloworld
sudo docker rmi mathricks/flask-back:sudah
sudo docker run -d --name helloworld -p 8080:8080 mathricks/flask-back:sudah

