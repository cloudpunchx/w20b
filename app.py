import mariadb
from dbhelpers import connect_db, close_connection, execute_statement, run_statement

# Function for Verifying Log In
def login():
    print("Please Log In:")
    alias = input("Enter Alias: ")
    password = input("Enter Password: ")
    result = run_statement("CALL verify_user(?,?)", [alias, password])
    for user_id in result:
        print("Welcome User: {}".format(user_id[0]))

# Function for Entering New Exploit
def create_exploit():
    print("Create New Exploit:")
    content = input("Enter Content: ")
    user_id = input("Enter User ID: ")
    run_statement("CALL create_exploit(?,?)", [content, user_id])
    print("Successfully Created Exploit")
    

# Function to view owned exploits
def view_owned_exploits():
    print("Viewing Owned Exploits: ")
    user_id = input("Enter User ID: ")
    result = run_statement("CALL view_own_exploits(?)", [user_id])
    for post in result:
        print("User Id: {} Content: {}".format(user_id, post))

# Function to discover other user's exploits
def discover_exploits():
    print("Discover Exploits From Other Users: ")
    user_id = input("Enter User ID: ")
    result = run_statement("CALL discover_exploits(?)", [user_id])
    for post in result:
        print("User Id: {} Content: {}".format(user_id, post))

# Bonus 1: Function to Sign UP
def signup():
    print("Sign Up:")
    alias = input("Enter Alias: ")
    password = input("Enter Password: ")
    run_statement("CALL signup(?,?)", [alias, password])
    print("Welcome User: ", alias)

# Script for Hacker Site
def hacker_site_script():
    print("Welcome, please Log In or Sign Up:\
        \n1. Log In\
        \n2. Sign Up")
    selection = input("Enter Selection: ")
    if selection == '1':
        login()
    elif selection == '2':
        signup()
    is_valid = False
    while not is_valid:
        print("Please select from the following:\
            \n1. Enter New Exploit\
            \n2. View Owned Exploits\
            \n3. Discover Exploits\
            \n4. Exit")
        selection = input("Enter Selection: ")
        if (selection == '1'):
            create_exploit()
        elif (selection == '2'):
            view_owned_exploits()
        elif (selection == '3'):
            discover_exploits()
        elif (selection == '4'):
            print("Log Out Successful")
            is_valid = True

hacker_site_script()