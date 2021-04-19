# Create a login project
# if the user has failed 3 times, program should say access denied
# if the use is successful, the prompt should say ACCESS GRANTED

users = [
    {"username": "bingus", "password": "Password1"},
    {"username": "dingus", "password": "Password2"} 
]

def check_user_credentials(user, user_entry, password_entry):
    if user["username"] == user_entry and user["password"] == password_entry:
        return True
    return False


limit_attempts = 3
is_not_logged_in = True
while is_not_logged_in:
    user_entry = input("username: ")
    password_entry  = input("password: ")

    for user in users:
        result = check_user_credentials(user, user_entry, password_entry)

        if result == True:
            print("Access Granted")
            is_not_logged_in = False
            break
    else:
        limit_attempts -= 1
        if limit_attempts == 0:
            print("ACCESS DENIED")
            break
        else:
            print("Try Again")

print("Welcome 4head")
 

