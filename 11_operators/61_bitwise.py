
# bitwise 'OR' operator

def printb(value):
    # print("{:08b}".format(value))
    print(f"{value:08b}")
    
    

# def main():
#     # printb(118) # representing 118 into binary
    
#     number1 = 0b01110110
#     number2 = 0b00100011
    
#     printb(number1|number2) # gives 01110111 like logic or gate
    
    
# setting bitwise flags
class Flags:
    LOUDER = L = 1
    DENOISE = N = 2
    DEESS = S = 4
    NORMALIZE = O = 8
    REMOVECLICKS = R = 16
    
    
def main():
    # printb(Flags.L)
    # printb(Flags.N)
    # printb(Flags.S)
    
    conbined_flags = Flags.L | Flags.N
    printb(conbined_flags)


    # bitwise "AND" operator
    conbined_flags2 = Flags.L & Flags.N
    printb(conbined_flags2)

    
    
if __name__ == "__main__":
    main()