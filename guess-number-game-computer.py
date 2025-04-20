import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    
    print(f"Think of a number between 1 and {x}, and I will try to guess it.")
    
    while feedback != 'c':
        # Make the guess
        guess = random.randint(low, high)
        
        # Get feedback from the user
        feedback = input(f"Is your number {guess}? (Too high? Type 'h', too low? Type 'l', correct? Type 'c'): ").lower()

        # Adjust the guess range based on feedback
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'c':
            print(f" I guessed your number: {guess} successfully! 💐")
        else:
            print("Invalid input! Please enter 'h', 'l', or 'c'.")
            feedback = ''  # To make sure the loop continues if invalid input is given

# Start the game for numbers between 1 and 10
computer_guess(10)
