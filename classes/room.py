class Room:

    def __init__(self, name, songs, guests):
        self.name = name
        self.songs = songs
        self.guests = guests

    def guest_count(self):
        return len(self.guests)
