from pygame import mixer

def play(song):
	mixer.music.stop()
	mixer.music.load(song)
	mixer.music.play(-1)