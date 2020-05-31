#### written by nasicseiiit@gmail.com(Nasimunni Attaru) ###

import re

'''
The method checkFileExistance will check whether the file exist or not and able to open the file
If the file exist and able to open the file then it will return the file pointer
'''

def checkFileExistance(phone_directory_path):
    try:
        pointer_to_file = open(phone_directory_path, "r")  # opening the file
        return pointer_to_file  # if file exist then returning the filePonter
    except IOError:  # catching the error
        return False  # if the file does not exist returning the False

'''
The method replaceDotWithHyphen method replace the all places of dots with an hyphen and returns that modified string
'''

def replaceDotWithHyphen(string):
    string=string.replace(".","-")
    return string

'''
The method removeEveryPunctuation removes all the punctuations and spaces except dot and returns that modified string
'''

def removeEveryPunctuation(string):
    string =re.sub(r'[^a-zA-Z0-9\-]', '', string)
    return string

'''
The method convertListOfStringsToCapitalString will convert the list of strings to a single string and convert it into upper case 
and it will return that modified string
'''

def convertListOfStringsToCapitalString(alpha_phrases):
    allPossiblePhrases = []
    for phrases in alpha_phrases:
        string = ""
        for phrase in phrases:
            string = string+phrase
        allPossiblePhrases.append(string.upper())
    return allPossiblePhrases