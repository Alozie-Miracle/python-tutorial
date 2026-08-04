
# Functional Programming

# - Use pure Function
# - Prefer recursion to loops
# - Functionals are first class type
# - Data is immutable


# RECURSIONS - when a function calls it self

def factorial(n):
    if n == 0:
        return 1
    
    return n * factorial(n -1)


# print(factorial(5))

# --------------------------------------------------------------------

# Passing function to function
def double(number):
    return number * 2


def apply(values, func):
    result = list()
    
    for value in values:
        result.append(func(value))
        
    return result


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# result = apply(numbers, double)
# print(result)


# ------------------------------------------------------------

# Iterators e.g list

class PowersOfTwo:
    def __init__(self, max):
        self._max = max
        
        
    def __iter__(self):
        
        self._index = 0
        self._last_value = 1
        
        return self
    
    
    def __next__(self):
        self._index += 1
        
        result = self._last_value
        
        self._last_value *= 2
        
        if self._index > self._max:
            raise StopIteration
        
        
        return result


# pot = PowersOfTwo(5)

# for x, y in enumerate(pot):
#     print(x, y)

# ----------------------------------------------------------------------------

# Mapping

animals = ['cat', 'Dog', 'giraffe', 'Badger']

def to_lower(str):
    return str.lower()

# animals1 = map(to_lower, animals)
# print(list(animals1))

animal_list = list(map(to_lower, animals))
# print(animal_list)


# -----------------------------------------------------------------------------------

# Lambda Functions

animals_2 = map(lambda str: str.lower(), animals)

# print(list(animals_2))
