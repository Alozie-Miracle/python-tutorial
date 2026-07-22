# tupples are container type to contain data and it's immutable
# tupples are ordered
# tupples are list of things

# def main():
#     animals = ("dog", "cat", "tigger", "cat", "wolf")

#     print(type(animals))

#     number_of_animals = len(animals)
#     print(number_of_animals) 

#     print(animals[0]) #dog

#     print()

#     for animal in animals:
#         print(animal)

#     print()
#     for i in range(0, len(animals)):
#         print(animals[i])


# main()

# packing and unpacking tupples

# def main():
#     elements = (True, 3.2, 7, "goat") #putting item in the tupple is called packing

#     # unpacking tupples
#     (is_raining, weight, volume, animal) = elements
#     print(is_raining, weight, volume, animal)


#     fruits = ("apple", "orange", "banana", "strawberry", "pear") #or "apple", "orange", "banana", "strawberry", "pear"
#     (fruit1, fruit2, fruit3, *more_fruits) = fruits
#     # or fruit1, fruit2, fruit3, *more_fruits = fruits
#     print(fruit1, fruit2, fruit3, more_fruits)

#     # to get the last fruits
#     # (fruit1, fruit2, *more_fruits  fruit3,) = fruits
#     print(type(more_fruits))

# main()



# slicing tupples
# def main():
#     animals = ("dog", "cat", "tigger", "goat", "wolf")

#     print(animals[1]) #dog
#     print(animals[1:3]) # 1-3
#     print(animals[0:3]) #0-3
#     print()
#     print(animals[-1]) # gives last element
#     print(animals[-3:-1]) # gives tigger and goat


# main()


# tupple function and operators

numbers1 = 1, 2, 3, 4, 4, 5, 8

print(len(numbers1))
print(min(numbers1))
print(max(numbers1))

# count gives us how many 4s are in the tupple
print(numbers1.count(4))

# index tells us at what position is the number in
print(numbers1.index(8))

# adding tupples together
print(numbers1 + (10, 20))

# multiplying tupple
print((1, 2, 3) * 3)


# to create a tupple with only one item in it
numbers2 = (15, )
print(numbers2)