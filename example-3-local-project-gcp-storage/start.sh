#!/bin/bash

# Build the base images from which are based the Dockerfiles
# then Startup all the containers at once 
#docker build -t phadoop-base docker && \

ln -sf config/.env
docker-compose -f docker-compose.yml up --build
