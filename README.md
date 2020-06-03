Many companies like to list their phone numbers using the letters printed on most
telephones. This makes the number easier to remember for customers. An example may
be 1-800-FLOWERS

This coding challenge is to write a program that will show a user possible matches for a list
of provided phone numbers.

Your program should be a command line application that reads from files specified as
command-line arguments or STDIN when no files are given. Each line of these files will
contain a single phone number.

For each phone number read, your program should output all possible word replacements
from a dictionary. Your program should try to replace every digit of the provided phone
number with a letter from a dictionary word; however, if no match can be made, a single
digit can be left as is at that point. No two consecutive digits can remain unchanged and
the program should skip over a number (producing no output) if a match cannot be made.
Your program should allow the user to set a dictionary with the -d command-line option,
but it's fine to use a reasonable default for your system. The dictionary is expected to have
one word per line.

All punctuation and whitespace should be ignored in both phone numbers and the
dictionary file. The program should not be case sensitive, letting "a" == "A". Output should
be capital letters and digits separated at word boundaries with a single dash (-), one
possible word encoding per line. For example, if your program is fed the number:

2255.63

One possible line of output is

CALL-ME

According to my dictionary.

The number encoding on the phone the program will use is:

DIGIT CHARACTERS
2 A B C
3 D E F
4 G H I
5 J K L
6 M N O
7 P Q R S
8 T U V
9 W X Y Z

####################
Steps to Run the source code
####################
PhoneNumbersEncode.py is the main file with the source code
Please add the command line arguments for the phone directory and dictionary files as shown below
    -> Passing zero command line arguments
        ... The program will prompt for the phone directory path
        ... The dictionary file will be set by the system default
         
    -> passing single command line argument 
        ... The argument will be the phone directory file input
        ... The dictionary file will be set by the system default
        
    -> passing three command line arguments with second argument as "-d"
        ... The first argument will be the phone directory file input
        ... The third argument will be the  dictionary file input
        eg : phone_numbers_data -d dictionary
   
please click on PhoneNumbersEncode.py and click on run button if passed the command line arguments then it will take the action according to that
If no command line arguments passed then it will prompt for the phone directory path and the dictionary will be set by default

If the phone number from directory is have replacement then it will provide the output if not it will skip that number according to the dictionary alpha 
phrases and according to the above problem statement

Running test cases
###################
AlphaPhraseTest.py -> this file consist of 2 test cases
DictionaryDataTest.py -> this file consist of 1 test case
GenericHelperTest.py -> this file consist of 4 test cases
PhoneNumbersDataTest.py -> this file consist of 1 test case
PhoneNumbersEncodeTest.py -> this file consist of 8 test cases and the negative test case will fail
#############################################

#There are 4 supporting files mentioned below

    CliArguments.py
    DictionaryData.py
    PhoneNumbersData.py
    GenericHelper.py
    