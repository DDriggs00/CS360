import Dict     # Custom Replacements (local file)
import nltk     # For Parsing
import sys      # for sys.exit


def ReplaceNotFirst(s, old, new, occurrence):
    li = s.rsplit(old, occurrence)
    return new.join(li)


# GoodDb = False
# while GoodDb is False:
#     DB = input("Select Database to use or \"Exit\" to quit\n")
#     if DB.lower() == "exit":
#         sys.exit("Have a nice Day :)")
#     # else
#         # send "use" + DB to Sql
#         # if output returned true GoodDb = True

quit = 0
# while True:
# s = input("Please enter a Query or \"Exit\" to quit\n")
s = "Give me a list of all the games in the game database that were made by nintendo before 2000"
if s.lower() == "exit":
    sys.exit("Have a nice Day :)")

s = Dict.DoReplacing(s)

if s.lower().find("from database") != -1:
    print("Please select a valid Database Table (Tables are listed below)")
    # MySQL Query show tables
    # continue

s = ReplaceNotFirst(s, 'where', 'and', s.count('where') - 1)

tokens = nltk.word_tokenize(s)
tagged = nltk.pos_tag(tokens)
print(tagged)
print("\n")
print(s)

# Create MySQL Syntax
# print(s)
