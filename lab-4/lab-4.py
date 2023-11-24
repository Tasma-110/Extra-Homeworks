user_list = []
authenticated_user = None

def show_menu(auth):
    print("Choose one option:  ")
    print("1. Create user")
    print("2. Show all users")
    print("3. Delete user from list")
    if auth:
        print("4. Logout")
    else:
        print("4. Authorization")
    print("5. Exit")

def add_user():
    user = {}
    user['Name'] = input("Name: ")
    user['Surname'] = input("Surname: ")
    user['Age'] = input("Age: ")
    user['Address'] = input("Address: ")
    user['Email'] = input("Email: ")
    while True:
        password = input("Password: ")
        if len(password) >= 8:
            user['Password'] = password
            break
        else:
            print("Password must be at least 8 characters long.")
    user_list.append(user)

def show_users():
    for user in user_list:
        for key, value in user.items():
            print(f'{key}: {value}', end=', ')
        print("")

def delete_user():
    name = input("Enter user name: ")
    for user in user_list:
        if user['Name'] == name:
            user_list.remove(user)
            print("The user was successfully deleted.")
            break
    else:
        print("User not found.")

def user_auth():
    global authenticated_user
    email = input("Enter email: ")
    if not email_check(email):
        print("Wrong email")
        return

    password = input("Enter password: ")
    if not password_check(email, password):
        print("Wrong password")
        return

    print("Authentication successful!!!")
    authenticated_user = email

def password_check(email, password):
    for user in user_list:
        if user['Email'] == email and user['Password'] == password:
            return True
    return False

def email_check(email):
    for user in user_list:
        if user['Email'] == email:
            return True
    return False

while True:
    show_menu(authenticated_user is not None)
    choice = input("Enter number: ")
    match choice:
        case "1":
            add_user()
        case "2":
            show_users()
        case "3":
             delete_user()
        case "4":
            if authenticated_user:
                authenticated_user = None
                print("Logout successful!")
            else:
                user_auth()
        case "5":
            break