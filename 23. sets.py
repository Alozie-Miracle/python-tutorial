# sets used to store collection of unique items
# sets are not ordered
# you can't get items based on index

# numbers = [1, 2, 3, 4] # list
# numbers2 = (1, 2, 3, 4) # tupple
# number3 = {1, 2, 3, 4} # sets

# # to get unique items in a list
# number_lists = [1, 2, 1, 3, 3, 3, 4, 5, 6, 6, 6, 7, 8]

# unique_items = set(number_lists)
# print(unique_items)

# # iterating over sets
# for number in number3:
#     print(number)


# # to check if item is in a set
# print(3 in number3) # returns true


"""
list: ordered, "in" is slow, mutable
tupple: ordered, "in" is slow, immutable
set: not ordered, "in" is fast, mutable

"""


# adding and updating sets

# numbers = {1, 2, 3}

# numbers.add(7)
# numbers.add(8)
# print(numbers)
# print()

# numbers2 = {10, 11, 12}

# numbers.update(numbers2) #adds a set to set
# print(numbers)
# print()

# # add a list to a set
# numbers.update(["cat", "dog"])
# print(numbers)


# removing item from a set
# numbers = {x for x in range(15)}
# print(numbers)

# print()

# numbers.remove(6)
# print(numbers)
# print()

# # safe way to remove item from a set not to get an error
# numbers.discard(20)
# print(numbers)


# union and intersection of sets
numbers1 = {1, 2, 3, 4, 5, 6, 7, 8}
numbers2 = {1, 9, 8, 0, 12, 453, 3, 5}

# union of a set
union = numbers1.union(numbers2)
print(union)

# intersection of a set
intersection = numbers1.intersection(numbers2)
print(intersection)

# difference of a set
difference1 = numbers1.difference(numbers2) #alternatively numbers1 - numbers2
difference2 = numbers2.difference(numbers1)
print(difference1)
print(difference2)

# to get the numbers that is not in both set
symetric_difference = numbers1.symmetric_difference(numbers2)
print(symetric_difference)


# set.clear clears the set
# set.copy returns a copy of the set

# difference_update removes the difference
print()
nums1 = {1, 2, 3, 4, 5, 6, 7 }
nums2 = {8, 0, 3, 10, 3, 6, 1 }
nums1.difference_update(nums2) 
print(nums1)


# checking superset
print(nums1.issuperset(nums2))
print({1,2,3}.issuperset({1,2}))

# subset
print({1,2}.issubset({1,2,3,4}))