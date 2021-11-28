import unittest
from classes.bar_tab import BarTab

class TestBarTab(unittest.TestCase):
    
    def setUp(self):
        self.bar_tab = BarTab("Joe Bloggs", 5)

    def test_bar_tab_has_guest_name(self):
        self.assertEqual("Joe Bloggs", self.bar_tab.guest)

    def test_bar_tab_has_amount(self):
        self.assertEqual(5, self.bar_tab.amount)

    def test_bar_tab_amount_can_be_increased(self):
        self.bar_tab.increase_bar_tab(5)
        self.assertEqual(10, self.bar_tab.amount)