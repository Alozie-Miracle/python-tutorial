"""
CRUD

Create a program that displays the following menu:

1. Display database
2. Add an item
3. Delete an item
4. Chnage an item
5. Quit

The program contains a list of items; for example, fuits

if you select 1, the program displays the items in the list, numbering each item. for example

0: orange
1 banana
2: blackberry

if you select 2 the program asks you to enter a new item. It adds what you've types to the list

if you select 3, the program asks you to enter the list number of an item to delete. 
It deletes the specified item from the list.

if you select 4, the program asks you to enter the list number of an item you want to change,
then asks you to enter text. It changes the specified item to specified text.


if you select 5, the program quits.

until you quite with option 5, the program displays the menu again after everyh action.

"""


# solution
data = ["orange", "banana", "blackberry"]

def menu():
    options = ["1. Display database", "2. Add an item", "3. Delete an item", "4. Chnage an item", "5. Quit"]
    return options

def get_input(request):
    response = input(f"{request}: ")

    return response


def main():
    print("FRUIT DATABASE")
    options = menu()
    for option in options:
        print(option)

    print()

    option = int(get_input("Program Options"))

    if option == 5:
        quit()

    if option == 1:
        for i in range(len(data)):
            print(f"{i + 1}. {data[i]}")

        
    if option == 2:
        item = get_input("Enter the name of fruit to add")
        data.append(item)
        
        
        print(f"{item} has been added.")

    if option == 3:
        item = int(get_input("Enter index of the fruit ou want to remove"))
        deleted_item = data[item - 1]
        del data[item - 1]
        print(f"{deleted_item} has been deleted.")

    if option == 4:
        item = int(get_input("Enter index of the fruit ou want to change"))
        fruit = get_input("Enter the name of the fruit of want to add")
        
        print(f"{data[item - 1]} has been changed to {fruit}.")
        data[item - 1] = fruit



    print()



while True:
    main()
