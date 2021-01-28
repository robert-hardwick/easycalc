#!/bin/bash
app="easycalc.service"
docker build -t ${app} .
docker run -d -p 8888:8888 --name=${app} ${app}