
# 1: Find the numerical values in the list
'''
list = ["1","2","3","5a","7ca","a","50"]
numbers = []
for item in list:
    try:
        numbers.append(int(item))
    except Exception as ex:
        continue
print(numbers)
'''
# 2: Take inputs from user. If input is numerical then accept it. if it is not numerical then give a error. User should input "q" to exit.
'''
numbers=[]
while True:
    print("Type the q to exit the system")
    user_input = input("Please enter a number: ")
    try:
        numbers.append(int(user_input))
        print(numbers)
    except Exception as ex :
        if user_input == "q":
            print("System is closed.")
            break
        else:
            print(ex)
'''
# 3: Take a password from user.If the password include any turkish letter, so give a error message to user.

'''
turkish_letters = ["ç","ğ","ö","ş","ı","ü","Ç","Ğ","Ö","Ş","İ","Ü"]
password = None

def check_password(password):
    for letter in password:
        if letter in turkish_letters:
            raise Exception("Please don't use any turkish letter")
        else:
            return

while True:
    password = input("Please enter the password")
    try:
        check_password(password)
    except Exception as ex:
        print(ex)
    else:
        break
'''

#4 : Create a factorial method . If that method takes any wrong input, then give a error message to user

'''
def find_fact(number):
    result = 1
    for x in range(1,number+1): 
        result = result * x
    return result

while True:
    answer = input("Please enter a number: ")
    try:
        number = int(answer)
        result=find_fact(number)
        print(result)
    except Exception as ex:
        print(ex)
    
'''