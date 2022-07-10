# computer generates random number that user has to guess
# program returns whether user's guess is too high or low, as well as number of tries taken

from random import randint

# personal version

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


# video version

# def guess(x):
#     random_number = randint(1, x)
#     guess = 0
#     while(guess != random_number):
#         guess = int(input(f"Guess a number between 1 and {x}: "))
#         if guess < random_number:
#             print("Sorry, guess again. Too low")
#         elif guess > random_number:
#             print("Sorry, guess again. Too high")

#     print(f"Yay, congrats! You have guessed the number ({random_number})")

# guess(10)
