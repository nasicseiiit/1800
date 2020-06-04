#### written by nasicseiiit@gmail.com(Nasimunni Attaru) ###

from app.getters.CliArguments import getCliArguments
from app.getters.DictionaryData import getDictionaryData
from app.getters.InputData import getInputData
from app.helper.GenericHelper import checkFileExistance, replaceDotWithHyphen, removeEveryPunctuation, convertListOfStringsToCapitalString
from app.getters.PhoneNumbersData import getListOfNumbersInDirectory
from app.helper.PrintOutputData import printOutputData
from app.values.AlphaPhrases import getPossiblePhraseforDigit, generateAllPossiblePhrases, \
    isHaveReplacementsFlagForNumber, firstUnchangedDigit

'''
The method getAlphaPhrasesForEachNumber will get the all possible Alpha phrases of a phone number  
'''
def getAlphaPhrasesForEachNumber(phone_number,alphaPhrasesFromDictionary):
    phone_number = replaceDotWithHyphen(phone_number) #replacing all the dots in the phone number with the Hyphen
    phone_number = removeEveryPunctuation(phone_number) #removing all the punctuations in the phone number
    [allPossiblePhrases,listOfPhrases,prevIndex] = firstUnchangedDigit(phone_number,alphaPhrasesFromDictionary)
    for digit_index in range(1,len(phone_number)):
        [allPossiblePhrases,listOfPhrases,prevIndex] = isHaveReplacementsFlagForNumber(allPossiblePhrases,phone_number, alphaPhrasesFromDictionary, prevIndex, digit_index)
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
    [dictionary_path, phone_directory_path] = getCliArguments() #getting the input files
    [listOfNumbersFromDirectory,alphaPhrasesFromDictionary]  = getInputData(phone_directory_path,dictionary_path)#extracting the data from the files
    if(len(listOfNumbersFromDirectory) > 0 and len(alphaPhrasesFromDictionary) >0):
        [allPossiblePhrasesOfAllNumbers,skipped_phone_numbers] = getAlphaPhrasesForDirectoryNumbers(listOfNumbersFromDirectory,alphaPhrasesFromDictionary)#getting all the possible alpha phrases of all phone numbers of directory
        printOutputData(allPossiblePhrasesOfAllNumbers,skipped_phone_numbers) #printing the output
if __name__ == "__main__":
    main() #calling main method