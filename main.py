import random

print("Hello! This is hangman, guess letters to solve the word. If you get it wrong, you will lose one of ten lives.")

def word():
    words = ["table", "happy", "classroom", "sphynx", "alternator"]
    return random.choice(words)

def display_word(word, guess):
    displayed_word = ""
    for letter in word:
        if letter in guess:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()

while True:
    guessing_word = word()
    lives = 10
    guessed = set()
    word_letters = set(guessing_word)
    tries = 0
    
    while lives > 0 and word_letters:  # Continue until we either run out of lives or guess the word
        print("\nLives = " + str(lives))
        print("Word to guess: " + display_word(guessing_word, guessed))  # Show word with blanks
        guess = input("Guess a letter: ").lower()
        tries = tries + 1
        
        # Validate the input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only a single letter.")
            continue
        
        if guess in guessed:
            print("You have already guessed that letter")
        elif guess in word_letters:
            guessed.add(guess)
            word_letters.remove(guess)
            print("Good guess!")
        else:
            lives -= 1
            guessed.add(guess)
            print("That letter is not in the word.")
        
        if not word_letters:
            print("\nHurray!!! You guessed the word: " + guessing_word + " correctly!")
            print("\nIt  took  you " + str(tries)  + " tries to guess " + guessing_word)
            break
    
    if lives == 0:
        print("\nI'm sorry, you're out of lives. The word was: " + guessing_word)
    
    play_again = input("\nWould you like to play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing!")
        break