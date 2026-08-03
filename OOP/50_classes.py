# Class Hierarchies


class Animal:
    pass


class Cat(Animal):
    pass


class Dog(Animal):
    pass


class Tigger(Animal):
    pass

class SiberianTigger(Tigger):
    pass


# print(SiberianTigger.mro())


# multiple inheritance

class Camera:
    def take_photo(self):
        print("Taking photo.")


class Phone:
    def make_call(self):
        print("Making call.")
        

class SmartPhone(Camera, Phone):
    pass

# device = SmartPhone()

# device.make_call()
# device.take_photo()


# the diamond problem
class Device:
    def activate(self):
        print("Device activated")

class Camera(Device):
    def activate(self):
        print("Camera activated")
        
    def take_photo(self):
        print("Taking photo.")


class Phone(Device):
    def make_call(self):
        print("Making call.")
        

class SmartPhone(Camera, Phone):
    pass

# device = SmartPhone()

# device.make_call()
# device.take_photo()
# print(SmartPhone.mro())
# device.activate()


# Mixins
class Alarm:
    def on(self):
        print("Alarm on")
    def off(self):
        print("Alarm off")


class Vehicle:
    def __init__(self, people):
        self._people = people
        
    def __str__(self):
        return f"Carries {self._people} people"
    
    
class Car(Vehicle, Alarm):
    def start(self):
        print("Car starting.")
        

# car = Car(4)
# car.on()
# print(car)


# property class
class Person:
    def __init__(self, age):
        self._age = age
        
    def get_age(self):
        return self._age
    
    def set_age(self, age):
        if age < 0 or age > 125:
            raise ValueError(f"Age {age} is out of range")
        self._age = age
        
    age = property(fget=get_age, fset=set_age)
        
    
person = Person(200)
print(person.get_age())

person.age = 20
print(person.get_age())