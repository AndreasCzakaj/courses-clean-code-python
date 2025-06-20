import unittest
from unittest import TestCase

from naming import DtaRcrd10

class DtaRcrd10Test(TestCase):

    def setUp(self):
        self.dtaRcrd10 = DtaRcrd10()

    def test_init(self):
        self.assertEqual(self.dtaRcrd10.genymdhms, "Black then white")
        self.assertEqual(self.dtaRcrd10.pszquint, "are all I see in my infancy")
        self.assertEqual(self.dtaRcrd10.serverProt, "Red and yellow then came to be, reaching out to me")



if __name__ == '__main__':
    unittest.main()