#### written by nasicseiiit@gmail.com(Nasimunni Attaru) ###

from itertools import product

'''
The method getPossiblePhraseforDigit will return the all Alpha Phrases of each digit from the Dictionary
'''

def getPossiblePhraseforDigit(digit,alphaPhrasesFromDictionary):
    if digit in alphaPhrasesFromDictionary:
        return alphaPhrasesFromDictionary[digit]
    else:
        return []

'''
The method generateAllPossiblePhrases will return the all possible Alpha Phrases of each phone number 
'''

def generateAllPossiblePhrases(allPossiblePhrases,listOfPhrases):
    result  = list(product(allPossiblePhrases, listOfPhrases))
    return result