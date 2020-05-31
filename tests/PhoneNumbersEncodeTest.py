import unittest

from app.getters.DictionaryData import getDictionaryData
from app.helper.GenericHelper import checkFileExistance
from app.values.PhoneNumbersEncode import getAlphaPhrasesForEachNumber


class PhoneNumbersEncode(unittest.TestCase):
    def testGetListOfPossiblePhrasesForNumberWithDot(self):
        number = "2.3"
        expectedList = ['A-D', 'A-E', 'A-F', 'B-D', 'B-E', 'B-F', 'C-D', 'C-E', 'C-F']
        pointer_to_file = checkFileExistance("../data/dictionary")
        alphaPhrasesFromDictionary = getDictionaryData(pointer_to_file)
        actualList= getAlphaPhrasesForEachNumber(number,alphaPhrasesFromDictionary)
        print(actualList)
        self.assertEqual(expectedList, actualList)

    def testGetListOfPossiblePhrasesForNumberWithHyphen(self):
        number = "2-3"
        expectedList = ['A-D', 'A-E', 'A-F', 'B-D', 'B-E', 'B-F', 'C-D', 'C-E', 'C-F']
        pointer_to_file = checkFileExistance("../data/dictionary")
        alphaPhrasesFromDictionary = getDictionaryData(pointer_to_file)
        actualList= getAlphaPhrasesForEachNumber(number,alphaPhrasesFromDictionary)
        print(actualList)
        self.assertEqual(expectedList, actualList)

    def testGetListOfPossiblePhrasesForNumberWithSpace(self):
        number = "2 3"
        expectedList = ['AD', 'AE', 'AF', 'BD', 'BE', 'BF', 'CD', 'CE', 'CF']
        pointer_to_file = checkFileExistance("../data/dictionary")
        alphaPhrasesFromDictionary = getDictionaryData(pointer_to_file)
        actualList= getAlphaPhrasesForEachNumber(number,alphaPhrasesFromDictionary)
        print(actualList)
        self.assertEqual(expectedList, actualList)

    def testGetListOfPossiblePhrasesForNumber(self):
        number = "23"
        expectedList = ['AD', 'AE', 'AF', 'BD', 'BE', 'BF', 'CD', 'CE', 'CF']
        pointer_to_file = checkFileExistance("../data/dictionary")
        alphaPhrasesFromDictionary = getDictionaryData(pointer_to_file)
        actualList= getAlphaPhrasesForEachNumber(number,alphaPhrasesFromDictionary)
        print(actualList)
        self.assertEqual(expectedList, actualList)

    def testGetListOfPossiblePhrasesForNumberWithPunctuations(self):
        number = "2!3?"
        expectedList = ['AD', 'AE', 'AF', 'BD', 'BE', 'BF', 'CD', 'CE', 'CF']
        pointer_to_file = checkFileExistance("../data/dictionary")
        alphaPhrasesFromDictionary = getDictionaryData(pointer_to_file)
        actualList= getAlphaPhrasesForEachNumber(number,alphaPhrasesFromDictionary)
        print(actualList)
        self.assertEqual(expectedList, actualList)

    def testCanHaveAlphaPhraseReplacementForNumber(self):
        number = "231"
        expectedList = ['AD1', 'AE1', 'AF1', 'BD1', 'BE1', 'BF1', 'CD1', 'CE1', 'CF1']
        pointer_to_file = checkFileExistance("../data/dictionary")
        alphaPhrasesFromDictionary = getDictionaryData(pointer_to_file)
        actualList = getAlphaPhrasesForEachNumber(number, alphaPhrasesFromDictionary)
        print(actualList)
        self.assertEqual(expectedList, actualList)

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
