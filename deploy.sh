#!/bin/bash
docker stop helloworld
docker rm helloworld
docker rmi mathricks/flask-back:sudah
docker run -d --name helloworld -p 8080:8080 mathricks/flask-back:sudah

