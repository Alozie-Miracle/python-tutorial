# write in normal text and in function

# response = input("Please enter your response: ")

# if response == "Ok" or response == "ok":
#     print("You entered Ok.")
# else:
#     print("You did not enter Ok.")


# # writing in function
# def check_response():
#     response = input("Please enter your response: ").strip().lower()

#     if response == "ok":
#         print("You entered Ok.")
#     else:
#         print("You did not enter Ok.")



# check_response()

# multiple functions
# def default_message():
#     print("Welcome, no unauthoirized access allowed.")


# def ask_password():
#     password = input("Please enter your password: ")
#     if password == "1234":
#         print("Access granted.")
#     else:
#         print("Access denied.")


# default_message()
# ask_password()

# using the main function

# def main():
#     default_message()
#     ask_password()



# main()

# function arguments
# def greet(name):
#     print(f"Hello, {name}!")


# def main():
#     user_name = input("Please enter your name: ")
#     greet(user_name)

# main()


# function ids
def greet(name): #name is a parameter
    print(f"Hello, {name}!")
    print(f"Function ID of greet: {id(name)}")


def main():
    user_name = 'zypher'
    print(f"Function ID of greet: {id(user_name)}")
    greet(user_name) #user_name is an argument


main()