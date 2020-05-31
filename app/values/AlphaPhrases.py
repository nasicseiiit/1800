from itertools import product

def getPossiblePhraseforDigit(digit,alphaPhrasesFromDictionary):
    if digit in alphaPhrasesFromDictionary:
        return alphaPhrasesFromDictionary[digit]
    else:
        return []

def generateAllPossiblePhrases(allPossiblePhrases,listOfPhrases):
    result  = list(product(allPossiblePhrases, listOfPhrases))
    return result