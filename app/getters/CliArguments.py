#### written by nasicseiiit@gmail.com(Nasimunni Attaru) ###
'''
The method getCliArguments used to take the command line arguments from the user with the below constraints

0 -> If the user passes no arguments then the user needs to input the phone directory file from STDIN and system sets the default dictionary file
1 -> The user can pass input file for the phone directory and with -d user can set the dictionary through command line
2 -> If the user passes only one argument and if it is -d then the user need to provide the phone directory and dictionary files from STDIN
3 -> If the user passes only one argument and if it is not -d then the phone directory will be the argument value
     and the system uses the default dictionary
4 -> If the user passes two arguments and if the first argument is -d then the second argument will be the dictionary and the user needs to provide the
     phone directory file from the STDIN
5 -> If the user passes two arguments and if the second argument is -d then the first argument will be the phone directory and the user needs to provide the
     dictionary file from the STDIN
6 -> If the user passes three arguments and if the first argument is the -d then the second argument is the dictionary file and the third argument will be the
     phone directory
7 -> If the user passes three arguments and if the second argument is the -d then the third argument is the dictionary file and the first argument will be the
     phone directory
'''

import sys
import os

def getCliArguments():
    current_directory =  os.getcwd()
    data_directory = (os.path.abspath(os.path.join(current_directory, os.pardir)))
    dictionary_path = data_directory + "/data/dictionary"
    if len(sys.argv) == 1:
        phone_directory_path = input("Please enter the phone numbers directory path : ")
    elif len(sys.argv)==2:
        if ("-d" == sys.argv[1] ):
            phone_directory_path = input("Please enter the phone numbers directory path : ")
            dictionary_path = input("Please enter dictionary path : ")
        else:
            phone_directory_path = sys.argv[1]
    elif len(sys.argv)==3:
        if ("-d" == sys.argv[1] ):
            phone_directory_path = input("Please enter the phone numbers directory path : ")
            dictionary_path = sys.argv[2]
        else:
            phone_directory_path = sys.argv[1]
            if ("-d" == sys.argv[2]):
                dictionary_path = input("Please enter dictionary path : ")
    elif len(sys.argv)==4:
        if ("-d" == sys.argv[1] ):
            phone_directory_path = sys.argv[3]
            dictionary_path = sys.argv[2]
        else:
            phone_directory_path = sys.argv[1]
            if ("-d" == sys.argv[2]):
                dictionary_path = sys.argv[3]
    else:
        phone_directory_path = sys.argv[1]
    return  dictionary_path,phone_directory_path