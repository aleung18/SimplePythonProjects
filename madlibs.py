# string concatenation
# suppose we wanted to create a string that says "subscribe to ______"
youtuber = "Ashton Leung" # some string variable

# a few ways to ouput/print
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adj1 = input("Enter an adjective: ")
adj2 = input("Enter an adjective: ")
verb1 = input("Enter a verb: ")
verb2 = input("Enter a verb: ")
person = input("Enter the name of a person: ")

# the "\" tells python that string has gone on to next line
madlibs = f"Computer programming is so {adj1}! It makes me so {adj2} all the time because \
I love to {verb1}. Be yourself and {verb2} sandwiches like you are {person.capitalize()}."


# alternate way for madlibs

madlibs2 = "Computer programming is so " + adj1 + "! It makes me so " + adj2 + " all the time because \
I love to " + verb1 +". Be yourself and " + verb2 + " sandwiches like you are " + person.capitalize() + "."


print(madlibs)
print(madlibs2)
