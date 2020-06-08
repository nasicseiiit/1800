from app.getters.DictionaryData import getDictionaryData
from app.getters.PhoneNumbersData import getListOfNumbersInDirectory
from app.helper.GenericHelper import checkFileExistance

'''
The method getInputData will get the data from the input files and return the listOfNumbersFromDirectory and alphaPhrasesFromDictionary 
'''

def getInputData(phone_directory_path,dictionary_path):
    pointer_to_phone_directory = checkFileExistance(phone_directory_path)  # method to check whether the file exist or not
    pointer_to_dictionary = checkFileExistance(dictionary_path)  # method to check whether the file exist or not

    listOfNumbersFromDirectory = getInputDataOfPhoneDirectory(pointer_to_phone_directory)
    alphaPhrasesFromDictionary = getInputDataOfDictionary(pointer_to_dictionary)

    return listOfNumbersFromDirectory,alphaPhrasesFromDictionary

def getInputDataOfPhoneDirectory(pointer_to_phone_directory):
    if (pointer_to_phone_directory is not False):
        listOfNumbersFromDirectory = getListOfNumbersInDirectory(pointer_to_phone_directory)  # getting the phone numbers of directory into the list
        return listOfNumbersFromDirectory
    else:
        print("Error: phone directory file is not exist.")  # printing the message if the file does not exist
        return []

def getInputDataOfDictionary(pointer_to_dictionary):
    if (pointer_to_dictionary is not False):  # if file exist
        alphaPhrasesFromDictionary = getDictionaryData(pointer_to_dictionary)  # getting the alpha phrases of dictionary
        return alphaPhrasesFromDictionary

    else:
        print("Error: dictionary file does not exist.")  # printing the message if the file does not exist
        return []