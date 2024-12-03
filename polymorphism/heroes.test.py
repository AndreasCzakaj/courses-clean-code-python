import unittest
from unittest import TestCase
from parameterized import parameterized

from heroes import Leader

class LeaderTest(TestCase):

    def setUp(self):
         self.sut = Leader()

    @parameterized.expand([
        ["storm", "pust, pust"],
        #["cyclops", "piu pie"],
        #["flash", "run fast"],
        #["oops", "wait and bleed"],
    ])
    def test_selectHero_Storm(self, heroName, expected):
         actual = self.sut.selectHero(heroName)
         self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()