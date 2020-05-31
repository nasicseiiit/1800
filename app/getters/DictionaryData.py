#### written by nasicseiiit@gmail.com(Nasimunni Attaru) ###

'''
The method getDictionaryData used to read the dictionary file and store the values into a dictionary with key as a digit and the values are Alpha Phrases

If the file successfully opens the with the pointer reference the method will read the each line of the dictionary file and stroes the data into the dictionary
'''

def getDictionaryData(pointer_to_dictionary):
    alpha_phrases = {}
    for line in pointer_to_dictionary:  # reading each line
        line = line.strip()  # removing the leading and trailing spaces
        line = line.split('=')
        line[1] = line[1].split(',')
        alpha_phrases[line[0]] = line[1]
    pointer_to_dictionary.close()
    return alpha_phrases