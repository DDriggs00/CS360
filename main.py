import Dict
import nltk
import sys

# GoodDb = False
# while GoodDb is False:
#     DB = input("Select Database to use or \"Exit\" to quit\n")
#     if DB.lower() == "exit":
#         sys.exit("Have a nice Day :)")
#     # else
#         # send "use" + DB to Sql
#         # if output returned true GoodDb = True


# Give me a list of all the games in the database that were made by nintendo before 2000
# what games did sega make?
# list all the games that nintendo made
# list every game

quit = 0
# while True:
Str = input("Please enter a Query or \"Exit\" to quit\n")
if Str.lower() == "exit":
    sys.exit("Have a nice Day :)")

Str = Dict.DoReplacing(Str)

tokens = nltk.word_tokenize(Str)
tagged = nltk.pos_tag(tokens)
print("\n")
print(tagged)

# Create MySQL Syntax
# print(Str)
