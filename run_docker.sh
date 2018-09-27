#!/bin/sh

docker build -t flask-vuln $(dirname $0)
docker run -d -p 127.0.0.1:5000:5000 --name=flask-vuln flask-vuln
