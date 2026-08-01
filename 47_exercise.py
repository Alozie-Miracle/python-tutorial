"""
Write a function that converts feet ti miles

(miles = feet x 1.89E-4)

Using this function, wite a program taht asks the user to enter a distance in feet and
converts it to miles.

If the user enters a valid input, print the distance in miles to three decimal places and 
quit.
If the user enters invalid input, print "Invalid input" and ask them again


If the user enters "quit", quit the progrm.

Mouth Everest is 29,028 feet high. How high is it in miles?
"""



def main():
    user_input = input("Enter a distance in feet: or 'quit' > ")

    if user_input == "quit":
        quit()
    
    try:
        distance_in_miles = float(user_input) * 1.89E-4
        print(f"{user_input} in miles is {distance_in_miles:.3} miles")
    except:
        print("Invalid input")


while True:
    main()

