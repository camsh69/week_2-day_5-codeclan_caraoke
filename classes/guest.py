class Guest:

    def __init__(self, name, wallet, fav_song):
        self.name = name
        self.wallet = wallet
        self.fav_song = fav_song

    def reduce_wallet(self, amount):
        self.wallet -= amount

    def fav_song_on_list(self, fav_song, room):
        if room.find_song(fav_song) != False:
            return "Woohoo!"
        return "You don't have my favourite song"