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




# getters and setters

class Machine:
    def __init__(self, name, id):
        self._name = name
        self._id = id

    def __str__(self):
        return f"Name: {self._name}"

    
    def get_name(self):
        return self._name

    def set_id(self, id):
        self._id = id

    def get_id(self):
        return self._id

# m = Machine("THX12344", "1345tfds")

# print(m.get_name())

# m.set_id("ftyjnbsy8765r")

# print(m.get_id())


# inheritance
class Car(Machine):
    pass


car = Car("Lexus", "123")
# print(car.get_name())



# Overriding methods
class Animal:
    def speak(self):
        print("I am an animal")

    def eat(self):
        print("Animal eating")

class Cat(Animal):
    def speak(self):
        print("I am a cat")


# animal = Animal()
# animal.speak()

# cat = Cat()
# cat.speak()


# super class constructor
class Machine:
    def __init__(self, name, id):
        self._name = name
        self._id = id


class Car(Machine):
    def __init__(self, id, name, type):
        # Machine.__init__(self, name, id)
        super().__init__(name, id)
        self._type = type

    def __str__(self):
        return f'{self._id}: {self._name}'

car = Car("Benz", 123, "GLE")
print(car)