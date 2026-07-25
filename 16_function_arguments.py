
# default positional arguments
# def new_patient(name, type = 'cat', age = -1): # default positional argument
#     print(name, type, age)


# def main():
#     new_patient("Biffy", "dog", 5)
#     new_patient("Tiddle", "cat")
#     new_patient("Rover", "dog", 8)


# main()

# keyword arguments

# def new_fruit(color, weight, sweetness, location):
#     print(color)
#     print(weight)
#     print(sweetness)
#     print(location)
#     print()

# def main():
#     new_fruit("orange", 1, 60, "Columbia")
#     new_fruit(color="red", sweetness=50, weight=0.5, location="Nigeria") # keyword arguent


# main()


# variable length argument

# def describe_person(name, *attributes): # *attributes -> variable length argument know as *args
#     print(name)

#     # print(type(attributes)) #tupple

#     for attribute in attributes:
#         print(attribute)

# def main():
#     describe_person("Nicole Loco", "warm", "depressive", 'acerbic', 'funny')
#     print()
#     describe_person("Giffy Mcbeth")

# main()


# variable length keyword arguments

def add_description(**description): #**description -> variable length keyword arguments know as **kwargs
    # print(type(description)) #dict
    # print(description)

    for prop in description:
        print(prop, ":", description[prop])



def main():
    add_description(height=180, weight=90, eyes="blue")
    add_description(trouser="black", beard=True)
    add_description(sex="male", height=170)

main()