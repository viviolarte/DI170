class Song:
    def _init_(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


# Example songs
stairway = Song([
    "There's a lady who's sure",
    "all that glitters is gold",
    "and she's buying a stairway to heaven"
])

happy_birthday = Song([
    "Happy birthday to you",
    "Happy birthday to you",
    "Happy birthday dear friend",
    "Happy birthday to you"
])

# Call the method
stairway.sing_me_a_song()
print()
happy_birthday.sing_me_a_song()