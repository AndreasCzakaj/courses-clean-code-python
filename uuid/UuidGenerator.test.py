import unittest
from unittest import TestCase
from parameterized import parameterized

from UuidGeneratorNaiveRandomImpl import UuidGeneratorNaiveRandomImpl
from UuidGeneratorUpperCaseDecorator import UuidGeneratorUpperCaseDecorator



class UuidGeneratorNaiveRandomImplTest(TestCase):

    @parameterized.expand([
        [UuidGeneratorNaiveRandomImpl(), "[a-f0-9]{32}", "lower case, no dashes"], 
        #[???, "[A-F0-9]{32}", "upper case, no dashes"],
        #[???, "[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}", "lower case, with dashes"], 
        #[???, "[A-F0-9]{8}-[A-F0-9]{4}-[A-F0-9]{4}-[A-F0-9]{4}-[A-F0-9]{12}", "upper case, with dashes"], 
    ])
    def test_shouldCreateAUuidInTheMatchingFormat(self, uuidGenerator, expectedRegex: str, info: str): 
        # when
        actual = uuidGenerator.create()
        # then
        self.assertRegex(actual, expectedRegex)


if __name__ == '__main__':
    unittest.main()