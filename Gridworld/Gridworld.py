


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
		return [random.randint(0, self.gridWidth-1), # X-coord
			random.randint(0, self.gridHeight-1)] # Y-coord


	def _transition(self, currentCoord, agentAction):
		nextCoord = currentCoord
			# Apply transition without constraints
		if (agentAction == "UP") : nextCoord[1] -= 1
		if (agentAction == "DOWN") : nextCoord[1] += 1
		if (agentAction == "LEFT") : nextCoord[0] -= 1
		if (agentAction == "RIGHT") : nextCoord[0] += 1
			# Apply constraints
		if (nextCoord[0] < 0 or nextCoord[0] > (self.gridWidth-1)) : nextCoord = self.agent.coord
		if (nextCoord[1] < 0 or nextCoord[1] > (self.gridHeight-1)) : nextCoord = self.agent.coord

		return nextCoord


	def _reward(self, currentCoord, nextCoord):
		nextReward = 0
		episodeEnded = False
		if (currentCoord != self.goalCoord and nextCoord == self.goalCoord) :
			nextReward = 1
			episodeEnded = True
		return nextReward, episodeEnded


	def startEpoch(self):
		self.agent.coord = self._generateObjectCoord()


	def possibleActions(self):
		return ("UP", "DOWN", "LEFT", "RIGHT")


	def step(self, agentAction):
		
		nextCoord = self._transition(self.agent.coord, agentAction)

		reward, episodeEnded = self._reward(self.agent.coord, agentAction)

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


	def __call__(self):
		print("Agent")
		print("coord : ", self.coord)







