import random


print("Hello! This is hangman, guess letters to solve the five letter word. If you get it wrong, you will lose one of ten lives.")


def word():
    words = ["table", "happy", "classroom", "sphynx", "alternator"]
    return random.choice(words)

def display_word(word, guess):
    displayed_word = ""
    for letter in word:
        if letter in guess:
            displayed_word += letter + " "
        else:
            displayed_word += "_"
    return displayed_word.strip()

while True:
    guessing_word = word()
    lives = 10
    guesses = 0
    guessed = set()
    word_letters = set(guessing_word)
    alphabet = set(chr(i) for i in range(ord("a"), ord("z") + 1))

    while lives > 0 and len(word_letters):
        print("Lives = " + str(lives))

        guess = input("Guess a letter: ").lower()
        if guess in alphabet - guessed:
            guessed.add(guess)
            if guess in word_letters:
                word_letters.remove(guessed)
                print(" ")
            else:
                lives = lives - 1
                guesses = guesses + 1
                print("That letter is not in the word")

        elif guess in guessed:
            print("You have already guessed that letter")
        
        else:
            print("Sorry, I don't know that character. Pleased try again.")
    
    if lives == 0:
        print("I'm sorry, you're out of lives")
        print("You're word was: " + word)
    else: 
        print("Hurray!!! You guessed " + word + "correctly!")