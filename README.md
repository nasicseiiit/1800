#1800 CODING CHALLENGE


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

#Requirements

Please install python 3 and above

#Installation

First, clone 1800_CODE_CHALLENGE using git

_`https://github.com/nasicseiiit/1800`_


# To build the project

Then, cd to the 1800_CODE_CHALLENGE folder 

 cd 1800_CODE_CHALLENGE/
 
 sudo python setup.py install 
 
#To run the project
 
 cd 1800_CODE_CHALLENGE
 
 cd to the values folder in app
 
 cd app/values
 
 then execute below command
 
 python PhoneNumbersEncode.py

#Input Format

provide the input format using CLI or STDIN
for phone directory file you can provide the input file by STDIN or Command line

`-> Passing zero command line arguments
    ... The program will prompt for the phone directory path
    ... The dictionary file will be set by the system default`
     
`-> passing single command line argument 
    ... The argument will be the phone directory file input
    ... The dictionary file will be set by the system default
    eg : phone_numbers_data`
    
`-> passing three command line arguments with second argument as "-d"
    ... The first argument will be the phone directory file input
    ... The third argument will be the  dictionary file input
    eg : phone_numbers_data -d dictionary`

`getAlphaPhrasesForDirectoryNumbers(231) #returns  ['AD1', 'AE1', 'AF1', 'BD1', 'BE1', 'BF1', 'CD1', 'CE1', 'CF1']` 

`getAlphaPhrasesForDirectoryNumbers(2301) #returns []`
 
`getAlphaPhrasesForDirectoryNumbers(2) #returns ['A','B','C']` 

#Contributing

As I am a beginner and writing the projects in GitHub. 
If you have any ideas or improvements, just open an issue by clicking on below link and tell me what you think.

https://github.com/nasicseiiit/1800/issues/new

If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are warmly welcome.

#Licensing

This project is licensed under Unlicense license. This license does not require you to take the license with you to your project. 
