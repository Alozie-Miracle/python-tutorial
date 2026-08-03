

name = input("Enter your name: ")
age = int(input("Enter your age: "))

age_limit = 100

print(f"Hello {name}! You have {age_limit - age} years left until you reach {age_limit}.")

# or

print("Hello " + name + "! You have " + str(age_limit - age) + " years left until you reach " + str(age_limit) + ".")