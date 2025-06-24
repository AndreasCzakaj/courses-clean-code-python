import unittest
from unittest import TestCase
from parameterized import parameterized

from exceptions.service import MyClient, MyCustomError


class MyServiceTest(TestCase):

    def setUp(self):
         self.sut = MyClient()

    def test_consumeStuff1(self):
      with self.assertRaisesRegex(ValueError, "1"):
        self.assertEqual(self.sut.consumeStuff(1), 1)

    def test_consumeStuff2(self):
        with self.assertRaisesRegex(MyCustomError, "2"):
            self.assertEqual(self.sut.consumeStuff(2), 42)

    def test_consumeStuff3(self):
         self.assertEqual(self.sut.consumeStuff(3), 666)


if __name__ == '__main__':
    unittest.main()