import Dict             # Custom Replacements (local file)
from tenses import pluralize, singularize

import nltk             # For Parsing


def buildQuery(s):
    s = Dict.DoReplacing(s)
    s = s.strip()   # Remove Leading and Trailing Whitespace
    s = ReplaceNotFirst(s, 'where', 'and')

    tokens = s.split(' ')

    # if there is no "find"
    if s.lower().find('from') == -1:
        temp = tokens[tokens.index('select') + 1]
        temps = singularize(temp)
        tempp = pluralize(temps)
        s = s.replace('select ' + temp, 'select ' + temps + ' from ' + tempp)
        print(s)
        tokens = s.split(' ')

    tagged = nltk.pos_tag(tokens)
    print(tagged)
    print("\n")

    return s


def ReplaceNotFirst(s, old, new):
    li = s.rsplit(old, s.count(old) - 1)
    return new.join(li)
