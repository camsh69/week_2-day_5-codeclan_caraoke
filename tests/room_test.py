import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.song_1 = Song("I will survive")
        self.song_2 = Song("Sweet Caroline")
        self.song_3 = Song("Yesterday")
        self.song_list = [self.song_1, self.song_2]
        self.guest_1 = Guest("Joe Bloggs")
        self.guest_2 = Guest("Jane Doe")
        self.guest_list = [self.guest_1, self.guest_2]
        self.room = Room("Golden Oldie Room", self.song_list, self.guest_list)

    def test_room_has_name(self):
        self.assertEqual("Golden Oldie Room", self.room.name)

    def test_for_song_in_song_list(self):
        self.assertEqual(True, self.room.find_song(self.song_1))

    def test_for_song_is_not_in_list(self):
        self.assertEqual(False, self.room.find_song(self.song_3))

    def test_number_of_guests_in_room(self):
        self.assertEqual(2, self.room.guest_count())

    
        