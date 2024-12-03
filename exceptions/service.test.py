import unittest
from unittest import TestCase
from parameterized import parameterized

from exceptions.service import MyClient


class MyServiceTest(TestCase):

    def setUp(self):
         self.sut = MyClient()

    def test_consumeStuff1(self): 
         self.assertEqual(self.sut.consumeStuff(1), 1)

    def test_consumeStuff2(self): 
         self.assertEqual(self.sut.consumeStuff(2), 2)

    def test_consumeStuff3(self): 
         with self.assertRaisesRegex(SyntaxError, "3"):
              self.sut.consumeStuff(3)


if __name__ == '__main__':
    unittest.main()