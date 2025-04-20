import random  # To let the computer make a random choice

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    print(f"Computer chose: {computer}")

    if user == computer:
        return "It's a tie!"

    if is_win(user, computer):
        return "You won!"
    
    return "You lost."

def is_win(player, opponent):
    # Returns True if the player beats the opponent
    # Rock beats scissors, scissors beats paper, paper beats rock
    return (player == 'r' and opponent == 's') or \
           (player == 's' and opponent == 'p') or \
           (player == 'p' and opponent == 'r')

# Run the game
print(play())
