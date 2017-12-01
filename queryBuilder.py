import Dict             # Custom Replacements (local file)

import nltk             # For Parsing

def buildQuery(s):
    finalQuery = Dict.DoReplacing(s)
    s = s.strip()   # Remove Leading and Trailing Whitespace
    s = ReplaceNotFirst(s, 'where', 'and')


    tokens = nltk.word_tokenize(s)
    tagged = nltk.pos_tag(tokens)
    print(tagged)
    print("\n")

    return finalQuery


def ReplaceNotFirst(s, old, new):
    li = s.rsplit(old, s.count(old) - 1)
    return new.join(li)
