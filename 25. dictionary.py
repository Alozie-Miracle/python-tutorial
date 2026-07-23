# fruits = {
#     "apple": "green",
#     "orange": "orange",
#     "banana": "yellow"
# }


# print(fruits)

# # to access apple
# print(fruits["apple"])


# adding item to a dictionary
# months = {
#     "Jan": "January",
#     "Feb": "February",
#     "Mar": "March"
# }

# months["Apr"] = "April"
# print(months)

# months.update({"May": "May", "Jun": "June"})
# print(months)


# iteracting a dictionary
# fruits = {
#     "apple": "green",
#     "orange": "orange",
#     "banana": "yellow"
# }

# for fruit in fruits:
#     print(fruit + ": " + fruits[fruit])

# print("apple" in fruits)

# # items method
# for fruit in fruits.items():
#     print(fruit) #gives a tupple
#     # to get the fruit itself
#     (name, color) = fruit # unpacking the tupples
#     print(name + ", " + color)

# print()

# # alternatively

# for name, color in fruits.items():
#     print(name + ", " + color)


# to loop over the keys
# for fruit in fruits.keys() or 
# for fruit in fruit:


# viewing items in dictionary

# keys = fruits.keys()
# values = fruits.values()
# items = fruits.items()

# print(keys)
# print(values)
# print(items)

# # converting dict to list
# keys_list = list(keys)
# print(keys_list)


# deleting items from dictionaries

# del fruits["apple"]
# print(fruits)

# # or

# fruits.pop("banana")
# print(fruits)


# # get method of dict
# color = fruits.get("mango") # returns none
# print(color)


# color2 = fruits.get("mango", "red") # returns red
# this is better than using fruits['mango']


# default dict
# people = dict()

# people.update({"Bob": 45, "Sara": 12})


# print(people)


# from collections import defaultdict

# people = defaultdict(int)

# people.update({"Bob": 45, "Sara": 12})

# print(people["Bob"]) # returns 42

# print(people["vicky"]) # returns 0


# dict comprehension

fruits1 = {
    "apple": "green",
    "orange": "orange",
    "banana": "yellow"
}

fruits2 = fruits1.copy()

fruits1.pop("apple")
print(fruits1)
print(fruits2)


fruit3 = {x for x in fruits2} # returns the keys
print(fruit3)

# to get the exact dictionary
fruits4 = {key:value for (key, value) in fruits2.items()}
print(fruits4)