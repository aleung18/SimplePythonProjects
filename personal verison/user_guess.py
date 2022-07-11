# computer generates random number that user has to guess
# program returns whether user's guess is too high or low, as well as number of tries taken

# personal version

from random import randint

random_number = randint(1, 9)

user_guess = ""
num_guesses = 0

while(user_guess != random_number):
    user_guess = int(input("Enter a number: "))
    if user_guess == random_number:
        num_guesses += 1
        print(f"Congrats! You got the number in {num_guesses} tries.")
    elif user_guess < random_number:
        num_guesses += 1
        print("Too low!")
    elif user_guess > random_number:
        num_guesses += 1
        print("Too high!")
