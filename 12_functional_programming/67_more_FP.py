
# Using SORTED

animals = ['dog', 'elephant', 'cat', 'giraffe', 'badger']


animals1 = sorted(animals) # ['badger', 'cat', 'dog', 'elephant', 'giraffe']

def order(item):
    return item

animals2 = sorted(animals, key=order) # ['badger', 'cat', 'dog', 'elephant', 'giraffe']


def order_by_len(item):
    return len(item)

animals3 = sorted(animals, key=order_by_len) # ['dog', 'cat', 'badger', 'giraffe', 'elephant']


# to reverse the order
animals4 = sorted(animals, reverse=True, key=order_by_len) # ['elephant', 'giraffe', 'badger', 'dog', 'cat']
# print(animals4)



# sorting the list without creating a new variable
animals.sort()
# print(animals)


# using a lambda expression
animal5 = sorted(animals4, key=lambda item: item)
# print(animal5)


# ---------------------------------------------------------------
# Generating Characters

# print(ord("A"))
# print(ord("Z"))

# print(chr(65))


characters = [chr(x) for x in range(65, 91)]
# print(characters)



# -----------------------------------------------------------------------
# Generator expression in python
generators = (chr(x) for x in range(65, 91))

# for x in generators:
#     print(x)
    
generator_list = list((chr(x) for x in range(65, 91)))

# print(generator_list)

# more examples
# print([x for x in range(0, 3)])
# print([x for x in range(0, 3) if x != 1])
# print([ '*' if x == 0 else x for x in range(0, 3)])
# print([ '*' if x == 0 else x for x in range(0, 3) if x != 1])

# print(list(x for x in range(0, 4) for y in range(0, 4)))

# print(list((x, y) for x in range(0, 4) for y in range(0, 4)))


# print(list((x, y) if x != y else '=' for x in range(0, 4) for y in range(0, 4)))

# print(list((x, y) if x != y else '=' for x in range(0, 4) if x != 1 for y in range(0, 4)))

# print(list((x, y) if x != y else '=' for x in range(0, 4) if x != 1 for y in range(0, 4) if y != 2))

# rewriting this in a nexted loop
li = list()

for x in range(0, 4):
    if x != 1:
        for y in range(0, 4):
            if y != 2:
                if x != y:
                    li.append((x, y))
                else:
                    li.append("=")
       

# alternatively

for x in range(0, 4):
    if x == 1:
        continue
    
    for y in range(0, 4):
        if y == 2:
            continue
        
        if x == y:
            li.append("=")
        else:
            li.append((x, y))


# print(li)


# -----------------------------------------------------------
# conways game of life array refactoring

for rowoffs in range(-1, 2):
    for coloffs in range(-1, 2):
        if rowoffs == 0 and coloffs == 0:
            continue
        
        # print(rowoffs, coloffs)

# print()

# using generators

gen = ((rowoffs, coloffs) for rowoffs in range(-1, 2) for coloffs in range(-1, 2) if not (rowoffs == 0 and coloffs == 0))
# for rowoffs, coloffs in gen:
#     print(rowoffs, coloffs)



# ------------------------------------------------------------------------------------
# using itertools module

import itertools as it

items = it.product(range(-1, 2), range(-1, 2))
items = it.filterfalse(lambda v: v[0]==0 and v[1]==0, items )

# for x, y in items:
#     print(x, y)


# ----------------------------------------------------------------------------
# Function Generators

def number_range():
    for i in range(0, 5):
        yield i
        

it = iter(number_range())

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))


# Powers of two 

def powers_of_two(n):
    powers = 1
    
    for _ in range(0, n):
        yield powers
        powers *= 2


# for x in powers_of_two(5):
#     print(x)


# -----------------------------------------------------------------------------
# Filtering

seq = filter(lambda x: x % 2 == 0, (x for x in range(0, 20)))
# print(list(seq))

# ----------------------------------------------------------------------------
# usind Reduce

import functools as fn
import operator as op

numbers = [1, 2, 3, 4, 5]

# print(fn.reduce(lambda x, y: x + y, numbers))
# print(fn.reduce(op.add, numbers))


# --------------------------------------------------------------------------------

# Word Exercise
from functools import reduce
from operator import add

guesses = set("aeiou")
word = 'fascinate'

# - a - - i - a - e

result = reduce(add, map(lambda x: ' - ' if x not in guesses else x, word))
# print(result)



# Functional Parsing

expenditure = """
Day        Electricity   Coffee      Cleaning     Wifi
Monday     330           10          50           20
Tuesday    220           12          40           25
Wednesday  120           14          80           30
Thursday   150           16          60           35
"""


for li in filter(lambda l: len(l) > 0, map(lambda s: s.split(), expenditure.split("\n"))):
    print(li)

