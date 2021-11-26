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
        self.guest_1 = Guest("Harry Tonedeaf", 25)
        self.guest_2 = Guest("Sheila Diva", 15)
        self.guest_3 = Guest("Larry Crooner", 35)
        self.guest_4 = Guest("Tina Tuneless", 45)
        self.guest_list = [self.guest_1, self.guest_2]
        self.room = Room("Golden Oldies", self.song_list, self.guest_list, 3, 5)
        self.room_2 = Room("Pop Classics", [], [], 3, 5)

    def test_room_has_name(self):
        self.assertEqual("Golden Oldies", self.room.name)

    def test_for_song_in_song_list__True(self):
        self.assertEqual(True, self.room.find_song(self.song_1))

    def test_for_song_in_song_list__False(self):
        self.assertEqual(False, self.room.find_song(self.song_3))

    def test_add_song_to_room(self):
        self.room.add_song_to_room(self.song_3)
        self.assertEqual(True, self.room.find_song(self.song_3))

    def test_number_of_guests_in_room(self):
        self.assertEqual(2, self.room.guest_count()) 

    def test_check_in_guest(self):
        self.room.check_in_guest(self.guest_3)
        self.assertEqual(3, self.room.guest_count())

    def test_check_out_guest(self):
        self.room.check_out_guest(self.guest_1)
        self.assertEqual(1, self.room.guest_count())

    def test_can_increase_till(self):
        self.room.increase_till(self.room.price)
        self.assertEqual(5, self.room.till)

    def test_check_in_multiple_guests_within_room_capacity__True(self):
        self.room_2.check_in_guest(self.guest_1)
        self.room_2.check_in_guest(self.guest_2)
        self.room_2.check_in_guest(self.guest_3)
        self.assertEqual(3, self.room_2.guest_count())
        self.assertEqual(15, self.room_2.till)
        self.assertEqual(20, self.guest_1.wallet)
        self.assertEqual(10, self.guest_2.wallet)
        self.assertEqual(30, self.guest_3.wallet)

    def test_check_in_multiple_guests_within_room_capacity__False(self):
        self.room_2.check_in_guest(self.guest_1)
        self.room_2.check_in_guest(self.guest_2)
        self.room_2.check_in_guest(self.guest_3)
        self.assertEqual("Sorry, the maximum number of guests is 3", self.room_2.check_in_guest(self.guest_4))
        self.assertEqual(3, self.room_2.guest_count())
        self.assertEqual(15, self.room_2.till)
        self.assertEqual(20, self.guest_1.wallet)
        self.assertEqual(10, self.guest_2.wallet)
        self.assertEqual(30, self.guest_3.wallet)
        self.assertEqual(45, self.guest_4.wallet)
