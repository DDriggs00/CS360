import Dict             # Custom Replacements (local file)
from tenses import pluralize, singularize

import nltk             # For Parsing
# import re


def buildQuery(s):
    s = Dict.DoReplacing(s)
    s = s.strip()   # Remove Leading and Trailing Whitespace
    s = ReplaceNotFirst(s, 'where', 'and')

    tokens = nltk.word_tokenize(s)

    # Remove generic database references
    if s.lower().find("from database") != -1:
        s = Dict.Replace(s, [" from database"], '')
        tokens = nltk.word_tokenize(s)

    # if there is no "from"
    if s.find('from') == -1 and s.find('select') != -1:
        temp = tokens[tokens.index('select') + 1]
        temps = singularize(temp)
        tempp = pluralize(temps)
        s = s.replace('select ' + temp, 'select ' + temps + ' from ' + tempp)

        tokens = nltk.word_tokenize(s)

        tables = ['games', 'systems']   # Actually generate tables from db later
        if tokens[tokens.index('from') + 1] not in tables:
            s = noTableName(s, tables, tokens[tokens.index('from') + 1])

    s = s + ';'
    tokens = s.split(' ')
    # tokens = nltk.word_tokenize(s)
    tagged = nltk.pos_tag(tokens)
    print(tagged)

    s = manageStringVars(s, tokens)
    print(s)
    # above func takes in string and list, looks for operator and if the following
    # string is not a digit, then the function will add quotes to it

    return s


def ReplaceNotFirst(s, old, new):
    li = s.rsplit(old, s.count(old) - 1)
    return new.join(li)


def noTableName(s, tables, BadName):
    print("Which of the following tables is that most related to?")
    print(tables)
    validTable = False
    tableName = "INVALID"
    while validTable is False:
        tableName = input("Table: ")
        if tableName not in tables:
            print("Sorry, " + tableName + " is not a valid table name. Please enter a value from above.")
        else:
            validTable = True
    tableName = tableName.lower().capitalize()
    s = s.replace(BadName, tableName, 1)
    return(s)


def manageStringVars(s, sList):
    for w in range(len(sList)):
        if isComparisonOperator(sList[w]):
            if sList[w + 1].isdigit():
                continue
            else:
                sList[w + 1] = '\"' + sList[w + 1]
                counter = w + 1

                while not isEndofString(sList[counter]):    # index out of range error
                    if sList[counter].find('and') != -1:    # 'and' could be part of title or sql operator
                        if isComparisonOperator(sList[counter + 2]):    # 'and' not part of title
                            sList[counter - 1] = sList[counter - 1] + '\"'  # end of string
                            break  # done with loop
                    counter += 1

    s = ' '.join(sList)
    return s


def isComparisonOperator(w):
    compOps = ['=', '<', '>', '>=', '>=']
    if w in compOps:
        return True
    else:
        return False


def isEndofString(w):
    endOS = [';', ',']
    if w in endOS:
        return True
    else:
        return False
