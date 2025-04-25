import random
import string

# --- words.py content ---
words = [
    "abandon", "ability", "able", "about", "above", "absent", "absorb", "abstract", "absurd", "access",
    "accident", "account", "accuse", "achieve", "acoustic", "acquire", "across", "act", "action", "actor",
    "actress", "actual", "adapt", "add", "addict", "address", "adjust", "admit", "adult", "advance",
    # ... You can add more words here ...
]

# --- word selection function ---
def get_valid_word(word_list):
    word = random.choice(word_list)
    while '-' in word or ' ' in word:
        word = random.choice(word_list)
    return word.upper()

# --- hangman game ---
def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print(f"\nYou have {lives} lives left. Used letters: {' '.join(used_letters)}")

        word_display = [letter if letter in used_letters else '-' for letter in word]
        print("Current word:", ' '.join(word_display))

        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("Correct!")
            else:
                lives -= 1
                print("Wrong guess.")
        elif user_letter in used_letters:
            print("You already guessed that letter.")
        else:
            print("Invalid character. Please try again.")

    if lives == 0:
        print(f"\nYou died! The word was: {word}")
    else:
        print(f"\nYou guessed the word {word} successfully! You win 🎉")

# --- start the game ---
hangman()
