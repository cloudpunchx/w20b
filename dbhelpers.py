import mariadb
import dbcreds

# Function to Connect to DB
def connect_db():
    try:
        conn = mariadb.connect(
        user = dbcreds.user,
        password = dbcreds.password,
        host = dbcreds.host,
        port = dbcreds.port,
        database = dbcreds.database,
        autocommit = True
        )
        cursor = conn.cursor()
        return cursor
    except mariadb.OperationalError as e:
        print("Could not connect to the database", e)
    except Exception as e:
        print("Something went wrong", e)

# Function to Close Cursor/Connection
def close_connection(cursor):
    try:
        conn = cursor.connection
        cursor.close()
        conn.close()
    except mariadb.IntegrityError as e:
        print("Integrity error", e)
    except mariadb.ProgrammingError as e:
        print("Error, please check syntax.", e)
    except mariadb.OperationalError as e:
        print("Something went wrong with the database.", e)
    except Exception as e:
        print("Error closing connection.", e)

# Function to Execute Statements, including with args
def execute_statement(cursor, statement, args=[]):
    try:
        cursor.execute(statement, args)
        result = cursor.fetchall()
        return result
    except mariadb.IntegrityError as e:
        print("Integrity error", e)
    except mariadb.ProgrammingError as e:
        print("Error, please check syntax.", e)
    except mariadb.OperationalError as e:
        print("Something went wrong with the database.", e)
    except Exception as e:
        print("Something went wrong.", e)

def run_statement(statement, args=[]):
    cursor = connect_db()
    if (cursor == None):
        return None
    results = execute_statement(cursor, statement, args)
    if (results == None):
        return None
    close_connection(cursor)
    return results

