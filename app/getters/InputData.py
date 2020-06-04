from app.getters.DictionaryData import getDictionaryData
from app.getters.PhoneNumbersData import getListOfNumbersInDirectory
from app.helper.GenericHelper import checkFileExistance

'''
The method getInputData will get the data from the input files and return the listOfNumbersFromDirectory and alphaPhrasesFromDictionary 
'''

def getInputData(phone_directory_path,dictionary_path):
    pointer_to_phone_directory = checkFileExistance(phone_directory_path)  # method to check whether the file exist or not
    pointer_to_dictionary = checkFileExistance(dictionary_path)  # method to check whether the file exist or not
    if (pointer_to_phone_directory is not False and pointer_to_dictionary is not False):  # if file exist
        listOfNumbersFromDirectory = getListOfNumbersInDirectory(pointer_to_phone_directory)  # getting the phone numbers of directory into the list
        alphaPhrasesFromDictionary = getDictionaryData(pointer_to_dictionary)  # getting the alpha phrases of dictionary
        return  listOfNumbersFromDirectory,alphaPhrasesFromDictionary
    else:
        print("Error: File does not exist.")  # printing the message if the file does not exist
        return [],[]