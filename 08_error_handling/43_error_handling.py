# traceback

def greet():
    print("Hello, World!")
    print(1/0)

# try:
#     greet()
# except:
#     print("Something went wrong!")


# division by zero error handling
# try:
#     greet()
# except ZeroDivisionError as e:
#     print(f"Zero Division Error: {e}")



def greet():
    print("Hello, World!")
    d = dict()
    print(d["non_existent_key"])

# key error handling
# try:
#     greet()
# except KeyError as e:
#     print(f"Key Error: {e}")


# Raising Exceptions
# raise KeyError("This is a custom KeyError message.")
# raise ValueError("This is a custom ValueError message.")
# raise TypeError("This is a custom TypeError message.")
# raise Exception("This is a custom exception message.")


# Keyboard Interrupt Error Handling
# try:
#     while True:
#         print("Press Ctrl+C to interrupt the program.")
# except KeyboardInterrupt:
#     print("Program interrupted by user.")


# Finally keyword
# try:
#     raise KeyError("This is a custom KeyError message.")
# except KeyError as e:
#     print(f"Key Error: {e}")
# except ZeroDivisionError as e:
#     print(f"Zero Division Error: {e}")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")
# finally:
#     print("This will always execute.")


# handling multiple exceptions
try:
    raise KeyError("This is a custom KeyError message.")

except (KeyError, ZeroDivisionError) as e:
    print(f"An error occurred: {e}")
else:
    print("No exceptions occurred.")
finally:
    print("This will always execute.")