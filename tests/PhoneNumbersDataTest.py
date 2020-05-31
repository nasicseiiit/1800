
import unittest

from app.getters.PhoneNumbersData import getListOfNumbersInDirectory
from app.helper.GenericHelper import checkFileExistance


class PhoneNumbersDataTest(unittest.TestCase):
    '''
        test case to read the data from the phone directory
    '''
    def testGetPhoneNumbersData(self):
        pointer_to_directory_file = checkFileExistance("../data/phone-numbers-directory")
        expectedDirectoryData = ['95355', '345236016', '2347 7809', '234?6!784', '123400', '2255.63']
        actualDirectoryData = getListOfNumbersInDirectory(pointer_to_directory_file)
        print(actualDirectoryData)
        self.assertEqual(expectedDirectoryData,actualDirectoryData)


if __name__ == '__main__':
    unittest.main()
