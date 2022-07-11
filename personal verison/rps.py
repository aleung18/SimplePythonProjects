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
