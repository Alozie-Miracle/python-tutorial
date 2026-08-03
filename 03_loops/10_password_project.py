"""

Write a program that asks the user to enter a password and compares it to
a hard-coded password.

if the password is correct, the program prints "Greetings Professor Falcon" and exits.



If the password is incorrect, the program prints "Access Denied" and prompts the user to enter the password again.

The program will ask for the password three times if necessary.


after that, it exits.

"""

PASSWORD = "Falcon123"  # hard-coded password
password = input("Please enter the password: ")

for i in range(3):  # allow up to 3 attempts
    if password == PASSWORD:
        print("Greetings Professor Falcon")
        break  # exit the loop if the password is correct
    else:
        print("Access Denied")
        if i < 2:  # only prompt again if there are attempts left
            password = input("Please enter the password again: ")