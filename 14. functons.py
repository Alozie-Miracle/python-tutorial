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
# def greet(name): #name is a parameter
#     print(f"Hello, {name}!")
#     print(f"Function ID of greet: {id(name)}")


# def main():
#     user_name = 'zypher'
#     print(f"Function ID of greet: {id(user_name)}")
#     greet(user_name) #user_name is an argument


# main()



# function paramters
# def greet(name):
#     print("Hello, " + name + "!")

#     print("Function ID of greet: " + name)
#     name = "Rachel"
#     print("Function ID of greet after changing name: " + name)


# def main():
#     name = "John"

#     print("Before calling greet function: " + name)
#     greet(name)
#     print("After calling greet function: " + name)

# main()



# returning values from functions
# def greet(name):
#     print(f"Hi, {name}!")


# def create_greeting(name):
#     return f"Hello, {name}!"

# def main():
#     name = "John"
#     greet(name)

#     greeting = create_greeting(name)
#     print(greeting)


# main()


# passing multiple arguments to functions
def add_numbers(num1, num2):
    return num1 + num2

def volume_of_cuboid(length, width, height):
    return length * width * height

def main():
    result = add_numbers(5, 3)
    print(f"The sum is: {result}")

    volume = volume_of_cuboid(5, 3, 2)
    print(f"The volume of the cuboid is: {volume}")

main()