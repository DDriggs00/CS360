import nltk
# import re
import Dict


def append(tagged, Query, POS):
    temp = False
    i = 0
    for row in tagged:
        if temp:
            if tagged[i][1] != POS:
                break
        if tagged[i][1] == POS:
            Query += tagged[i][0]
            Query += ' '
            tagged[i] = ((tagged[i][0]), ('X' + tagged[i][1]))
            temp = True
        i += 1
    return Query


def append2(tagged, Query, POS, POS2):
    temp = False
    i = 0
    for row in tagged:
        if temp:
            if tagged[i][1] != POS2 and tagged[i][1] != POS:
                break
            else:
                Query += tagged[i][0]
                Query += ' '
                tagged[i] = ((tagged[i][0]), ('X' + tagged[i][1]))

        if tagged[i][1] == POS:
            Query += tagged[i][0]
            Query += ' '
            tagged[i] = ((tagged[i][0]), ('X' + tagged[i][1]))
            temp = True

        i += 1
    return Query


# select A.B from games as x, systems as y where x.system = y.system
# Start: What games were made for systems made by Nintendo
# Start: What games were made for Nintendo Systems
# Goal: select games.game from games, systems where
s = "What games were made for systems made by Nintendo"
Query = "select "

tokens = nltk.word_tokenize(s)
tagged = nltk.pos_tag(tokens)
print(tagged)

Query = append(tagged, Query, 'NNS')

print(Query)
print(tagged)

Query += 'from games, systems '     # Change later
Query += 'where games.system = systems.system '     # Change later

Query = append2(tagged, Query, 'VBN', 'IN')
Query = Dict.DoReplacing(Query)
print(Query)
print(tagged)
