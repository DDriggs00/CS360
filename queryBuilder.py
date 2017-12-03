import Dict             # Custom Replacements (local file)
from tenses import pluralize, singularize

import nltk             # For Parsing
# import re


def buildQuery(s):
    s = Dict.DoReplacing(s)
    s = s.strip()   # Remove Leading and Trailing Whitespace
    s = ReplaceNotFirst(s, 'where', 'and')

    tokens = nltk.word_tokenize(s)

    # Remove ganaric database references
    if s.lower().find("from database") != -1:
        s = Dict.Replace(s, [" from database"], '')
        tokens = nltk.word_tokenize(s)

    # if there is no "from"
    if s.find('from') == -1 & s.find('from') != -1:
        temp = tokens[tokens.index('select') + 1]
        temps = singularize(temp)
        tempp = pluralize(temps)
        s = s.replace('select ' + temp, 'select ' + temps + ' from ' + tempp)
        print(s)
        tokens = nltk.word_tokenize(s)

    tagged = nltk.pos_tag(tokens)
    print(tagged)
    print("\n")
    sList = s.split(' ') # list for finding and adding quotes where necessary
    s = manageStringVars(s, sList)
    # above func takes in string and list, looks for operator and if the following
    # string is not a digit, then the function will add quotes to it

    return s


def ReplaceNotFirst(s, old, new):
    li = s.rsplit(old, s.count(old) - 1)
    return new.join(li)

def manageStringVars(s, sList):
    for w in range(len(sList)):
        if isComparisonOperator(sList[w]):
            if sList[w+1].isdigit():
                continue
            else:
                sList[w+1] = '"{}"'.format(sList[w+1])

    s = ' '.join(sList)
    return s

def isComparisonOperator(w):
    compOps = ['=', '<', '>', '>=', '>=']
    if w in compOps:
        return True
    else:
        return False
