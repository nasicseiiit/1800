#### written by nasicseiiit@gmail.com(Nasimunni Attaru) ###

'''
The method getListOfNumbersInDirectory used to read the directory file and store the values into a list

If the file successfully opens the with the pointer reference the method will read the each line of the directory file and stroes the data into the list
'''

def getListOfNumbersInDirectory(pointer_to_phone_directory):
    list_of_numbers = []
    for line in pointer_to_phone_directory:  # reading each line
        line = line.strip()  # removing the leading and trailing spaces
        list_of_numbers.append(line)  # appending the numbers to the list_of_numbers
    pointer_to_phone_directory.close()
    return list_of_numbers
