import unittest

from app.getters.DictionaryData import getDictionaryData
from app.helper.GenericHelper import checkFileExistance
from app.values.AlphaPhrases import getPossiblePhraseforDigit


class AlphaPhraseTest(unittest.TestCase):
    def testGetSetOfPossiblePhrasesForDigit(self):
        number = "2"
        expectedList = ["A","B","C"]
        pointer_to_file = checkFileExistance("../data/dictionary")
        alphaPhrasesFromDictionary = getDictionaryData(pointer_to_file)
        actualList = getPossiblePhraseforDigit(number, alphaPhrasesFromDictionary)
        print(actualList)
        self.assertEqual(expectedList, actualList)

    def testCheckIfDigitDoesNotHaveReplacements(self):
        number = "!"
        expectedList = []
        pointer_to_file = checkFileExistance("../data/dictionary")
        alphaPhrasesFromDictionary = getDictionaryData(pointer_to_file)
        actualList = getPossiblePhraseforDigit(number, alphaPhrasesFromDictionary)
        print(actualList)
        self.assertEqual(expectedList, actualList)


if __name__ == '__main__':
    unittest.main()
