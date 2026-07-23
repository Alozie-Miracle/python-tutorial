# enumerate gives you the index and the item in a list
# zip loops two lists and give you access to it items at the same time

fruits = ["apple", "orange", "banana"]
animals = ['dog', 'cat', 'gaot']

for i, item in enumerate(fruits):
    print(i, item) #i is index and item is the data in the list


for fruit, animal in zip(fruits, animals):
    print(fruit, animal)




# improving the previous solution
people = ["Angela", 'Arthur', 'Isla', 'Noah', 'Ava', 'Leo', "Mia", "Oscar"]
ages = [20, 30, 40, 22, 30, 21, 20, 25]




# solution, put in a dict
profile = {}

for persion, age in zip(people, ages):
    profile.update({ persion: age })

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