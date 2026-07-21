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