from dbhelpers import connect_db, close_connection, execute_statement, run_statement

# LEAVING OFF WITH NEEDING TO COMMENT, AND CANT GET ERRORS TO GO AWAY EVEN THOUGH ITS SUCCESS
# CURSOR DOESNT HAVE A RESULT SET

# Function for Verifying Log In
def login():
    is_valid = False
    while not is_valid: 
        print("Please Log In:")
        alias = input("Enter Alias: ")
        password = input("Enter Password: ")
        results = run_statement("CALL verify_user(?,?)", [alias, password])
        for user_id in results:
            print("Welcome User: {}".format(user_id[0]))
            is_valid = True
            user_id = user_id[0]
            return user_id

# Function for Entering New Exploit
def create_exploit(user_id):
    print("Create New Exploit:")
    content = input("Enter Content: ")
    run_statement("CALL create_exploit(?,?)", [content, user_id])
    print("Successfully Created Exploit")

# Function to view owned exploits
def view_owned_exploits(user_id):
    print("Viewing Owned Exploits: ")
    result = run_statement("CALL view_own_exploits(?)", [user_id])
    for post in result:
        print("User Id: {} Content: {}".format(user_id, post))

# Function to discover other user's exploits
def discover_exploits(user_id):
    print("Discover Exploits From Other Users: ")
    result = run_statement("CALL discover_exploits(?)", [user_id])
    for post in result:
        print("User Id: {} Content: {}".format(user_id, post))

# Bonus 1: Function to Sign UP
def signup():
    is_valid = False
    while not is_valid: 
        print("Sign Up:")
        alias = input("Enter Alias: ")
        password = input("Enter Password: ")
        run_statement("CALL signup(?,?)", [alias, password])
        print("Welcome User: ", alias)
        is_valid = True

# Bonus 2: Function to modify exploit belonging to them
def edit_exploit(user_id):
    is_valid = False
    while not is_valid: 
        print("Edit Existing Exploit:")
        exploit_id = input("Enter Exploit ID: ")
        content = input("Enter New Content: ")
        run_statement("CALL edit_exploit(?,?,?)", [content, exploit_id, user_id])
        print("Successfully edited exploit.")
        is_valid = True

# Script for Hacker Site
def hacker_site_script():
    is_valid = False
    while not is_valid:
        print("Welcome, please Log In or Sign Up:\
            \n1. Log In\
            \n2. Sign Up")
        selection = input("Enter Selection: ")
        if selection == '1':
            login()
            is_valid = True
        elif selection == '2':
            signup()
            is_valid = True
        else:
            print("Invalid Selection, Choose From 1-2")
        is_valid = False
        while not is_valid:
            print("Please select from the following:\
                \n1. Enter New Exploit\
                \n2. View Owned Exploits\
                \n3. Discover Exploits\
                \n4. Exit\
                \n5. Edit Exploit")
            selection = input("Enter Selection: ")
            if (selection == '1'):
                user_id = login()
                create_exploit(user_id)
            elif (selection == '2'):
                user_id = login()
                view_owned_exploits(user_id)
            elif (selection == '3'):
                user_id = login()
                discover_exploits(user_id)
            elif (selection == '4'):
                print("Log Out Successful")
                is_valid = True
            elif (selection == '5'):
                user_id = login()
                edit_exploit(user_id)
            else:
                print("Invalid Selection, Choose From 1-5")

hacker_site_script()