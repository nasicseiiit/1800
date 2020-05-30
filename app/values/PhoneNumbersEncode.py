
from app.getters.CliArguments import getCliArguments
from app.getters.DictionaryData import getDictionaryData
from app.helper.GenericHelper import checkFileExistance, replaceDotWithHyphen, removeEveryPunctuation, convertListOfStringsToString
from app.getters.PhoneNumbersData import getListOfNumbersInDirectory
from app.values.AlphaPhrases import getPossiblePhraseforDigit, generateAllPossiblePhrases


def getAlphaPhrasesForEachNumber(phone_number,alphaPhrasesFromDictionary):
    phone_number = replaceDotWithHyphen(phone_number)
    phone_number = removeEveryPunctuation(phone_number)
    digit = phone_number[0]
    listOfPhrases = getPossiblePhraseforDigit(digit,alphaPhrasesFromDictionary)
    prevIndex = -2
    if(len(listOfPhrases)==0):
        listOfPhrases = [digit]
        prevIndex = 0
    allPossiblePhrases = listOfPhrases
    for digit_index in range(1,len(phone_number)):
        digit = phone_number[digit_index]
        listOfPhrases = getPossiblePhraseforDigit(digit,alphaPhrasesFromDictionary)
        if (len(listOfPhrases) == 0):
            if(digit_index-prevIndex == 1):
                allPossiblePhrases=[]
                break
            else:
                prevIndex = digit_index
                listOfPhrases = [digit]
        alpha_phrases = generateAllPossiblePhrases(allPossiblePhrases,listOfPhrases)
        allPossiblePhrases = convertListOfStringsToString(alpha_phrases)
    return allPossiblePhrases


def getAlphaPhrasesForDirectoryNumbers():
    [dictionary_path,phone_directory_path] = getCliArguments()
    pointer_to_phone_directory = checkFileExistance(phone_directory_path)  # method to check whether the file exist or not
    if (pointer_to_phone_directory is not False):  # if file exist
        listOfNumbersFromDirectory = getListOfNumbersInDirectory(pointer_to_phone_directory)
        pointer_to_dictionary = checkFileExistance(dictionary_path)  # method to check whether the file exist or not
        alphaPhrasesFromDictionary = getDictionaryData(pointer_to_dictionary)
        missed_phone_numbers = []
        print("\n#####################################################################")
        print("Encoded the all phone numbers of phone directory")
        print("#####################################################################")
        for phone_number in listOfNumbersFromDirectory :
            allPossiblePhrases = getAlphaPhrasesForEachNumber(phone_number,alphaPhrasesFromDictionary)
            if(len(allPossiblePhrases)>0):
                print("\n----------------------------------------------------------------")
                print("Possible Alpha Phrases of" , phone_number)
                print("----------------------------------------------------------------")
                print(allPossiblePhrases,"\n")
            else:
                missed_phone_numbers.append(phone_number)
        print("#####################################################################")
        print("Skipped phone numbers due to having more than one consecutive unchanged digits\n")
        for missedNumber in missed_phone_numbers:
            print(missedNumber)
    else:
        print("Error: File does not exist.")  # printing the message if the file does not exist

def main():
    getAlphaPhrasesForDirectoryNumbers()

if __name__ == "__main__":
    main() #calling main method

