import unittest
from unittest import TestCase
from parameterized import parameterized

from UuidGeneratorNaiveRandomImpl import UuidGeneratorNaiveRandomImpl



class UuidGeneratorNaiveRandomImplTest(TestCase):

    @parameterized.expand([
        [UuidGeneratorNaiveRandomImpl(), "[a-f0-9]{32}", "lower case, no dashes"], 
    ])
    def test_shouldCreateAUuidInTheMatchingFormat(self, uuidGenerator, expectedRegex: str, info: str): 
        # when
        actual = uuidGenerator.create()
        # then
        self.assertRegexpMatches(actual, expectedRegex)


if __name__ == '__main__':
    unittest.main()