import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song = Song("I will survive")

    def test_song_has_title(self):
        self.assertEqual("I will survive", self.song.title)