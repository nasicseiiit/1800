
def getListOfNumbersInDirectory(pointer_to_phone_directory):
    list_of_numbers = []
    for line in pointer_to_phone_directory:  # reading each line
        line = line.strip()  # removing the leading and trailing spaces
        list_of_numbers.append(line)  # appending the numbers to the list_of_numbers
    pointer_to_phone_directory.close()
    return list_of_numbers
