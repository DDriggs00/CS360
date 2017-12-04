import re


def DoReplacing(String):
    Words = ['\.', '\:', '\;', '\'', '\"', '\?', ',', '%', 'a list of ', 'that were ', 'that are ', 'the ', 'were ', 'are ', 'in the database ', 'in database ']
    Word = ''   # Words to be Removed
    String = Replace(String, Words, Word)

    Words = ['when ']
    Word = 'select year '   # Words to be Removed
    String = Replace(String, Words, Word)

    Words = ['what', 'give me', 'show me', 'list', 'show', 'print out', 'display', 'retrieve', 'get', 'select']
    Word = 'select'  # Words that mean Select
    String = Replace(String, Words, Word)

    Words = ['How Many']
    Word = r'select count(*) from'  # Words that mean Select
    String = Replace(String, Words, Word)

    Words = ['that are in ', 'contained in ', 'from ']
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

    Words = ['before ', 'prior to ']
    Word = 'where year < '
    String = Replace(String, Words, Word)

    Words = ['released in ', 'released during ', 'released on']
    Word = 'where year = '
    String = Replace(String, Words, Word)

    Words = ['after ']
    Word = 'where year > '
    String = Replace(String, Words, Word)

    Words = ['come out in', 'come out on', 'come out', 'get released', 'released', 'release']
    Word = 'release'
    String = Replace(String, Words, Word)

    Words = ['release between', 'came out between', 'published between']
    Word = 'where year between'
    String = Replace(String, Words, Word)

    Words = []
    # Replace that * made
    if String.find('that') != -1 and String.find('made') != -1:
        middle = re.findall(r'that(.*?)made', String)[0]
        Words = ['that' + middle + 'made']
        Word = 'where publisher = ' + middle.strip()
        String = Replace(String, Words, Word)

    Words = []
    # Replace was * released
    if String.find('was') != -1 and String.find('release') != -1:
        middle = re.findall(r'was(.*?)release', String)[0]
        Words = ['was' + middle + 'release']
        Word = 'where game = ' + middle.strip()
        String = Replace(String, Words, Word)

    Words = []
    # Replace did * release
    if String.find('did') != -1 and String.find('release') != -1:
        middle = re.findall(r'did(.*?)release', String)[0]
        Words = ['did' + middle + 'release']
        if String.find('game') == -1:
            Word = 'where game = ' + middle.strip()
        else:
            Word = 'where Publisher = ' + middle.strip()
        String = Replace(String, Words, Word)

    Words = []
    # Replace did * make
    if String.find('did') != -1 and String.find('make') != -1:
        middle = re.findall(r'did(.*?)make', String)[0]
        Words.append('did' + middle + 'make')
        Word = 'where publisher = ' + middle.strip()
        String = Replace(String, Words, Word)

    Words = []
    # Replace with * in title
    if String.find('with') != -1 and String.find('in title') != -1:
        middle = re.findall(r'with(.*?)in title', String)[0]
        Words = ['with' + middle + 'in title']
        if String.find('game') != -1:
            Word = 'where game like ' + middle.strip()
        else:
            Word = 'where System like ' + middle.strip()
        String = Replace(String, Words, Word)
        String = String.replace(middle.strip(), '\"%' + middle.strip() + '%\"')

    return String


# Replaces all occurences of all of the words in the Words array with the word in the Word variable
# Not Case Sensitive
def Replace(String, Words, Word):
    Replacer = re.compile(r'\b' + '|'.join(Words) + r'\b', re.IGNORECASE)
    String = Replacer.sub(Word, String)
    return String
