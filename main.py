# main

class Game:
	def __init__(self):
		self.running = True
		self.won = False
		self.lost = False
		self.round = 0
		
class Player:
	def __init__(self):
		self.score = 0
		self.level = 0
		
class Power:
	def __init__(self, name="power"):
		self.name = name
		self.description = ""
		self.traits = []
		
	def describe(self):
		print(self.description)
		
	def show_traits(self):
		for trait in self.traits:
			if trait != self.traits[-1]:
				print(trait, end=", ")
			else:
				print(trait, end=".")

class Rune(Power):
	def __init__(self, name="rune"):
		self.name = name

class Glyph(Power):
	def __init__(self, name="glyph"):
		self.name = name
			
game = Game()
player = Player()

rune_oak = Rune("Oak Tree")
rune_oak.description = "Great power grows from a small beginning."
rune_oak.traits = ["strength", "healing", "growth"]

rune_poet = Rune("The Poet")
rune_poet.description = "The power of creation flows from word and song."

rune_yew = Rune("Yew Tree")
rune_yew.description = "True aim and timing is granted."

rune_serpent = Rune("World Serpent")
rune_serpent.description = "The duality of nature is revealed, hardship can be endured."

soil_rune = Rune("Soil of Earth")
soil_rune.description = "All living things must return to the soil, so that life may spring anew."

rune_oak.show_traits()

