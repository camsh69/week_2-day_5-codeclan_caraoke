class Room:

    def __init__(self, name, songs, guests):
        self.name = name
        self.songs = songs
        self.guests = guests

    def guest_count(self):
        return len(self.guests)

    def find_song(self, song_name):
        for song in self.songs:
            if song == song_name:
                return True
        return False

    def add_song_to_room(self, song_name):
        self.songs.append(song_name)

    def check_in_guest(self, guest_name):
        self.guests.append(guest_name)

    def check_out_guest(self, guest_name):
        self.guests.remove(guest_name)