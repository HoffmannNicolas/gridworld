


import numpy as np
import random


class Gridworld():

	def __init__(self, gridWidth=5, gridHeight=5):
		print("New Gridworld")

		self.gridHeight = gridHeight
		self.gridWidth = gridWidth

		self.grid = np.zeros((self.gridHeight, self.gridWidth), dtype=int)

		self.startCoord = (
			random.randint(0, self.gridWidth-1), # X-coord
			random.randint(0, self.gridHeight-1) # Y-coord
		)

		self.goalCoord = (
			random.randint(0, self.gridWidth-1), # X-coord
			random.randint(0, self.gridHeight-1) # Y-coord
		)
		

	def __call__(self):
		print("grid : ", self.grid)
		print("startCoord : ", self.startCoord)
		print("goalCoord : ", self.goalCoord)


