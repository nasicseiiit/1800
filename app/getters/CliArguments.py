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