class Widget:
    count = 0 # associated to the class and not the object

    def __init__(self, name):
        self._name = name

        Widget.count += 1
        print(f"{self.count} widgets created.")

    def __str__(self):
        return self._name

    

# widget1 = Widget("Project panel")

# widget2 = Widget("Project panel")


# print(Widget.count)


"""
Assign sequwntial IDs 'Machine' objects, so machines have an ID
1, 2, 3, 4, etc. in the order they are created.

"""

class Machine:
    count = 0
    
    def __init__(self, name):
        self._name = name
        self._id = Machine.count + 1
        
        Machine.count += 1
        
    def __str__(self):
        return f"{self._name}, {self._id}"
    
# m1 = Machine("Lexus")
# print(m1)
    
        
# m2 = Machine("Benz GLE")
# print(m2)

# m3 = Machine("BWN")
# print(m3)




# class methods
class Machine:
    _count = 0
    
    def __init__(self, name):
        self._name = name
        self._id = Machine._count + 1
        
        Machine._count += 1
        
    def __str__(self):
        return f"{self._name}, {self._id}"
    
    
    @classmethod
    def get_count(cls):
        return Machine._count
    
    @classmethod
    def create(cls):
        return cls("unknown")
    
    
m1 = Machine("Lexus")
m2 = Machine("Benz GLE")
m3 = Machine("BWN")
    
        
