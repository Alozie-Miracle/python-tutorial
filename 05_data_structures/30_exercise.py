"""
Put this data in a suitable data structure

Science Fiction: Journey to the Centre of the Earth, Day of the Triffids
Drama: A Tale of Two Cities, Moby Dick


Assume:
1. Categories are unique (cannot have two different categories with the same name)
2. Book titles are unique
3. We want to be able to easily determine which books are in a given category
4. The order of book titles doesn't matter
5. we want to be able to quickly determine if a given book is present in a given category
6. We want to be able to easily add books to a category.



Now programmatically add this book:

Science Fiction: The War of Worlds

Do not assume that the category already exists in the data structure. Write a code that will 
add the book whether the category already exists or not.

Write code that prints all categories and book in them

Write a function that can determine whether a particular book is present in the data structure
without knowing the category.

"""

def add(book, library):
    pass



def show_categories(library):
    print()
    print("Categories")
    for i, category in enumerate(library):
        print(f"{i + 1}. {category}")


def show_category(response, library):
    print()
    print("Books in the category")
    if len(response) == 1:
        for i, category in enumerate(library):
            if i == int(response) - 1:
                for j, book in enumerate(library[category]):
                    print(f"{j}. {book}")
    else:
        for category in library:
            if category.lower() == response:
                for i, book in enumerate(library[category]):
                    print(f"{i}. {book}")

def add_book(library):
    category = input("Enter category name: ")
    book = input("Enter book name: ")

    if not category in library:
        library[category] = set()

    library[category.title()].add(book) #you can also use .update({ book })
    print(f"{book} added to {category.title()} category")
    for i, category in enumerate(library):
        print(f"{category}: ")
        for j, book in enumerate(library[category]):
            print(f"{j + 1}. {book}")
        print()


def find_book(library):
    book = input("Enter book name: ")
     
    for val in library.values():
        for item in val:
            if book.lower() == item.lower():
                print(f"{book.title()} found.")
                return

    print(f"{book} not in the library.")
    


def main():
    library = {
        "Science Fiction": {"Journey to the Centre of the Earth", "Day of the Triffids"},
        "Drama": {"A Tale of Two Cities", "Moby Dick"}
    }
    print()
    print("Welcome to our library")
    print("1. Show Categories")
    print("2. Add Book")
    print("3. Find Book")
    print("4. quit")

    option = input("Pick option: ").lower()
    if option == 'quit' or option == '4':
        quit()

    if option == '1' or option == 'show categories':
        show_categories(library)
        response = input("Pick a category: ").lower()
        show_category(response, library)

    if option == "2" or option == "add book":
        print()
        add_book(library)
    
    if option == "3" or option == "find book":
        find_book(library)




while True:
    main()

