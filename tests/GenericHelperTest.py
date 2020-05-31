import unittest

from app.helper.GenericHelper import checkFileExistance, convertListOfStringsToCapitalString, replaceDotWithHyphen, \
    removeEveryPunctuation


class GenericHelperTest(unittest.TestCase):

    def testCheckFileExistance(self):
        pointer_to_file = checkFileExistance("../data/dictionary")
        self.assertNotEqual(pointer_to_file, False)
        pointer_to_file.close()

    def testConvertListOfStringsToCapitalString(self):
        inputList = [("a","b")]
        expectedString = ["AB"]
        actualString = convertListOfStringsToCapitalString(inputList)
        print(actualString)
        self.assertEqual(expectedString, actualString)

    def testreplaceDotWithHyphen(self):
        inputString = "ab.c"
        expectedString = "ab-c"
        actualString = replaceDotWithHyphen(inputString)
        print(actualString)
        self.assertEqual(expectedString, actualString)

    def testremoveEveryPunctuation(self):
        inputString = "a b?c!"
        expectedString = "abc"
        actualString = removeEveryPunctuation(inputString)
        print(actualString)
        self.assertEqual(expectedString, actualString)


if __name__ == '__main__':
    unittest.main()