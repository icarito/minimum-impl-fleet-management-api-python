from psycopg import OperationalError, connect
from fleet_api.config import Config  # Import your Config class from the appropriate module

env = Config()

def get_connection():   
    try:
        connection = connect(
            conninfo=env.DATABASE_URL
        );
        cursor = connection.cursor()
        return connection;

    except OperationalError as ex:
        print_db_exception(ex)
        return None

def print_db_exception(ex):
    print(f"pgcode: {ex.pgcode} pgerror: {ex.pgerror}")
    raise ex from ex