# lists are mutable and can be modified

# def main():
#     fruits = ["apple", "orange", "banana"]

#     print(len(fruits))


#     print(fruits[2])
#     print(fruits[0:2])

#     test1 = tuple()
#     test2 = list()


#     animals = ("fox", "rabbit")
#     print(animals)
#     animals = list(animals)
#     print(animals)


#     for animal in animals:
#         print(animal)

# main()



# joining lists
# animals1 = ("dog", "cat", "mouse")
# animals2 = ("lion", "tigger", "elephant")

# fruits1 = ["apple", "orange"]
# fruits2 = ["strawberry", "melon", "grape"]

# value = 5
# # value = value + 3
# value += 3
# # value *= 3
# print(value)

# print(id(animals1))
# animals1 += animals2
# print(id(animals1))

# print(animals1)

# print(id(fruits1))
# fruits1 += fruits2
# print(id(fruits1))
# print(fruits1)


# modifying lists
# fruits = ["apple", "orange", "strawberry", "banana"]
# print(fruits)

# fruits.append("melon")
# fruits.append("grape")
# print(fruits)

# print(fruits[2])

# fruits[2] = 'blackberry'
# print(fruits)


# print(fruits[1:4])

# fruits[1:4] = ["lime"]
# print(fruits)


# fruits[2:] = ["kiwi"]
# print(fruits)


# fruits[:2] = ["lemon", "redcurrent"]
# print(fruits)


# extending slicing
# numbers = ["zero", "one", "two", "three", "four", "five", "six"]

# print(numbers[3:7])

# # to add step size
# print(numbers[3:7:2])

# # multiply all the values in the even position by 2 using slice
# digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# digits[1:11:2] = [4, 8, 12, 16, 0]
# print(digits)

# # prints everything
# print(numbers[::])


# greeting = "Hello there"
# print(greeting[::2])


# print("What are you?"[3::3])


# extending and inseerting items into a list
# def main():
#     animals = ["dog", "donkey", "duck"]

#     animals.insert(1, "giraffe") # add at the middle of the list

#     more_animals = {"elephant", "monkey"}
#     animals.extend(more_animals) # add more at the end of the list

#     print(animals)



# main()


# removing list from list
# def main():
#     days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


    # days[0:3] = []
    # print(days)

    # days.remove("Sat")
    # print(days)

    # days.pop()
    # print(days)

    # days.pop(0)
    # print(days)

#     del days[1]
#     print(days)


#     days.clear()
#     print(days)

# main()




# list comprehension
# animals1 = ["dog", "goat", "sloth", "tiger"]

"""
animals2 = animals1
del animals2[1]

print(animals1)
print(animals2)

"""

# animals3 = animals1.copy()

# del animals3[1]
# print(animals1)
# print(animals3)

# animals4 = [animal for animal in animals1] #this is list comprehension
# print(animals4)

# animals5 = [animal.upper() for animal in animals1] #this is list comprehension
# print(animals5)

# lengths = [len(text) for text in animals1]
# print(lengths)


# number1 = [1, 2, 3, 4, 5, 6]
# numbers2 = [x for x in number1]

# # performing arithemethic
# numbers3 = [x**2 for x in number1]

# print(numbers3)

# conditions in list comprehension

# def main():
#     number1 = [x for x in range(0, 10)]
#     print(number1)

#     print()

#     # attaching conditions
#     numbers2 = [x for x in number1 if x > 5]
#     print(numbers2)

#     print() 
#     # getting the even numbers
#     numbers3 = [x for x in number1 if x % 2 == 0]
#     print(numbers3)

# main()


# if else in lsit comprehension

def main():
    numbers = [x for x in range(0, 20) if x % 2 == 1]

    print(numbers)

    # using if else
    more_numbers = [x if x > 10 else 0 for x in numbers]
    print(more_numbers)

main()