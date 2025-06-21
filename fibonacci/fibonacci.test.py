import unittest
from unittest import TestCase
from parameterized import parameterized

from fibonacci import Fibonacci



class FibonacciTest(TestCase):

    def setUp(self):
        self.fibonacci = Fibonacci()

    def test_index_0_should_yield_0(self):
        self.assertEqual(self.fibonacci.calc(0), 0)


if __name__ == '__main__':
    unittest.main()