class Room:

    def __init__(self, name, songs, guests, max_guests, price):
        self.name = name
        self.songs = songs
        self.guests = guests
        self.max_guests = max_guests
        self.price = price
        self.till = 0

    def guest_count(self):
        return len(self.guests)

    def find_song(self, song_name):
        for song in self.songs:
            if song == song_name:
                return True
        return False

    def add_song_to_room(self, song_name):
        self.songs.append(song_name)

    def check_out_guest(self, guest):
        self.guests.remove(guest)

    def increase_till(self, amount):
        self.till += amount

    def check_in_guest(self, guest):
        if self.guest_count() < self.max_guests:
            self.guests.append(guest)
            self.increase_till(self.price)
            guest.reduce_wallet(self.price)
        return f"Sorry, the maximum number of guests is {self.max_guests}"

