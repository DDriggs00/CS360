import Dict             # Custom Replacements (local file)

import nltk             # For Parsing
from pattern.en import pluralize, singularize


def buildQuery(s):
    s = Dict.DoReplacing(s)
    s = s.strip()   # Remove Leading and Trailing Whitespace
    s = ReplaceNotFirst(s, 'where', 'and')

    tokens = s.split(' ')

    # if there is no "find"
    if s.lower().find('from') == -1:
        temp = tokens[tokens.index('select') + 1]
        temp2 = singularize(temp)
        temp = pluralize(temp2)
        s = s.replace('select ' + temp, 'select ' + temp2 + ' from ' + temp)

    tagged = nltk.pos_tag(tokens)
    print(tagged)
    print("\n")

    return s


def ReplaceNotFirst(s, old, new):
    li = s.rsplit(old, s.count(old) - 1)
    return new.join(li)
