import re

"""
    Create a class called Media
    Create the following subclassess: Book, Movie, Podcast
    
    Each subsclass should contain instance variable appropriate to type of media, and should be
    convertible to a string which displays this information.
    
    
    Create several instances of each class and add the to a container.
    
    Write a program that displays a prompt, like this:
    
    search >
    
    when the user enters a word or phrase, the program searches all the Media objects
    to find a match in their details. If any matches are found, it displays them.
    
    
    if no matches are found. it prints "No match".
    
    if the user types "quit"c, the program terminates. Otherwise is displays the prompt again
"""


class Media:
    def __init__(self, title):
        self._title = title
        
    def search_str(self):
        fields = vars(self)
        return " ".join(fields.values())


class Book(Media):
    def __init__(self, title, author):
        super().__init__(title)
        self._author = author
        
    def __str__(self):
        return f"Title: {self._title}\nAuthor: {self._author}"


class Movie(Media):
    def __init__(self, title, director):
        super().__init__(title)
        self._director = director
        
    def __str__(self):
        return f"Title: {self._title}\nDirector: {self._director}"

class Podcast(Media):
    def __init__(self, title, episode):
        super().__init__(title)
        self._episode = episode
        
    def __str__(self):
        return f"Title: {self._title}\nEpisode: {self._episode}"



media = [
    Book("Jouney to the centre of the Earth", "Jules Verne"),
    Book("Moby Dick", "Herman Melville"),
    Book("A Tale of two cities", "Charles Dickens"),
    Movie("Limitless", "Weil Burger"),
    Movie("Withnail and I", "Bruce Robinson"),
    Podcast("Cave of Programming Postcast", "Epsiode 1: Why Learn to Code?"),
    Podcast("Skeptiko", "Is the Dalai Lama an Atheist?")
]

while True:
    text = input('search > ')
    
    if text == 'quit':
        break
    elif len(text) == 0:
        continue

    regex = re.escape(text)
    
    matches_found = False
    
    for m in media:
        if re.search(regex, m.search_str(), flags=re.IGNORECASE) is not None:
            matches_found = True
            print(m)
            print()
            
    if matches_found is False:
        print("No matches")
    
    
    
