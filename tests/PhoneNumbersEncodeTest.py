import unittest

from app.getters.DictionaryData import getDictionaryData
from app.helper.GenericHelper import checkFileExistance
from app.values.PhoneNumbersEncode import getAlphaPhrasesForEachNumber


class PhoneNumbersEncode(unittest.TestCase):
    '''
    test case whether we are able to get list of possible phrases for number with dot or not
    '''
    def testGetListOfPossiblePhrasesForNumberWithDot(self):
        number = "2.3"
        expectedList = ['A-D', 'A-E', 'A-F', 'B-D', 'B-E', 'B-F', 'C-D', 'C-E', 'C-F']
        pointer_to_file = checkFileExistance("../data/dictionary")
        alphaPhrasesFromDictionary = getDictionaryData(pointer_to_file)
        actualList= getAlphaPhrasesForEachNumber(number,alphaPhrasesFromDictionary)
        print(actualList)
        self.assertEqual(expectedList, actualList)

    '''
        test case whether we are able to get list of possible phrases for number with Hyphen or not
    '''
    def testGetListOfPossiblePhrasesForNumberWithHyphen(self):
        number = "2-3"
        expectedList = ['A-D', 'A-E', 'A-F', 'B-D', 'B-E', 'B-F', 'C-D', 'C-E', 'C-F']
        pointer_to_file = checkFileExistance("../data/dictionary")
        alphaPhrasesFromDictionary = getDictionaryData(pointer_to_file)
        actualList= getAlphaPhrasesForEachNumber(number,alphaPhrasesFromDictionary)
        print(actualList)
        self.assertEqual(expectedList, actualList)

    '''
        test case whether we are able to get list of possible phrases for number with space or not
    '''
    def testGetListOfPossiblePhrasesForNumberWithSpace(self):
        number = "2 3"
        expectedList = ['AD', 'AE', 'AF', 'BD', 'BE', 'BF', 'CD', 'CE', 'CF']
        pointer_to_file = checkFileExistance("../data/dictionary")
        alphaPhrasesFromDictionary = getDictionaryData(pointer_to_file)
        actualList= getAlphaPhrasesForEachNumber(number,alphaPhrasesFromDictionary)
        print(actualList)
        self.assertEqual(expectedList, actualList)

    '''
        test case whether we are able to get list of possible phrases for number 
    '''
    def testGetListOfPossiblePhrasesForNumber(self):
        number = "23"
        expectedList = ['AD', 'AE', 'AF', 'BD', 'BE', 'BF', 'CD', 'CE', 'CF']
        pointer_to_file = checkFileExistance("../data/dictionary")
        alphaPhrasesFromDictionary = getDictionaryData(pointer_to_file)
        actualList= getAlphaPhrasesForEachNumber(number,alphaPhrasesFromDictionary)
        print(actualList)
        self.assertEqual(expectedList, actualList)

    '''
        test case whether we are able to get list of possible phrases for number with punctuations or not
    '''
    def testGetListOfPossiblePhrasesForNumberWithPunctuations(self):
        number = "2!3?"
        expectedList = ['AD', 'AE', 'AF', 'BD', 'BE', 'BF', 'CD', 'CE', 'CF']
        pointer_to_file = checkFileExistance("../data/dictionary")
        alphaPhrasesFromDictionary = getDictionaryData(pointer_to_file)
        actualList= getAlphaPhrasesForEachNumber(number,alphaPhrasesFromDictionary)
        print(actualList)
        self.assertEqual(expectedList, actualList)

    '''
        test case whether we are able to get list of possible phrases for number with single unchanged digit or not
    '''
    def testCanHaveAlphaPhraseReplacementForNumber(self):
        number = "231"
        expectedList = ['AD1', 'AE1', 'AF1', 'BD1', 'BE1', 'BF1', 'CD1', 'CE1', 'CF1']
        pointer_to_file = checkFileExistance("../data/dictionary")
        alphaPhrasesFromDictionary = getDictionaryData(pointer_to_file)
        actualList = getAlphaPhrasesForEachNumber(number, alphaPhrasesFromDictionary)
        print(actualList)
        self.assertEqual(expectedList, actualList)

    '''
        test case whether we are able to skip the number with two consecutive unchanged digits or not
        This is negative test case and will fail
    '''
    def testCanHaveAlphaPhraseReplacementForNumberNegative(self):
        number = "2301"
        expectedList = ['AD01', 'AE01', 'AF01', 'BD01', 'BE01', 'BF01', 'CD01', 'CE01', 'CF01']
        pointer_to_file = checkFileExistance("../data/dictionary")
        alphaPhrasesFromDictionary = getDictionaryData(pointer_to_file)
        actualList = getAlphaPhrasesForEachNumber(number, alphaPhrasesFromDictionary)
        print(actualList)
        self.assertEqual(expectedList, actualList,msg="Negative test case which will fail")

    '''
        test case whether we are able to skip the number with two consecutive unchanged digits or not 
    '''
    def testNotHaveAlphaPhraseReplacementForNumberDueToTwoConsecutiveUnchangedDigits(self):
        number = "2310"
        expectedList = []
        pointer_to_file = checkFileExistance("../data/dictionary")
        alphaPhrasesFromDictionary = getDictionaryData(pointer_to_file)
        actualList = getAlphaPhrasesForEachNumber(number, alphaPhrasesFromDictionary)
        print(actualList)
        self.assertEqual(expectedList, actualList)


if __name__ == '__main__':
    unittest.main()
