

def get_user_info():
    name = input("Enter your name: ")
    height = input("Enter your height: ")


    return name, height


def main():
    name, height = get_user_info() # return a tupple (name, height)

    print(name, ", ", height)

main()


