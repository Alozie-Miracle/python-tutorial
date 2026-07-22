"""
Define a single function that accepts
one or more positional arguments
zero or more variable arguments
zero or more variable arguments

maker the function print out all arguments it receives

"""



def accept_data(one, two, three, *args, **kwargs):
    print(one, two, three)
    for i in args:
        print(i)

    for i in kwargs:
        print(i, ":", kwargs[i])


def main():
    accept_data(1, 2, 3, "hi", "hello", five=5, six=6)


main()