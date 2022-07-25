# aws-fastapi
An AWS and FastAPI crash course

# Docker container for PostgreSQL database

## Steps for create and run the PostgreSQL container

Steps
```bash
* Download the official image
* Check the image
* Run the container with the next flags:
    * --name: container name
    * --env/-e: environment variables
    * -p: port assigment (<local>:<external>)
    * -v: where the data will be saved
    * --detach/-d: if you prefer execute it in background
* Try the connection and availability
```

Commands
```bash
docker ps
docker ps -a
docker pull postgres:latest
docker images

docker run \ 
    --name fastapi-postgres \
    -e POSTGRES_PASSWORD=mysecretpassword \
    -e PGDATA=/var/lib/postgresql/data/pgdata \
    -v C:<path>\aws-fastapi:/var/lib/postgresql/data \
    -p 5432:5432 \
    -d postgres:latest
    
docker logs fastapi-postgres
docker exec -it fastapi-postgres bash
```

# Start fastapi-app

```bash
uvicorn main:app --reload
```