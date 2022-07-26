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

If you want to start the postgres console

```bash
docker ps
docker exec -it CONTAINER_ID bash
psql -h localhost -p 5432 -U postgres -W
\l 
\c postgres
\d
\dt
```

# Start fastapi-app

```bash
uvicorn main:app --reload
```

# Connection configuration 

## database.py

```python
import databases
from config.env_reader import env

def get_database_url()->str:
    ## Local vars
    drivername = "postgresql"
    db_user = env("DB_USER")
    db_pass = env("DB_PASSWORD")
    db_name = env("DB_NAME")
    db_host = env("INSTANCE_HOST")
    db_port = env("DB_PORT")
    connection = drivername + '://' + db_user + ":" + db_pass + "@" + db_host + ":" + db_port + "/" + db_name
    return connection

database_url = get_database_url()
database = databases.Database(database_url)

```

## models.py

```python
from sqlalchemy import Column, Integer, String, ForeignKey, Table, MetaData
from .database import database, database_url
from sqlalchemy.orm import relationship
import sqlalchemy

meta = MetaData()

Test = Table(
    'test', meta, 
    Column('id_test', Integer, primary_key=True, index=True),
    Column('nametest', String, unique=True, nullable=False)
)

Books = Table(
    'books', meta, 
    Column("id", Integer, primary_key=True),
    Column('title', String, nullable=False),
    Column('author', String, nullable=False)
)

engine = sqlalchemy.create_engine(database_url)
meta.create_all(engine)
```

## main.py

Notice the important of _startup_ and _shutdown_ endpoints

```python
from fastapi import FastAPI
from connection.database import database
from connection.models import Test, Books

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

```

# Alembic

Alembic is our migration manager

```bash
alembic init migrations
# Delete or change information
alembic revision --autogenerate -m "Initial"
alembic upgrade head
# Delete or change information into models file
alembic revision --autogenerate -m "Delete Test table"
alembic upgrade head
```