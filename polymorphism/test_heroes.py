import unittest
from unittest import TestCase
from parameterized import parameterized

from polymorphism.heroes import Leader

class LeaderTest(TestCase):

    def setUp(self):
         self.sut = Leader()

    @parameterized.expand([
        ["storm", "pust, pust"],
        #["cyclops", "piu pie"],
        #["flash", "run fast"],
        #["oops", "wait and bleed"],
    ])
    @unittest.skip("todo: implement code")
    def test_useForce_Storm(self, heroName, expected):
         hero = self.sut.selectHero(heroName)
         actual = hero.useForce()
         self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()