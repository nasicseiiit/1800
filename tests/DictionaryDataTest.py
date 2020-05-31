import unittest

from app.getters.DictionaryData import getDictionaryData
from app.helper.GenericHelper import checkFileExistance


class DictionaryDataTest(unittest.TestCase):
    def testGetDicitonaryData(self):
        pointer_to_dictionary_file = checkFileExistance("../data/dictionary")
        expectedDictionaryData = {'2': ['A', 'B', 'C'], '3': ['D', 'E', 'F'], '4': ['G', 'H', 'I'], '5': ['J', 'K', 'L'], '6': ['M', 'N', 'O'], '7': ['P', 'Q', 'R', 'S'], '8': ['T', 'U', 'V'], '9': ['W', 'X', 'Y', 'Z']}
        actualDictionaryData = getDictionaryData(pointer_to_dictionary_file)
        print(actualDictionaryData)
        self.assertEqual(expectedDictionaryData,actualDictionaryData)

if __name__ == '__main__':
    unittest.main()
