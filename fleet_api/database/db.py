import os
from psycopg import OperationalError, connect
from fleet_api.config import DevConfig  # Import your Config class from the appropriate module
from fleet_api.config import DevConfig  # Import your Config class from the appropriate module

env = DevConfig()

def get_connection():
   
    # set config
    print(env.DATABASE_URL)
    try:
        connection = connect(
            conninfo=env.DATABASE_URL
        );
        cursor = connection.cursor()
        cursor.execute("SET search_path TO " + env.POSTGRESQL_DEFAULT_SCHEMA)
        return connection;

    except OperationalError as ex:
        print_db_exception(ex)
        return None

def print_db_exception(ex):
    print(f"pgcode: {ex.pgcode} pgerror: {ex.pgerror}")
    raise ex from ex