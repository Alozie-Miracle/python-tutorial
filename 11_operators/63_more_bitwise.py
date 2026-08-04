
# bitwise "XOR" and "NOT" operator

def printb(value):
    # print("{:08b}".format(value))
    print(f"{value:08b}")
    
def print_flip(value):
    # print(f"{0b11111111 & value:08b}")
    print(f"{255 & value:08b}")


def main():
     
    num1 = 0b10001000
    num2 = 0b00001001
    
    # XOR operator
    printb(num1 ^ num2)
    
    
    # NOT operator
    printb(~num1)
    # flipping
    print_flip(~num1)
    
    
    
# if __name__ == "__main__":
#     main()


# --------------------------------------------------------------
# shift operators
num1 = 0b10001000

printb(num1 >> 1)
printb(num1 >> 3)

num = 0b00100100
printb(num << 2)