"""

- concetenation
- print multiple arguments
- string methods: lower, upper, casefold, join
- print termination character
- control character / escape sequences: \n \t \\

"""

print("Hello" + "there")
print("Hello" + str(7))
print("Hello", 100, {1, 2, 3}, 1.23)

print("Hello".upper()) # uppercase
print("Hello".lower()) # lowercase
print("Hello".casefold()) # lowercase

print(", ".join({'one', 'two', "three"}))
print("Hello", end="....")
print("Hi")


print("Hi,\nhow\nare you") #new line

print("Hi,\nhow\nare\tyou") #tabs

print("Hi,\nhow\nare\tyou\\") #give back slash

print('"Hi')
print("'Hi'")


# formating strings
# using a placeholder

name = "Zoe"
text = "Hello %s. How are you?" % name
print(text)


# for two placeholders
print("Hello %s and %s. How are you?" % ("Zoe", "Jack"))


# for int
print("Hello %s. The teperature is %d" % ("Zoe", 31))


# for floating point number
print("Hello %s. The teperature is %f" % ("Zoe", 31.123))
# for 2 decimal place
print("Hello %s. The teperature is %.2f" % ("Zoe", 31.123))

# to specify a width, will give it 10 spaces
print("Hello %s. The teperature is %10d" % ("Zoe", 31))




# format method
print("Hello {}".format("Zoe"))
print("Hello {} and {}".format("Zoe", "Jack"))
print("Hello {0} and {1}".format("Zoe", "Jack"))

print("The temperature is {}".format(11))
print("The temperature is {:.2f}".format(31.12333))

print("We have {number_units}".format(number_units=98))

print("Hello {name}. It is {temperature:.2f} degree today".format(temperature=27.1233, name="Jack"))


print("It is {distance:,.0f} mile to the sun".format(distance=9.3E7))


# to give space horizontally
print("Hello {:>20}".format(0.25))

print("We have {:.1%} fuel left".format(0.25)) 


# using f-string
name = "Zoe"
temperature = 32.2332333

greefing = f"Hello {name}, the temperature is {temperature} C"
greefing = f"Hello {name.upper()}, the temperature is {temperature:.2f} C"



# raw string in python
directory = "C:\\Documents\temp"
print(directory)

directory = r"C:\\Documents\temp"
print(directory)


directory = r"C:\\Documents\temp""\\"
print(directory)
