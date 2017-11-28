import re


def ReplaceSelect(String):
    ReplacedWords = ['give me', 'show me', 'list', 'show', 'print out', 'display', 'retrieve', 'get']
    ReplaceWord = 'select'

    Replacer = re.compile(r'\b' + '|'.join(ReplacedWords) + r'\b', re.IGNORECASE)
    String = Replacer.sub(ReplaceWord, String)
    return String


def ReplaceFrom(String):
    ReplacedWords = ['that are in', 'contained in', 'in']
    ReplaceWord = 'From'

    Replacer = re.compile(r'\b' + '|'.join(ReplacedWords) + r'\b', re.IGNORECASE)
    String = Replacer.sub(ReplaceWord, String)
    return String


def ReplaceStar(String):
    ReplacedWords = ['everything', 'all items']
    ReplaceWord = '\*'

    Replacer = re.compile(r'\b' + '|'.join(ReplacedWords) + r'\b', re.IGNORECASE)
    String = Replacer.sub(ReplaceWord, String)
    return String
