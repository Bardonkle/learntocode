# Create a login project
# if the user has failed 3 times, program should say access denied
# if the use is successful, the prompt should say ACCESS GRANTED
import login_user

user_1 = login_user.User("bingus", "Password1")
user_2 = login_user.User("dingus", "Password2")
users = [user_1, user_2]


limit_attempts = 3
is_not_logged_in = True
while is_not_logged_in:
    user_entry = input("username: ")
    password_entry  = input("password: ")

    for user in users:

        if user.user_credentials(user_entry, password_entry) == True:
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
 

