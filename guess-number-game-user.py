import random

def guess_the_number():
    print(" Welcome to the Guess the Number Game!")
    print("I have selected a number between 1 and 10.")
    
    number_to_guess = random.randint(1, 10)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1

            if guess < 1 or guess > 10:
                print("Please guess a number between 1 and 10.")
            elif guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f" Congratulations! You guessed the number {number_to_guess} in {attempts} tries.")
                break
        except ValueError:
            print("Please enter a valid number.")

# Run the game
guess_the_number()
