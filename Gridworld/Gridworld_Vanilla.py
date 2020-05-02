

import os
import sys
sourcePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(sourcePath)

from Gridworld.Gridworld import Gridworld as Gridworld

import numpy as np
import random


class Gridworld_Vanilla(Gridworld):

    def __init__(self, agent):
        print("New Gridworld")
        self.name = "Gridworld"
        self.gridHeight = 3
        self.gridWidth = 4
        self.grid = np.zeros((self.gridHeight, self.gridWidth), dtype=int)
        self.exploringStates = False
        self.startState = (0, 2)
        self.goalState = (3, 0)
        self.obstacles = [(1, 1), (3, 1)]
        self.obstacleCosts = [0, -1]
        self.agent = agent
        self.episodeIsRunning = False

