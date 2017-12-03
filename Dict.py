import re


def DoReplacing(String):
    Words = ['\.', '\:', '\;', '\'', '\"', '\?', '\,', 'a list of ', 'that were ', 'that are ', 'the ']
    Word = ''   # Words to be Removed
    String = Replace(String, Words, Word)

    Words = ['what', 'give me', 'show me', 'list', 'show', 'print out', 'display', 'retrieve', 'get', 'select']
    Word = 'select'  # Words that mean Select
    String = Replace(String, Words, Word)

    Words = ['that are in ', 'contained in ', 'in ', 'from ']
    Word = 'from '   # Words that mean From
    String = Replace(String, Words, Word)

    Words = ['everything', 'all items']
    Word = '\*'     # Words that mean everything
    String = Replace(String, Words, Word)

    Words = ['all ', 'every ']
    Word = ''       # Words to remove after replacing others
    String = Replace(String, Words, Word)

    Words = ['made by ', 'published by ', 'designed by ', 'where publisher = ']
    Word = 'where Publisher = '
    String = Replace(String, Words, Word)

    # Replace did * make
    Words = []
    Word = ''
    if String.find('did') != -1 and String.find('make') != -1:
        middle = re.findall(r'did(.*?)make', String)[0]
        Words.append('did' + middle + 'make')
        Word = 'where publisher = ' + middle.strip()
        String = Replace(String, Words, Word)
    if String.find('that') != -1 and String.find('made') != -1:
        middle = re.findall(r'that(.*?)made', String)[0]
        Words = ['that' + middle + 'made']
        Word = 'where publisher = ' + middle.strip()
        String = Replace(String, Words, Word)

    Words = ['before ']
    Word = 'where year < '
    String = Replace(String, Words, Word)

    Words = ['after ']
    Word = 'where year > '
    String = Replace(String, Words, Word)

    return String


# Replaces all occurences of all of the words in the Words array with the word in the Word variable
# Not Case Sensitive
def Replace(String, Words, Word):
    Replacer = re.compile(r'\b' + '|'.join(Words) + r'\b', re.IGNORECASE)
    String = Replacer.sub(Word, String)
    return String
