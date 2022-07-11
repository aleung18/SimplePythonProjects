# personal version

from random import choice
from words import word_lst

templates = ["""
         __________
        |          |
        |
        |
        |
        |
        |   
        |
        |
---------------------
""",

"""
         __________
        |          |
        |          0 
        |          
        |          
        |
        |   
        |
        |
---------------------
""",

"""
         __________
        |          |
        |          0 
        |          |
        |          |
        |
        |   
        |
        |
---------------------
""",

"""
         __________
        |          |
        |          0 
        |         \|
        |          |
        |
        |   
        |
        |
---------------------
""",

"""
         __________
        |          |
        |          0 
        |         \|/
        |          |
        |
        |   
        |
        |
---------------------
""",

"""
         __________
        |          |
        |          0 
        |         \|/
        |          |
        |         /
        |   
        |
        |
---------------------
"""]

computer_word = choice(word_lst)

placeholders = "_" * len(computer_word)
word_template = "Guess the word: " + (placeholders)

template_count = 0
word_incomplete = True # serves as gameover boolean

user_word = ""
output_msg = """
         __________
        |          |
        |          0 
        |         \|/
        |          |
        |         / \\
        |   
        |
        |
---------------------
""" + f"Sorry, the word was '{computer_word}'"

# returns list of letters where user's guess matches with letter of computer's word
def letter_match(letter, word):
    letter_lst = []
    for i in range(len(word)):
        if letter == word[i:i+1]:
            letter_lst.append(letter)
    return letter_lst

def find_index(letter, word):
    index_lst = []
    for i in range(len(word)):
        if letter == word[i:i+1]:
            index_lst.append(i)
    return index_lst

while (template_count < 6) and word_incomplete:
    print(templates[template_count])
    print(word_template + "\n")
    user_guess = input("Enter a letter: ").lower()

    idx_lst = find_index(user_guess, computer_word)
    ltr_lst = letter_match(user_guess, computer_word)

    # checks to see if ltr_index_lst contains indices or if it is empty, determines whether letter is in the word or not
    if not ltr_lst:
        print(f"Sorry, the letter '{user_guess}' is not in the word!")
        template_count += 1 

    for idx in idx_lst:
        word_template = word_template[:idx+16] + user_guess + word_template[idx+17:]

    if word_template[16:] == computer_word:
        word_incomplete = False
        output_msg = f"Congrats, you guessed the word ({computer_word})!"


print(output_msg)
