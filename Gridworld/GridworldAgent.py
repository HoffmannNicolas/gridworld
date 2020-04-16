

import random



class GridworldAgent():

	def __init__(self):
		print("New Agent")
		self.coord = None


	def choseAction(self, possibleActions):
		return random.choice(possibleActions)


	def __str__(self):
		return "Agent " + str(self.coord)







