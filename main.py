import Dict
import nltk

# Give me a list of all the games in the database that were made by nintendo before 2000
quit = 0
# while True:
InString = input("Please enter a Query or \"Exit\" to quit\n")
#     if InString.lower() == "exit":
#         break

tokens = nltk.word_tokenize(InString)
tagged = nltk.pos_tag(tokens)
entities = nltk.chunk.ne_chunk(tagged)
print("\n")
print(entities)

# InString = Dict.DoReplacing(InString)
# Create MySQL Syntaxtet
# print(InString)
