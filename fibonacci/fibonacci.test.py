import unittest
from unittest import TestCase
from parameterized import parameterized

from fibonacci import Fibonacci



class FibonacciTest(TestCase):

    def setUp(self):
        self.fibonacci = Fibonacci()

    def test_0_should_yield_0(self):
        pass


if __name__ == '__main__':
    unittest.main()