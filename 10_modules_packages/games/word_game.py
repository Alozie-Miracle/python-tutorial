import random

class WordGame:
    def __init__(self, *words):
        # list of possible words
        self._words = words

        # set of correctly guessed letters
        self._guesses = set()

        # set of all the letters in the word
        self._letters = set()

        # number of guesses made by the user
        self._number_guesses = 0

        # the word to guess
        self._word = None

    def _choose_word(self):
        # pick random word from words and assign to self._word
        self._word = random.choice(self._words)


        # add all the letters of the word (separately) to self._letters
        # self._letters.update(self._word[i] for i in range(len(self._word)))
        self._letters.update(self._word)
        return self._letters

    def _guess_letter(self):
        # Ask the user to guess a letter
        user_input = input("Enter a letter: ").lower()

        if len(user_input) == 0:
            return

        # Add the letter guessed by the user to self._guesses,
        # Only if the letter is actually in the word
        if user_input in self._word:
            self._guesses.add(user_input)

        # Increment the number of guesses
        self._number_guesses += 1
        

    def _show_word(self):
        # display the word, but:

        # for any letters that aren't gueesed yet, display '_'
        # for any letters that have been guessed by now, display the letter
        # space out all the letters and hyphens
        for word in self._word:
            if word in self._guesses:
                print(f"{word}", end=" ")
            else:
                print(f"_", end=" ")

        print('\n')

    def _display_result(self):
        print(f"Guessed {self._word} in {self._number_guesses} guesses")

    def run(self):
        self._choose_word()
        
        while self._guesses != self._letters:
            self._show_word()
            self._guess_letter()


        self._display_result()
        # print(self._guesses, self._letters)


class App:
    def run(self):
        game = WordGame("peach", "alligator", "sky", "fascinate")
        game.run()


def main():
    app = App()
    app.run()
    

if __name__ == '__main__':
    main()