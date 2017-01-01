class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there."])

bulls_on_parade = Song(["They rally around the family",
                        "WIth a pocket full of shells"])

rap_god = Song(["But for me to rap like a computer must be in my genes",
                "I got a laptop in my back pocket",
                "My pen'll go off when I half-cock it",
                "Got a fat knot from that rap profit"])

# happy_bday.sing_me_a_song()

# bulls_on_parade.sing_me_a_song()

rap_god.sing_me_a_song()