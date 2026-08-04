"""
Hexadecimal 

0 1 2 3 4 5 6 7 8 9 A B C D E F 10 11 12 .....

binary b
hexadecimal x

Exercise 1

Print a table of numbers from 0 t0 255.

Print each number in decimal, binary and hexadecimal format

"""



# for i in range(0, 256):
#     print(f'{i:03} {i:08b} {i:02x}')
    

# print("{:6x}".format(0x123456 & 0xFF00FF))


"""
Exercise 2

red      0x12
green    0x34
blue     0x56


combined color: 0x123456

Write a function that accepts three colours: red, green and blue.
The function returns a single integer that combines all three colours, as about.


Write another function that accepts a single combined colour and returns the 
red, green and blue components.
"""


def to_color(red, green, blue):
    return blue + (green << 8) + (red << 16)

def from_color(color):
    red = (color & 0xFF0000) >> 16
    green = (color & 0x00FF00) >> 8
    blue = (color & 0x0000FF)
    
    return red, green, blue


color = 0x123456

(red, green, blue) = from_color(color)

print(f"{red:x} {green:x} {blue:x}")

combined =  to_color(red, green, blue)

print(f"{combined:x}")