import re


def DoReplacing(String):
    Words = ['\.', '\:', '\;', '\'', '\"', '\?', '\,', 'a list of ', 'that were ', 'that are ', 'the ']
    Word = ''   # Words to be Removed
    String = Replace(String, Words, Word)

    Words = ['what', 'give me', 'show me', 'list', 'show', 'print out', 'display', 'retrieve', 'get']
    Word = 'select'  # Words that mean Select
    String = Replace(String, Words, Word)

    Words = ['that are in', 'contained in', 'in']
    Word = 'From'   # Words that mean From
    String = Replace(String, Words, Word)

    Words = ['everything', 'all items']
    Word = '\*'     # Words that mean everything
    String = Replace(String, Words, Word)

    Words = ['all ', 'every ']
    Word = ''       # Words to remove
    String = Replace(String, Words, Word)

    Words = ['made by ', 'published by ']
    Word = 'where Publisher = '
    String = Replace(String, Words, Word)

    Words = ['before ']
    Word = 'where year < '
    String = Replace(String, Words, Word)

    Words = ['after ']
    Word = 'where year > '
    String = Replace(String, Words, Word)

    return String


# Replaces all occurences of all of the words in the Words array with the word in the Word variable
def Replace(String, Words, Word):
    Replacer = re.compile(r'\b' + '|'.join(Words) + r'\b', re.IGNORECASE)
    String = Replacer.sub(Word, String)
    return String
