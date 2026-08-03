import math
"""
Write a function that calculates pi

you can calculate PI by adding up a large number of terms of the following series

pi = 4 x (1/1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ...)

You can check your value against the actual value of pi.
Import the math module and then use math.pi
"""

def calculate_pi():
    value = 1;
    sum = 0.0
    sign = 1
    for i in range(0, 1000):
        sum += (sign * 1/value)

        value += 2
        sign *= -1

    # adding an assertion
    pi = sum * 4

    assert pi > 2.5 and pi < 3.5, f"Pi is out of range: {pi}" # if it's false it throws error
    return sum



def main():
    approximated_pi = calculate_pi()
    print(approximated_pi, math.pi)

    difference = math.pi - approximated_pi
    print(f"Difference {difference}")

main()