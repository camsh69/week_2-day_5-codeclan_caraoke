import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest
from classes.bar_tab import BarTab

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.song_1 = Song("I Will Survive")
        self.song_2 = Song("Sweet Caroline")
        self.song_3 = Song("Yesterday")
        self.song_list = [self.song_1, self.song_2]
        self.guest_1 = Guest("Harry Tonedeaf", 25, "Bohemian Rhapsody")
        self.guest_2 = Guest("Sheila Diva", 15, "My Heart Will Go On")
        self.guest_3 = Guest("Larry Crooner", 35, "Suspicious Minds")
        self.guest_4 = Guest("Tina Tuneless", 45, "I Will Survive")
        self.guest_1_bar_tab = BarTab(self.guest_1.name, 5)
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

    def test_check_out_guest_with_no_bar_tab(self):
        self.room.check_out_guest(self.guest_1, None)
        self.assertEqual(1, self.room.guest_count())

    def test_check_out_guest_with_bar_tab(self):
        self.room.check_out_guest(self.guest_1, self.guest_1_bar_tab.amount)
        self.assertEqual(1, self.room.guest_count())
        self.assertEqual(5, self.room.till)

    def test_can_increase_till(self):
        self.room.increase_till(self.room.price)
        self.assertEqual(5, self.room.till)

    def test_bar_tab_can_increase_till(self):
        self.room.increase_till(self.guest_1_bar_tab.amount)
        self.assertEqual(5, self.room.till)

    def test_check_in_and_check_out_guests_integrated_test(self):
        self.room_2.check_in_guest(self.guest_1)
        self.room_2.check_in_guest(self.guest_2)
        self.room_2.check_in_guest(self.guest_3)
        self.room_2.add_song_to_room(self.song_1)
        self.room_2.add_song_to_room(self.song_2)
        self.room_2.add_song_to_room(self.song_3)
        self.assertEqual("Sorry, the maximum number of guests is 3", self.room_2.check_in_guest(self.guest_4))
        self.assertEqual(3, self.room_2.guest_count())
        self.assertEqual(15, self.room_2.till)
        self.assertEqual(20, self.guest_1.wallet)
        self.assertEqual(10, self.guest_2.wallet)
        self.assertEqual(30, self.guest_3.wallet)
        self.assertEqual(45, self.guest_4.wallet)
        self.guest_1_bar_tab.increase_bar_tab(5)
        self.room_2.check_out_guest(self.guest_1, self.guest_1_bar_tab.amount)
        self.assertEqual(2, self.room_2.guest_count())
        self.assertEqual(25, self.room_2.till)
        self.assertEqual(10, self.guest_1.wallet)
        self.room_2.check_in_guest(self.guest_4)
        self.assertEqual(3, self.room_2.guest_count())
        self.assertEqual(30, self.room_2.till)
        self.assertEqual(40, self.guest_4.wallet)
        self.assertEqual(True, self.room_2.find_song(self.song_1))
        self.assertEqual(True, self.room_2.find_song(self.song_2))
        self.assertEqual(True, self.room_2.find_song(self.song_3))
        self.assertEqual("Woohoo!", self.guest_4.fav_song_on_list(self.song_3, self.room_2))