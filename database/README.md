# Prerequisites

## Install Docker [![Generic badge](https://img.shields.io/badge/Prerequisite-Docker-blue.svg)](https://www.docker.com/products/docker-desktop/)

Refer https://www.docker.com/products/docker-desktop/ to install Docker

# Run database with Docker
```
cd ./src
docker build -t infom126-postgres-db ./
docker run -d --name infom126-postgresdb-container -p 5432:5432 infom126-postgres-db
```
