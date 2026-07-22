#   Task
"""
Write a function that asks the user to enter their weight in kilos and their height in metres,
thenn calculates their BMI

(weight divided by height times height)

the the fuction should return all three values

"""

def BMI():
    name = input("Enter your name: ")
    weight = float(input("Enter your weight: "))
    height = float(input("Enter your height: "))

    return name, weight, height

def main():
    
    name, weight, height = BMI()
    bmi = round(weight / ( height * height ), 2)
    print(f"{name}, your BMI reads {bmi}")

main()