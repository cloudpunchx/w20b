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