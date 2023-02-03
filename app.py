from dbhelpers import run_statement

# Function for Verifying Log In
def login():
    is_valid = False
    while not is_valid:
        print("Log In")
        alias = input("Enter Alias: ")
        password = input("Enter Password: ")
        result = run_statement("CALL verify_user(?, ?)", [alias, password])
        if (type(result) == list):
            print("Successful login.")
            is_valid = True
            return result
        else:
            print("There was an error: "+ result)

# Function for Entering New Exploit
def create_exploit():
    user_id = input("Enter User Id: ")
    print("Create New Exploit:")
    content = input("Enter Content: ")
    run_statement("CALL create_exploit(?,?)", [content, user_id])
    print("Successfully Created Exploit")

# Function to view owned exploits
def view_owned_exploits():
    user_id = input("Enter User Id: ")
    print("Viewing Owned Exploits: ")
    result = run_statement("CALL view_own_exploits(?)", [user_id])
    if (type(result) == list):
        for exploit in result:
            print(exploit)
    else:
        print("There was an error: "+ result)

# Function to discover other user's exploits
def discover_exploits():
    user_id = input("Enter User Id: ")
    print("Discover Exploits From Other Users: ")
    result = run_statement("CALL discover_exploits(?)", [user_id])
    if (type(result) == list):
        for exploit in result:
            print("Post Id:", exploit)
    else:
        print("There was an error: "+ result)

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
def edit_exploit():
    is_valid = False
    while not is_valid: 
        print("Edit Existing Exploit:")
        user_id = input("Enter User Id: ")
        exploit_id = input("Enter Exploit ID: ")
        content = input("Enter New Content: ")
        run_statement("CALL edit_exploit(?,?,?)", [content, exploit_id, user_id])
        print("Successfully edited exploit.")
        is_valid = True

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
            create_exploit()
        elif (selection == '2'):
            view_owned_exploits()
        elif (selection == '3'):
            discover_exploits()
        elif (selection == '4'):
            print("Log Out Successful")
            is_valid = True
        elif (selection == '5'):
            edit_exploit()
        else:
            print("Invalid Selection, Choose From 1-5")


hacker_site_script()