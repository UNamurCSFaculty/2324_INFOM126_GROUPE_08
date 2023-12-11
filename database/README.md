# Run database with Docker
```
cd ./src
docker build -t infom126-postgres-db ./
docker run -d --name infom126-postgresdb-container -p 5432:5432 infom126-postgres-db
```
