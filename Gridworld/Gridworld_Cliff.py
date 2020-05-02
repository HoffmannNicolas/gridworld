

import os
import sys
sourcePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(sourcePath)

from Gridworld.Gridworld import Gridworld as Gridworld

import numpy as np
import random


class Gridworld_Cliff(Gridworld):

    def __init__(self, agent, cliffHeight=4, cliffWidth=12):
        print("New Gridworld")
        self.name = "Gridworld_Cliff"

        self.gridHeight = cliffHeight
        self.gridWidth = cliffWidth

        self.grid = np.zeros((self.gridHeight, self.gridWidth), dtype=int)
        self.exploringStates = False
        self.startState = (0, self.gridHeight-1)
        self.goalState = (self.gridWidth-1, self.gridHeight-1)

        self.obstacles = []
        self.obstacleCosts = []
        for xCoord in range(1, self.gridWidth-1):
            self.obstacles.append((xCoord, self.gridHeight-1))
            self.obstacleCosts.append(-1)
        self.agent = agent
        self.episodeIsRunning = False

