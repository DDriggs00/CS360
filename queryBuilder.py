import Dict             # Custom Replacements (local file)
from tenses import pluralize, singularize

import nltk             # For Parsing
# import re


def buildQuery(s):
    s = Dict.DoReplacing(s)
    # s = 'Show me when both Mario and Sonic first came out'
    s = s.strip()   # Remove Leading and Trailing Whitespace
    s = ReplaceNotFirst(s, 'where', 'and')
    s = s.replace('and and', 'and')
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

    if s[-1] != ';':
        s = s + ';'
    tokens = s.split(' ')
    # tokens = nltk.word_tokenize(s)
    # tagged = nltk.pos_tag(tokens)

    s = manageStringVars(s, tokens)
    # above func takes in string and list, looks for operator and if the following
    # string is not a digit, then the function will add quotes to it

    return s


# Replace all occurances starting with the second
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
            print("\033[91mSorry, " + tableName + " is not a valid table name. Please enter a value from above.\033[0m")
        else:
            validTable = True
    tableName = tableName.lower().capitalize()
    s = s.replace(BadName, tableName, 1)
    if tableName == "Systems":
        s = Dict.Replace(s, ["game"], "system")
        s = Dict.Replace(s, ["Publisher"], "Creator")
    return(s)


def manageStringVars(s, sList):
    # problem was that the semicolon wasn't its own string in the list. now it is and works
    endVarstr = sList.pop()
    endVarlst = endVarstr.split(';')
    sList.append(endVarlst[0])
    sList.append(';')
    for w in range(len(sList)):
        if sList[w] == 'in' and sList[w + 1] == '(':
            # if not sList[w + 2].isdigit():
            #     sList[w + 2] = '\"' + sList[w + 2]
            icounter = w + 2
            numComma = sList[w].count(',')
            while icounter < len(sList):
                if sList[icounter].find(',') != -1:
                    sList[icounter] = sList[icounter].rstrip(',')
                    if sList[icounter + 1] == 'and':
                        sList[icounter + 1] = '\"'
                        sList[icounter] = '\"' + sList[icounter] + '\"' + ','
                        icounter += 2
                    else:
                        if not sList[icounter].isdigit():
                            sList[icounter] = '\"' + sList[icounter] + '\"' + ','
                if numComma == 0 and sList[icounter] == 'and':
                    if not sList[icounter - 1].isdigit():
                        sList[icounter - 1] = '\"' + sList[icounter - 1] + '\"'
                        sList[icounter] = ','
                    if not sList[icounter + 1].isdigit():
                        sList[icounter + 1] = '\"' + sList[icounter + 1]
                if sList[icounter] == ';':
                    if not sList[icounter - 1].isdigit():
                        sList[icounter - 1] = sList[icounter - 1] + '\"'
                    sList[icounter] = ') ;'

                icounter += 1

        if isComparisonOperator(sList[w]):
            andFlg = False
            likeFlg = False
            if sList[w + 1].isdigit():
                if isEndofString(sList[w + 1]):
                    break
                continue
            else:
                likeFlg = True
                if 'like' not in sList[w]:
                    sList[w + 1] = '\"' + sList[w + 1]
                    likeFlg = False

                counter = w
                while not isEndofString(sList[counter]):
                    if sList[counter].find('and') != -1:    # 'and' could be part of title or sql operator
                        if isComparisonOperator(sList[counter + 2]):    # 'and' not part of title
                            sList[counter - 1] = sList[counter - 1] + '\"'  # end of string
                            andFlg = True
                            break  # done with loop
                    counter += 1

                if not andFlg:
                    if not likeFlg:
                        sList[counter - 1] = sList[counter - 1] + '\"'

    s = ' '.join(sList)
    s = s.rstrip(' ;')
    s = s + ';'     # to remove space between last word and semicolon
    s = s.replace('( ', '(')
    s = s.replace(' )', ')')
    s = s.replace(' \"', "\"")
    s = s.replace('\" ', '\"')
    s = s.replace(' , ', ', ')
    s = s.replace(',', ', ')
    return s


def isComparisonOperator(w):
    compOps = ['=', '<>', '<', '>', '>=', '>=', 'like', 'between']
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
