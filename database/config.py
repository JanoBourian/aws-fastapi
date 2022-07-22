from config.env_reader import env
from typing import Dict
import sqlalchemy

def init_connection_engine():
    db_config = {
        "pool_size": 5,
        "max_overflow": 2,
        "pool_timeout": 30,
        "pool_recycle": 1800
    }
    
    if env("ENVIRONMENT") not in ["dev", "qas", "int", "prd"]:
        return init_local_connection(db_config)
    else:
        return init_cloud_connection(db_config)
    
def init_local_connection(db_config:Dict[str, int]):
    
    ## Local vars
    drivername = "postgresql+psycopg2"
    db_user = env("DB_USER")
    db_pass = env("DB_PASSWORD")
    db_name = env("DB_NAME")
    db_host = env("INSTANCE_HOST")
    db_port = env("DB_PORT")
    connection = drivername + '://' + db_user + ":" + db_pass + "@" + db_host + ":" + db_port + "/" + db_name
    
    pool = sqlalchemy.create_engine(
        connection
    )
    
    return pool

def init_cloud_connection(db_config:Dict[str, int]):
    
    ## Cloud vars
    drivername = "postgresql+psycopg2"
    db_user = env("DB_USER")
    db_pass = env("DB_PASSWORD")
    db_name = env("DB_NAME")
    instance_connection_name = env("INSTANCE_CONNECTION_NAME")
    
    pool = sqlalchemy.create_engine(
        sqlalchemy.engine.url.URL.create(
            drivername = drivername,
            username = db_user,
            password = db_pass,
            database = db_name,
            query = {
                "unix_socket": f"/cloudsql/{instance_connection_name}"
            }
        ),
        **db_config
    )
    
    return pool