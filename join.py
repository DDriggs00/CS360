import nltk
# import re
import Dict
from tenses import pluralize, singularize


def append(tagged, Query, POS):
    i = 0
    for row in tagged:
        if tagged[i][1] == POS:
            Query += tagged[i][0]
            Query += ' '
            tagged[i] = ((tagged[i][0]), ('X' + tagged[i][1]))
            break
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
# s = "Give me a list of all the games in the database that were made by Nintendo before 2000 and have mario in the title"
Query = "select "

tokens = nltk.word_tokenize(s)
tagged = nltk.pos_tag(tokens)
print(tagged)

Query = append(tagged, Query, 'NNS')

tables = ['games', 'systems']
for table in tables:
    Query = Query.replace(table, table + '.' + singularize(table))
    Query = Query.replace(' ' + singularize(table) + ' ', ' ' + pluralize(table) + '.' + table + ' ')

print(Query)
print(tagged)

Query += 'from '

Query += tables[0]
Query += ', '
Query += tables[1]
Query += ' '

Query += 'where games.system = systems.system '     # Change later

print(Query)
print(tagged)

i = 0
flag = False
for row in tagged:
    if tagged[i][1] == 'NNS':
        flag = True
    if flag:
        tagged[i] = ((tagged[i][0]), ('Z' + tagged[i][1]))
    i += 1

i = 0
flag = False
for row in tagged:
    if tagged[i][1][0] == 'Z':
        flag = True
    if flag:
        if tagged[i][1] == 'ZNNS':
            Query += tagged[i][0]
            Query += '.'
        else:
            Query += tagged[i][0]
            Query += ' '

    i += 1
Query = Dict.DoReplacing(Query)

Query = Query.replace('systems.where ', 'where systems.')
Query = Query.replace('games.where ', 'where games.')

print(Query)
print(tagged)
