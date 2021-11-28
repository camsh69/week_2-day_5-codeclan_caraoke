import unittest
from classes.bar_tab import BarTab
from classes.guest import Guest

class TestBarTab(unittest.TestCase):
    
    def setUp(self):
        self.guest = Guest("Joe Bloggs", 10, "I Will Survive")
        self.bar_tab = BarTab(self.guest.name, 5)

    def test_bar_tab_has_guest_name(self):
        self.assertEqual("Joe Bloggs", self.bar_tab.guest)
