# finances with Excel
# Jarrod Correll
# backend development Python
# version 0.01
import os
import time

os.system('cls')
print("-----Welcome-----")
print("Do you have a financial document you would like to open?")
option = input("(Y/N): ")

if option == "Y" or option == "y":
    print("What is the name of the document?")
    docname = input("$: ")
elif option == "N" or option == "n":
    print("Let us create a document, what would like to name it?")
    docnewname = input("$: ")
else:
    print("error (closing in 3 seconds)")
    time.sleep(3)
    os.system('exit')











