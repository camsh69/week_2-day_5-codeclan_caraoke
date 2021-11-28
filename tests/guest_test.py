import unittest
from classes.guest import Guest
from classes.room import Room

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Joe Bloggs", 10, "I Will Survive")
        self.room = Room("Pop Classics", ["I Will Survive", "Sweet Caroline"], [], 3, 5)

    def test_customer_has_name(self):
        self.assertEqual("Joe Bloggs", self.guest.name)

    def test_customer_has_wallet(self):
        self.assertEqual(10, self.guest.wallet)

    def test_customer_wallet_can_be_reduced(self):
        self.guest.reduce_wallet(5)
        self.assertEqual(5, self.guest.wallet)

    def test_fav_song_on_list(self):
        self.assertEqual("Woohoo!", self.guest.fav_song_on_list(self.guest.fav_song, self.room))
    
    def test_fav_song_is_not_on_list(self):
        self.assertEqual("You don't have my favourite song", self.guest.fav_song_on_list("Bohemian Rhapsody", self.room))