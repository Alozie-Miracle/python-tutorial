"""
Procedural programming (PP) - function calling function
Object orirented programming (OOP) - classes and obejcts
Functional Programming (FP) - passing functions to functios
"""


class Person:
    def eat(self):
        print("I am eating")

    def talk(self):
        print("Hello")



# person = Person()
# person2 = Person()

# person.talk()
# person2.eat()



# using constructors
class Person:
    def __init__(self, name):
        self._name = name
        print(f"{self._name} created") # runs when a person is created
        print(id(self))


    def eat(self):
        print("I am eating")

    def talk(self):
        print("Hello")


# person = Person("John")
# print(id(person))
# print()
# person2 = Person("Jack")
# print(id(person2))


# object properties

class Cat:
    def __init__(self, name, weight):
        self._name = name
        self._weight = weight

    
    def introduce(self):
        print(f"Hello my name is {self._name}, i weigh {self._weight} kg")


# cat = Cat("Purity", 1.2)

# cat.introduce()



# casting string representation to objects

class Cat:
    def __init__(self, name, weight):
        self._name = name
        self._weight = weight

    def __str__(self):
        return f"Hello, my name is {self._name}"

    
    def introduce(self):
        print(f"Hello my name is {self._name}, i weigh {self._weight} kg")


# cat = Cat("Purity", 1.2)
# print(cat)