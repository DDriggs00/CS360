import re


def ReplaceSelect(String):
    ReplacedWords = ['give me', 'show me', 'list', 'show', 'print out', 'display']
    ReplaceWord = 'Select'
    for word in ReplacedWords:
        Replacer = re.compile(re.escape(word), re.IGNORECASE)
        Replacer.sub(ReplaceWord, String)

def ReplaceFrom(String):
    ReplacedWords = ['that are in', 'contained in', 'in']
    ReplaceWord = 'From'
    for word in ReplacedWords:
        Replacer = re.compile(re.escape(word), re.IGNORECASE)
        Replacer.sub(ReplaceWord, String)

def ReplaceStar(String):
    ReplacedWords = ['everything', 'all items']
    ReplaceWord = '\*'
    for word in ReplacedWords:
        Replacer = re.compile(re.escape(word), re.IGNORECASE)
        Replacer.sub(ReplaceWord, String)
