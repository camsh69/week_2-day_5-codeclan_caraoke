import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Joe Bloggs", 10)

    def test_customer_has_name(self):
        self.assertEqual("Joe Bloggs", self.guest.name)

    def test_customer_has_wallet(self):
        self.assertEqual(10, self.guest.wallet)