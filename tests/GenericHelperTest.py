import unittest

from app.helper.GenericHelper import checkFileExistance, convertListOfStringsToCapitalString, replaceDotWithHyphen, \
    removeEveryPunctuation


class GenericHelperTest(unittest.TestCase):
    '''
    test case to check whether the file exist or not
    '''
    def testCheckFileExistance(self):
        pointer_to_file = checkFileExistance("../data/dictionary")
        self.assertNotEqual(pointer_to_file, False)
        pointer_to_file.close()

    '''
    test case whether are we able to convert the list of strings to a string and make it into capital or not
    '''
    def testConvertListOfStringsToCapitalString(self):
        inputList = [("a","b")]
        expectedString = ["AB"]
        actualString = convertListOfStringsToCapitalString(inputList)
        print(actualString)
        self.assertEqual(expectedString, actualString)

    '''
    test case whether we are able to convert the all dots of string into the Hyphen
    '''
    def testReplaceDotWithHyphen(self):
        inputString = "ab.c"
        expectedString = "ab-c"
        actualString = replaceDotWithHyphen(inputString)
        print(actualString)
        self.assertEqual(expectedString, actualString)

    '''
    test case whether we are able to remove all punctuations or not
    '''
    def testRemoveEveryPunctuation(self):
        inputString = "a b?c!"
        expectedString = "abc"
        actualString = removeEveryPunctuation(inputString)
        print(actualString)
        self.assertEqual(expectedString, actualString)


if __name__ == '__main__':
    unittest.main()