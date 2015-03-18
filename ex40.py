class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
			
happy_bday = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"])
					
bulls_on_parade = Song(["They rally around tha family",
						"With pockets full of shells"])
						
katy_song_line_1 = "California girls"
katy_song_line_2 = "Sporty and strong"
katy_song_line_3 = "Love to sing a song"

						
katy_perry_song = Song([katy_song_line_1,
						katy_song_line_2,
						katy_song_line_3])
						
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

katy_perry_song.sing_me_a_song()