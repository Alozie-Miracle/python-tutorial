# tupples are container type to contain data and it's immutable
# tupples are ordered
# tupples are list of things

def main():
    animals = ("dog", "cat", "tigger", "cat", "wolf")

    print(type(animals))

    number_of_animals = len(animals)
    print(number_of_animals)

    print(animals[0]) #dog

    print()

    for animal in animals:
        print(animal)

    print()
    for i in range(0, len(animals)):
        print(animals[i])


main()