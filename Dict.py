import re


def DoReplacing(String):
    Words = ['give me', 'show me', 'list', 'show', 'print out', 'display', 'retrieve', 'get']
    Word = 'select'
    String = Replace(String, Words, Word)

    Words = ['that are in', 'contained in', 'in']
    Word = 'From'
    String = Replace(String, Words, Word)

    Words = ['everything', 'all items']
    Word = '\*'
    String = Replace(String, Words, Word)

    return String


def Replace(String, Words, Word):
    Replacer = re.compile(r'\b' + '|'.join(Words) + r'\b', re.IGNORECASE)
    String = Replacer.sub(Word, String)
    return String
