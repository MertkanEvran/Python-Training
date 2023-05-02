def interface():
    print("Welcome to main page".center(50,"-"))
    print("1-) Login")
    print("2-) Register")
    print("3-) Quit")
    user_choice = int(input("Please select a operation: "))
    if user_choice == 1:
        user_login()
    elif user_choice == 2:
        user_register()
    elif user_choice == 3:
        exit()
    else:
        raise Exception("Please enter a accaptable value.")
            
       
def check_file(file_name):
    try:
        open(file_name,"r",encoding="utf-8")
    except FileNotFoundError:
        return False
    else:
        return True

def create_file(file_name):
    if check_file(file_name):
        print("File is already exist")
    else:
        folder = open(file_name,"x",encoding="utf-8")
        folder.close()
        print("File is created")
        interface()

def initilaze_system(file_name):
    if check_file(file_name):
        interface()
    else:
        print("Need a file to store the user's data. Do you want to create a new one")
        print("1-) Yes")
        print("2-) No")
        user_input = input("Please select your option: ")
        if user_input == 1:
            create_file(file_name)
        elif user_input == 2:
            exit()
        else:
            raise Exception("Not acceptable input.")

def get_data():
    username=input("Username: ")
    password = input("Password: ")
    return username,password

def user_validation(username,password):
    if check_file("user_database.txt"):
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
            raise Exception("Not acceptable input.")

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

while True:
    try:
        initilaze_system("user_database.txt")
    except Exception as ex:
        print(ex)