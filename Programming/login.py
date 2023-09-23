with open("Programming/data/login_attempts.txt", "r") as file:
    file_text = file.read()
usernames = file_text.split()

# Function counting user's failed login attempts


def login_check(login_list, current_user):
    counter = 0
    for i in login_list:
        if i == current_user:
            counter = counter + 1
    if counter >= 3:
        # return "You have tried to login three or more times. Your account has been locked.""
        print("You have tried to login three or more times. Your account has been locked.")
    else:
        # return "You can log in!"
        print("You can log in!")


login_check(usernames, "errab")
