import os
from ..database.db import get_connection, print_db_exception

def get():
    
    try:
        connection = get_connection()
        taxis = []
        with connection.cursor() as cursor:
            cursor.execute(
                """SELECT id, plate
                    FROM taxis"""                
            )
            resultset = cursor.fetchall()
            taxis = [{"id": row[0], "plate": row[1]} for row in resultset]

        connection.close()
        return taxis
    # https://www.psycopg.org/docs/errors.html
    # cual error debemos usar DataError, DatabaseError, OperationalError?
    # pylint: disable=broad-except
    except Exception as ex:
        # pylint: disable=raise-missing-from,broad-exception-raised
        print_db_exception(ex)
        return None