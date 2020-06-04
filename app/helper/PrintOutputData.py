
'''
The method printOutputData will call the methods to print the encoded phone numbers and the skipped phone numbers
'''

def printOutputData(allPossiblePhrasesOfAllNumbers,skipped_phone_numbers,):
    print("\n#####################################################################")
    print("Encoded the all phone numbers of phone directory")
    print("#####################################################################")
    printEncodedNumber(allPossiblePhrasesOfAllNumbers)
    printSkippedNumbers(skipped_phone_numbers)

'''
The method printEncodedNumber will print the successfully encoded phone numbers
'''

def printEncodedNumber(allPossiblePhrasesOfAllNumbers):
    for phone_number in allPossiblePhrasesOfAllNumbers:
        if(len(allPossiblePhrasesOfAllNumbers[phone_number])>0):
            print("\n----------------------------------------------------------------")
            print("Possible Alpha Phrases of" , phone_number)
            print("----------------------------------------------------------------")
            print(allPossiblePhrasesOfAllNumbers[phone_number],"\n")
'''
The method printSkippedNumbers will print the skipped phone numbers 
'''

def printSkippedNumbers(skipped_phone_numbers):
    if (len(skipped_phone_numbers) > 0):  # if is there any skipped phone numbers
        print("#####################################################################")
        print("Skipped phone numbers due to having more than one consecutive unchanged digits ")
        print("----------------------------------------------------------------------")
        for missedNumber in skipped_phone_numbers:
            print(missedNumber)  # printing the skipped phone numbers