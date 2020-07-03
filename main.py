import getpass
import os
os.system('cls')

file1 = open("accounts.txt", "r+")


print(file1.read())

print("")
print("")
print("Welcome to Financial Pro!")
print("-----------")
print("Login (1)")
print("Create Account (2)")
print("-----------")

choice = input("$: ")
if choice=="1":
    os.system('cls')
    print("---Login---")
    print("Enter Username: ")
    loguser = input("$: ")
    print("Enter Password: ")
    logpass = getpass.getpass("$: ")


elif choice == "2":
    os.system('cls')
    print("---Create Account---")
    print("Enter Username: ")
    createuser = input("$: ")
    print("Enter Password: ")
    createpass = getpass.getpass("$: ")
    print("ReEnter Password: ")
    createpass2 = getpass.getpass("$: ")
    if createpass == createpass2:
        print("success!")
    file1.write(createuser + "\n")
    file1.write(createpass + "\n")
    print (file1.readline(0))

else:
    print("error")











