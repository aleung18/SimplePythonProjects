# rock paper scissors game between the user and the computer

# personal version

from random import choice


def output(user, computer, winner, rslt):
    if rslt == "tie":
        return f"Your choice: {user}\nComputer's choice: {computer}\nIt's a tie!"  
    return f"Your choice: {user}\nComputer's choice: {computer}\n{winner} wins!"

def rock_paper_scissors():
    user_choice = input("Choose rock (r), paper (p), or scissors (s): ")
    computer_choice = choice(["r", "p", "s"])
    winner = "Computer"
    result = "lose"

    if user_choice == computer_choice:
        result = "tie"
        return output(user_choice, computer_choice, winner, result)
    elif (user_choice == "r" and computer_choice == "s") or (user_choice == "s" and computer_choice == "p") or (user_choice == "p" and computer_choice == "r"):
        result = "win"
        winner = "User"
        return output(user_choice, computer_choice, winner, result)
    return output(user_choice, computer_choice, winner, result)
    

print(rock_paper_scissors())

# video version

# import random

# def play():
#     user = input("Choose rock (r), paper (p), or scissors (s): ")
#     computer = random.choice(["r", "p", "s"])

#     if user == computer:
#         return "It's a tie!"

#     elif is_win(user, computer):
#         return "You won!"
    
#     return "You lost!"

# def is_win(player, opponent):
#     # return true if player wins
#     # r > s, s > p, p > r
#     if (player== "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and opponent == "r"):
#         return True

# print(play())
