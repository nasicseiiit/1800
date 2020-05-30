import re

def checkFileExistance(phone_directory_path):
    try:
        pointer_to_file = open(phone_directory_path, "r")  # opening the file
        return pointer_to_file  # if file exist then returning the filePonter
    except IOError:  # catching the error
        return False  # if the file does not exist returning the False


def replaceDotWithHyphen(string):
    string=string.replace(".","-")
    return string

def removeEveryPunctuation(string):
    string =re.sub(r'[^a-zA-Z0-9\-]', '', string)
    return string

def convertListOfStringsToString(alpha_phrases):
    allPossiblePhrases = []
    for phrases in alpha_phrases :
        string = ""
        for phrase in phrases:
            string = string+phrase
        allPossiblePhrases.append(string.upper())
    return  allPossiblePhrases