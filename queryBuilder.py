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
    if s.find('from') == -1:
        s = noTableName(s)
        if s.find('select') != -1:
            temp = tokens[tokens.index('select') + 1]
            temps = singularize(temp)
            tempp = pluralize(temps)
            s = s.replace('select ' + temp, 'select ' + temps + ' from ' + tempp)
            print(s)
            tokens = nltk.word_tokenize(s)

    tagged = nltk.pos_tag(tokens)
    print(tagged)

    s = manageStringVars(s, tokens)
    # above func takes in string and list, looks for operator and if the following
    # string is not a digit, then the function will add quotes to it

    return s


def ReplaceNotFirst(s, old, new):
    li = s.rsplit(old, s.count(old) - 1)
    return new.join(li)

def noTableName(s):
    print("Table is not defined, which of the following tables would you like to query?")
    print("Games       Systems")

    validTable = False
    tableName = "INVALID"
    while validTable is False:
        tableName = input("Table Name: ")
        if tableName not in ['Games', 'Systems']:
            print("Sorry, the Database doesn't have info on " + tableName + " please try again.")
        else:
            validTable = True
    splitQuery = s.split('where')
    if len(splitQuery) == 1:
        s = s + 'from ' + tableName + ';'
        return s
    else:
        splitQuery[0] = splitQuery[0] + 'from ' + tableName + ' '
        s = splitQuery[0] + splitQuery[1]
        return s

def manageStringVars(s, sList):
    for w in range(len(sList)):
        if isComparisonOperator(sList[w]):
            if sList[w + 1].isdigit():
                continue
            else:
                sList[w + 1] = '\"' + sList[w + 1]
                counter = w + 1
                while !isEndofString(sList[counter]):
                    if 'and' in sList[counter]: # 'and' could be part of title or sql operator
                        if isComparisonOperator(sList[counter + 2]): # 'and' not part of title
                            sList[counter -1] = sList[counter -1] + '\"' # end of string
                            break # done with loop
                    sList[counter] = sList[counter]
                    counter++

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
