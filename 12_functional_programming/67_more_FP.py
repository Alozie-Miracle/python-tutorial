
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

print(list((x, y) if x != y else '=' for x in range(0, 4) if x != 1 for y in range(0, 4) if y != 2))

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


print(li)




