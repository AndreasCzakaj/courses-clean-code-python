import unittest
from unittest import TestCase
from parameterized import parameterized

from order_processing import OrderProcessor, ShoppingCart, Customer, Address, PaymentData, Order


class UuidGeneratorNaiveRandomImplTest(TestCase):

    def test(self): 
        orderProcessor = OrderProcessor()
        order = orderProcessor.processOrder(
            ShoppingCart(), Customer(), Address(), Address(), PaymentData() 
        )
        self.assertEqual(order.invoice.total, 123)


if __name__ == '__main__':
    unittest.main()
