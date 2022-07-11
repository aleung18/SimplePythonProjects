# user generates random number that computer has to guess

# personal version

from random import randint

lower = 1
upper = int(input("Please enter upper bound: "))
feedback = ""
num_tries = 0

while feedback != "c":
    
    if lower != upper:
        computer_guess = randint(lower, upper)
    else:
        computer_guess = lower # can also be upper because they are same value
    
    feedback = input(f"Is my guess ({computer_guess}) too low (L), too high (H), or correct (C)? ").lower()
    if feedback == "c":
        num_tries += 1
        print(f"Yay! I guessed the number ({computer_guess}) in {num_tries} tries")
    elif feedback == "l":
        num_tries += 1
        lower = computer_guess + 1
    elif feedback == "h":
        num_tries += 1
        upper = computer_guess - 1
