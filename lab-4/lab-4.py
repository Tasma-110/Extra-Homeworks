user_list = []

def show_menu():
    print("Choose one option:  ")
    print("1.Create user")
    print("2.Show all users")
    print("3.Delete user from list")
    print("4.Authorization")
    print("5.Exit")

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
        for key,value in user.items():
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
             print("User is not found.")

while True:
    show_menu()
    choice = input("Enter number: ")
    match choice:
        case "1":
            add_user()
        case "2":
            show_users()
        case "3":
            delete_user()
        case "4":
            case1()
        case "5":
            break
