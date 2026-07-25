# Task

"""
Get the user to enter a temperature in Celsius. 

conditions:
1. < 0: print "Fridge too cold"
2. 0 - 4: print "Fridge ok"
3. 4 - 6: print "Fridge too warm"
4. > 6: print "Fridge broken"

"""


temperature = float(input("Enter the temperature in Celsius: "))

if temperature < 0:
    print("Fridge too cold")
elif 0 <= temperature <= 4:
    print("Fridge ok")
elif 4 < temperature <= 6:
    print("Fridge too warm")
else:
    print("Fridge broken")


# improving code readability by using a function

# status = "Fridge broken"

if temperature < 0:
    status = "Fridge too cold"
elif 0 <= temperature <= 4:
    status = "Fridge ok"
elif 4 < temperature <= 6:
    status = "Fridge too warm"
else:
    status = "Fridge broken"

print(status)

# better improvement
STATUS_COLD = "Fridge too cold"
STATUS_OK = "Fridge ok"
STATUS_WARM = "Fridge too warm"
STATUS_BROKEN = "Fridge broken"

status = STATUS_BROKEN

if temperature < 0:
    status = STATUS_COLD
elif 0 <= temperature <= 4:
    status = STATUS_OK
elif 4 < temperature <= 6:
    status = STATUS_WARM


print(status)