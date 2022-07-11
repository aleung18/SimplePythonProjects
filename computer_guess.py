# user generates random number that computer has to guess

# video version

from random import randint

def computer_guess(x):
    num_tries = 1
    lower_bound = 1
    upper_bound = x
    feedback = ""
    while feedback != "c":
        if lower_bound != upper_bound:
            guess = randint(lower_bound, upper_bound)
        else:
            num_tries += 1
            guess = lower_bound # can also be upper_bound b/c they are the same number in this conditional
        
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()
        if feedback == "h":
            num_tries += 1
            upper_bound = guess - 1
        elif feedback == "l":
            num_tries += 1
            lower_bound = guess + 1

    return f"Yay! The computer guessed your number ({guess}) in {num_tries} tries"

print(computer_guess(10))
