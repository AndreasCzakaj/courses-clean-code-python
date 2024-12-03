import unittest
from unittest import TestCase
from parameterized import parameterized

from currying import print_address_line1, translation_provider, Employee, create_address_line_printer

class UuidGeneratorNaiveRandomImplTest(TestCase):

    def setUp(self):
        self.sut = None
        self.collector = []

    def print_consumer(self, value: str):
        self.collector.append(value)
    
    def test_long(self): 
        employee = Employee("John Doe", "developer")
        print_address_line1(employee, translation_provider, "en", self.print_consumer)
        self.assertEqual(self.collector, ["John Doe - Developer"])
    
    def test_currying(self): 
        english_address_printer = create_address_line_printer(translation_provider, "en", self.print_consumer)
        employee = Employee("John Doe", "developer")

        english_address_printer(employee)
        self.assertEqual(self.collector, ["John Doe - Developer"])


if __name__ == '__main__':
    unittest.main()