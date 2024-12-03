import unittest
from unittest import TestCase
from parameterized import parameterized

from duck import RubberDuck


class Test(TestCase):

    def setUp(self):
         self.duck = RubberDuck()

    def test_init(self): 
        if isinstance(self.duck, RubberDuck):
            self.duck.insertBatteries()
        self.duck.swim()
        pass


if __name__ == '__main__':
    unittest.main()