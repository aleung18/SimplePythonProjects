# computer generates random number that user has to guess
# program returns whether user's guess is too high or low, as well as number of tries taken

from random import randint

# video version

def guess(x):
    random_number = randint(1, x)
    guess = 0
    while(guess != random_number):
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again. Too low")
        elif guess > random_number:
            print("Sorry, guess again. Too high")

    print(f"Yay, congrats! You have guessed the number ({random_number})")

guess(10)
