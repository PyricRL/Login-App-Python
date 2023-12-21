file = open("passwords.txt", "a")

createOrEnter = input("Would you like to create an account or login?")
if createOrEnter == "create":
    account = input("What is account name?")
    password = input("What is the account password?")
    print(account, password)
    print("Here is account username and password")
    account = str(account)
    password = str(password)
    file.write(account + "," + password + '\n')

if createOrEnter == "login":
    with open("passwords.txt", 'r') as fileopen:
        lines = fileopen.readlines()
        for line in lines:
            info = line.split(",")
            print(info[0], info[1])
    
    loginaccount = input("Enter account name: ")
    loginpassword = input("Enter account password: ")
    loginpassword = str(loginpassword) + "\n"

    if loginaccount == info[0]:
        if loginpassword == info[1]:
            print("You have access to account")
        
        else:
            print("Incorrect password")