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


from naming import Person

class PersonTest(TestCase):

    def setUp(self):
        self.person = Person()

    def test_init(self):
        self.assertEqual(self.person.firstName, "Joey")
        self.assertEqual(self.person.lastName, "Ramone")
        self.assertEqual(self.person.personState, "unalive")
        self.assertEqual(self.person.addrStreetAndNo, "1-2-3-4 Fake Street")
        self.assertEqual(self.person.addrZipAndCity, "12345 New York City")
        self.assertEqual(self.person.addrState, "NY")



if __name__ == '__main__':
    unittest.main()