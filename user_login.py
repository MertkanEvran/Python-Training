def interface():
    print("Welcome to main page".center(50,"-"))
    print("1-) Login")
    print("2-) Register")
    print("3-) Quit")
    while True:
        user_choice = int(input("Please select a operation: "))
        if user_choice == 1:
            user_login()
            break
        elif user_choice == 2:
            user_register()
            break
        elif user_choice == 3:
            break
        else:
            raise Exception("Please enter a accaptable value.")
        
def check_file():
    try:
        open("user_database.txt","r",encoding="utf-8")
    except FileNotFoundError:
        with open("user_database.txt","x",encoding="utf-8") as folder:
            print("File is created")
            return True
    else:
        return True

def get_data():
    username=input("Username: ")
    password = input("Password: ")

    return username,password

def user_validation(username,password):
    if check_file():
        with open("user_database.txt","r",encoding="utf-8") as folder:
            content = folder.readlines()
            for line in content:
                user_info = line.strip().split("->")
                if username == user_info[0] and password == user_info[1]:
                    return True
            return False

def user_login():
    user_info=get_data()
    username = user_info[0]
    password = user_info[1]
    if user_validation(username,password):
        print("Welcome to club dude")
    else:
        print("User is not found")
        print("Do you want to register?(y/n)")
        result=input("Your answer: ")
        if result == "y":
            user_register()
        elif result=="n":
            interface()
        else:
            raise Exception("Please enter the right input")

def user_register():
    user_info = get_data()
    username = user_info[0]
    password = user_info[1]
    if user_validation(username,password):
        print("User already exist.")
        interface()
    else:
        with open("user_database.txt","a",encoding="utf-8") as folder:
            folder.write(username + "->" + password + "\n")
            print("User is registered succesfully")
    
interface()