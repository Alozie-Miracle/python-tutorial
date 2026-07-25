"""
Write a function that calculates the factorial of a number

The factorial of a number is defined like this:

n! =  n * (n - 1) * (n - 2) * ... * 3 * 2 * 1

e.g.

factorial(5) = 5 * 4 * 3 * 2 * 1 = 120

The factorial of 0 is defined to be 1.

calculate the factorial of 7, i.e. 7! = 7 * 6 * 5 * 4 * 3 * 2 * 1 = 5040

Hint:
Use a loop
Create a variable before the loop, and have the loop repeatedly the number that
variable refers to.

"""


# def factorial(n):
#     if n < 1:
#         return 1
#     else:
#         number = n
#         for i in range(1, n):
#             number = number * (n - i)

#         return number



# def main():
#     data = factorial(7)
#     print(f"factorial of {7} is {data}")

# main()


# alternatively
def factorial(n):
    result = 1

    for i in range(2, n + 1):
        result = result * i

    return result

def main():
    result = factorial(7)
    print("Result:", result)

main()