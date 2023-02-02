import mariadb
from dbhelpers import connect_db, close_connection, execute_statement

def login():
    alias = input("Enter Alias: ")
    password = input("Enter Password: ")
    cursor = connect_db()
    user_id = execute_statement(cursor, "CALL verify_user(?,?)", [alias, password])
    close_connection(cursor)
    for id in user_id:
        print("Successful login, welcome {}. User Id: {}".format(alias, id[0]))

def hacker_site():
    cursor = connect_db()
    
login()