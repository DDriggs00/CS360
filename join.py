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


def join(s, tables):
    Query = "select "

    tokens = nltk.word_tokenize(s)
    tagged = nltk.pos_tag(tokens)

    Query = append(tagged, Query, 'NNS')

    tables = ['games', 'systems']
    for table in tables:
        Query = Query.replace(table, table + '.' + singularize(table))
        Query = Query.replace(' ' + singularize(table) + ' ', ' ' + pluralize(table) + '.' + table + ' ')

    # From
    Query += 'from '
    for table in tables:
        Query += table
        Query += ', '
    Query = Query.strip(', ') + ' '

    # Actual Joining
    Query += 'where games.system = systems.system '     # Change later

    # Nintendo Systems ==> Systems made by Nintendo
    temp = False
    i = 0
    for row in tagged:
        if tagged[i][1] == 'NNP' and i + 1 < len(tagged):
            if tagged[i + 1][1] == 'NNPS':
                Query += tagged[i + 1][0]
                Query += '.made by '
                Query += tagged[i][0]
                Query += ' '
                tagged[i] = ((tagged[i][0]), ('X' + tagged[i][1]))
                tagged[i + 1] = ((tagged[i + 1][0]), ('X' + tagged[i + 1][1]))
                break

        i += 1

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
    for i in range(0, len(tagged)):
        if tagged[i][1][0] == 'Z':
            flag = True
        if flag:
            if tagged[i][1] == 'ZNNS':
                temp = tagged[i][0] + '.'
                Query += temp
            elif tagged[i][1] == 'ZNNP' and i + 1 < len(tagged):
                Query += tagged[i][0] + ' '
                Query += temp
            else:
                Query += tagged[i][0]
                Query += ' '

        i += 1
    Query = Dict.DoReplacing(Query)

    for table in tables:
        Query = Dict.Replace(Query, [table + '\.where '], 'where ' + table + '.')

    return Query
