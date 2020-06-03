#### written by nasicseiiit@gmail.com(Nasimunni Attaru) ###

from app.getters.CliArguments import getCliArguments
from app.getters.DictionaryData import getDictionaryData
from app.getters.InputData import getInputData
from app.helper.GenericHelper import checkFileExistance, replaceDotWithHyphen, removeEveryPunctuation, convertListOfStringsToCapitalString
from app.getters.PhoneNumbersData import getListOfNumbersInDirectory
from app.helper.PrintOutputData import printOutputData
from app.values.AlphaPhrases import getPossiblePhraseforDigit, generateAllPossiblePhrases

'''
The method getAlphaPhrasesForEachNumber will get the all possible Alpha phrases of a phone number  
'''
def getAlphaPhrasesForEachNumber(phone_number,alphaPhrasesFromDictionary):
    phone_number = replaceDotWithHyphen(phone_number) #replacing all the dots in the phone number with the Hyphen
    phone_number = removeEveryPunctuation(phone_number) #removing all the punctuations in the phone number
    digit = phone_number[0]
    listOfPhrases = getPossiblePhraseforDigit(digit,alphaPhrasesFromDictionary) #getting the list of possible phrases of digit
    prevIndex = -2 #to know the consecutive unchanged digit
    if(len(listOfPhrases)==0):
        listOfPhrases = [digit]
        prevIndex = 0
    allPossiblePhrases = listOfPhrases
    for digit_index in range(1,len(phone_number)):
        digit = phone_number[digit_index]
        listOfPhrases = getPossiblePhraseforDigit(digit,alphaPhrasesFromDictionary)
        if (len(listOfPhrases) == 0): #condition if the two consecutive digits are unchanged
            if(digit_index-prevIndex == 1):
                allPossiblePhrases=[] #then skipping the phone number to encode
                break
            else:
                prevIndex = digit_index
                listOfPhrases = [digit]
        alpha_phrases = generateAllPossiblePhrases(allPossiblePhrases,listOfPhrases)#generating all possible alpha phrases of phone number
        allPossiblePhrases = convertListOfStringsToCapitalString(alpha_phrases)
    return allPossiblePhrases

'''
The method getAlphaPhrasesForDirectoryNumbers is used to generate all possible phrases of phone numbers of phone directory 
'''
def getAlphaPhrasesForDirectoryNumbers(listOfNumbersFromDirectory,alphaPhrasesFromDictionary):
    allPossiblePhrasesOfAllNumbers = {}
    skipped_phone_numbers = [] #to hold the skipped phone numbers which are not converted
    for phone_number in listOfNumbersFromDirectory : #printing the all possible alpha phrases of phone number
        allPossiblePhrases = getAlphaPhrasesForEachNumber(phone_number,alphaPhrasesFromDictionary)
        if(len(allPossiblePhrases)>0):
            allPossiblePhrasesOfAllNumbers[phone_number]=allPossiblePhrases
        else:
            skipped_phone_numbers.append(phone_number)
    return allPossiblePhrasesOfAllNumbers,skipped_phone_numbers

def main():
    [dictionary_path, phone_directory_path] = getCliArguments()
    [listOfNumbersFromDirectory,alphaPhrasesFromDictionary]  = getInputData(phone_directory_path,dictionary_path)
    if(len(listOfNumbersFromDirectory) > 0 and len(alphaPhrasesFromDictionary) >0):
        [allPossiblePhrasesOfAllNumbers,skipped_phone_numbers] = getAlphaPhrasesForDirectoryNumbers(listOfNumbersFromDirectory,alphaPhrasesFromDictionary)#getting all the possible alpha phrases of all phone numbers of directory
        printOutputData(allPossiblePhrasesOfAllNumbers,skipped_phone_numbers)
if __name__ == "__main__":
    main() #calling main method