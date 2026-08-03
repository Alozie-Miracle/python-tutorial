"""
Write a program that asks the user to enter a name.

if the user enters a name in the list below, respond with the age of the person
entered. Otherwise print "Unkown person"

Make the program keep asking for names like this until the user enters
"quit". then the program exits.

Start by putting the names and ages in dictionary.

"""
people = ["Angela", 'Arthur', 'Isla', 'Noah', 'Ava', 'Leo', "Mia", "Oscar"]
ages = [20, 30, 40, 22, 30, 21, 20, 25]




# solution, put in a dict
profile = {}

for i in range(len(people)):
    profile.update({people[i]:ages[i]})

while True:

    response = input("Enter user name or 'quit': ").capitalize()
    if response == 'quit' or response == "Quit":
        # quit()
        break

    data = profile.get(response)
    if data is None:
        print("Unknown person")
    else:
        print(f"{response} is {data} years old")