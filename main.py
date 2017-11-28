import Dict
# import nltk

# Give me all the games in the database that were made before 2000
quit = 0
while True:
    InString = raw_input("Please enter a Query or \"Exit\" to quit\n")
    if InString.lower() == "exit":
        break

    InString = Dict.ReplaceSelect(InString)
    InString = Dict.ReplaceFrom(InString)
    InString = Dict.ReplaceStar(InString)

    print(InString)
