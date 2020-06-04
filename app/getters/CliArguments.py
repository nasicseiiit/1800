#### written by nasicseiiit@gmail.com(Nasimunni Attaru) ###
'''
The method getCliArguments used to take the command line arguments from the user with the below constraints

0 -> If the user passes no arguments then the user needs to input the phone directory file from STDIN and system sets the default dictionary file
1 -> The user can pass input file for the phone directory and with -d user can set the dictionary through command line
2 -> If the user passes only one argument and if then the phone directory will be the argument value
     and the system uses the default dictionary
3 -> If the user passes three argumnets then the first will be the input file for the phone directory and the third is the dictionary file
'''

import sys
import os

def getCliArguments():
    current_directory =  os.getcwd()
    data_directory = (os.path.abspath(os.path.join(current_directory, os.pardir)))
    data_directory = (os.path.abspath(os.path.join(data_directory, os.pardir)))
    dictionary_path = data_directory + "/data/dictionary"
    if len(sys.argv)==2:
            phone_directory_path = sys.argv[1]
    elif len(sys.argv)==4:
        phone_directory_path = sys.argv[1]
        dictionary_path = sys.argv[3]
    else:
        phone_directory_path = input("Please enter the phone numbers directory path : ")
    return  dictionary_path,phone_directory_path