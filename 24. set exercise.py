"""
Print all the cubic numbers up to and including 729
Print all the square numbers up to and including 729

which cubic numbers are also square numbers
which cubic numbers are not square numbers

"""

cubic_numbers = {x**3 for x in range(0, 10)}
print(cubic_numbers)

square_numbers = {x**2 for x in range(0, 28)}
print(square_numbers)

print()
print("intersection")
intersection = cubic_numbers.intersection(square_numbers)
print(intersection)

print()
print("difference")
difference = cubic_numbers.difference(square_numbers)
print(difference)