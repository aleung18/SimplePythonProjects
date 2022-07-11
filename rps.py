# rock paper scissors game between the user and the computer

# video version

import random

def play():
    user = input("Choose rock (r), paper (p), or scissors (s): ")
    computer = random.choice(["r", "p", "s"])

    if user == computer:
        return "It's a tie!"

    elif is_win(user, computer):
        return "You won!"
    
    return "You lost!"

def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player== "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and opponent == "r"):
        return True

print(play())
