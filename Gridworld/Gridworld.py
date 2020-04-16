


import numpy as np
import random


class Gridworld():


	def __init__(self, gridWidth=5, gridHeight=5):
		print("New Gridworld")

		self.gridHeight = gridHeight
		self.gridWidth = gridWidth

		self.grid = np.zeros((self.gridHeight, self.gridWidth), dtype=int)

		self.startCoord = self._generateObjectCoord()
		self.goalCoord = self._generateObjectCoord()

		self.agent = GridworldAgent()


	def _generateObjectCoord(self):
		return (random.randint(0, self.gridWidth-1), # X-coord
			random.randint(0, self.gridHeight-1)) # Y-coord


	def _transition(self, currentCoord, action):
		nextCoord = currentCoord
			# Apply transition without constraints
		if (action == "UP") : nextCoord = (nextCoord[0], nextCoord[1]-1)
		if (action == "DOWN") : nextCoord = (nextCoord[0], nextCoord[1]+1)
		if (action == "LEFT") : nextCoord = (nextCoord[0]-1, nextCoord[1])
		if (action == "RIGHT") : nextCoord = (nextCoord[0]+1, nextCoord[1])
			# Apply constraints
		if (nextCoord[0] < 0 or nextCoord[0] > (self.gridWidth-1)) :
			nextCoord = currentCoord
		if (nextCoord[1] < 0 or nextCoord[1] > (self.gridHeight-1)) :
			nextCoord = currentCoord
		return nextCoord


	def _reward(self, currentCoord, nextCoord):
		nextReward = 0
		episodeEnded = False

		if (currentCoord != self.goalCoord and nextCoord == self.goalCoord):
			nextReward = 1
			episodeEnded = True
		return nextReward, episodeEnded


	def startEpoch(self):
		self.agent.coord = self._generateObjectCoord()


	def possibleActions(self):
		return ("UP", "DOWN", "LEFT", "RIGHT")


	def step(self, agentAction):
		
		currentCoord = self.agent.coord
		nextCoord = self._transition(currentCoord, agentAction)

		reward, episodeEnded = self._reward(currentCoord, nextCoord)

		self.agent.coord = nextCoord

		return reward, episodeEnded


	def __call__(self):
		print("grid : ", self.grid)
		print("startCoord : ", self.startCoord)
		print("goalCoord : ", self.goalCoord)




class GridworldAgent():

	def __init__(self):
		print("New Agent")
		self.coord = None


	def choseAction(self, possibleActions):
		return random.choice(possibleActions)


	def __str__(self):
		return "Agent " + str(self.coord)







