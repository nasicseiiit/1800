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

'''
The method firstUnchangedDigit will return the allPossiblePhrases 
'''

def firstUnchangedDigit(phone_number,alphaPhrasesFromDictionary):
    digit = phone_number[0]
    listOfPhrases = getPossiblePhraseforDigit(digit,alphaPhrasesFromDictionary)  # getting the list of possible phrases of digit
    prevIndex = -2  # to know the consecutive unchanged digit
    if (len(listOfPhrases) == 0):
        listOfPhrases = [digit]
        prevIndex = 0
    allPossiblePhrases = listOfPhrases
    return  allPossiblePhrases,listOfPhrases,prevIndex

'''
The method firstUnchangedDigit will skip the phone number if more than two unchanged digits 
'''

def isHaveReplacementsFlagForNumber(allPossiblePhrases,phone_number,alphaPhrasesFromDictionary,prevIndex,digit_index):
    digit = phone_number[digit_index]
    listOfPhrases = getPossiblePhraseforDigit(digit, alphaPhrasesFromDictionary)
    if (len(listOfPhrases) == 0 and digit_index - prevIndex == 1):  # condition if the two consecutive digits are unchanged
        allPossiblePhrases = []  # then skipping the phone number to encode
    elif (len(listOfPhrases) == 0 and digit_index - prevIndex != 1):  # condition if the two consecutive digits are unchanged
        prevIndex = digit_index
        listOfPhrases = [digit]
    return allPossiblePhrases,listOfPhrases,prevIndex
