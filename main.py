import Dict.py
# import nltk

# Give me all the games in the database that are older than
quit = 0
while quit == 0:
    print("Please enter a Query")
    InString = input()

    Dict.ReplaceSelect(InString)
    Dict.ReplaceFrom(InString)
    Dict.ReplaceStar(InString)

    print(InString)
