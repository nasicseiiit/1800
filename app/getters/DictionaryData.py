
def getDictionaryData(pointer_to_dictionary):
    alpha_phrases = {}
    for line in pointer_to_dictionary:  # reading each line
        line = line.strip()  # removing the leading and trailing spaces
        line = line.split('=')
        line[1] = line[1].split(',')
        alpha_phrases[line[0]] = line[1]
    return alpha_phrases