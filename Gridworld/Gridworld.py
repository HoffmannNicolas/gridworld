

import os
import sys
sourcePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(sourcePath)

import numpy as np
import random


class Gridworld():


    def __init__(self, agent, gridWidth=20, gridHeight=5):
        print("New Gridworld")
        self.name = "Gridworld"

        self.gridHeight = gridHeight
        self.gridWidth = gridWidth

        self.grid = np.zeros((self.gridHeight, self.gridWidth), dtype=int)

        self.startCoord = self._generateObjectCoord()
        self.goalCoord = self._generateObjectCoord()

        self.agent = agent

        self.episodeIsRunning = False


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
        if (nextCoord[0] < 0 or nextCoord[0] > (self.gridWidth-1)) : # Horizontally out of bounds
            nextCoord = currentCoord
        if (nextCoord[1] < 0 or nextCoord[1] > (self.gridHeight-1)) : # Vertically out of bounds
            nextCoord = currentCoord
        return nextCoord


    def _reward(self, currentCoord, nextCoord):
        nextReward = 0
        episodeEnded = False
        if (currentCoord != self.goalCoord and nextCoord == self.goalCoord):
            nextReward = 1
            episodeEnded = True
        return nextReward, episodeEnded


    def startEpisode(self):
        print(f"[{self.name}] : New episode started !")
        self.agent.coord = self.startCoord
        self.agent.onEpisodeStart()
        self.episodeIsRunning = True


    def endEpisode(self):
        print(f"[{self.name}] : Episode ended")
        self.episodeIsRunning = False
        self.agent.onEpisodeEnd()


    def _possibleActions(self):
        return ("UP", "DOWN", "LEFT", "RIGHT")


    def runOneStep(self):
        if (self.episodeIsRunning == False):
            print(f"[{self.name}] : No episode Running : start one with gridworld.startEpisode()")
            return

        possibleActions = self._possibleActions()

        agentAction = self.agent.choseAction(possibleActions)
        currentCoord = self.agent.coord

        nextCoord = self._transition(currentCoord, agentAction)
        reward, episodeEnded = self._reward(currentCoord, nextCoord)

        self.agent.coord = nextCoord

        self.agent.onTransition()

        if (episodeEnded) : self.endEpisode()

        return nextCoord, reward, episodeEnded


    def runOneEpisode(self):
        if not(self.episodeIsRunning):
            self.startEpisode()

        episodeEnded = False
        while (episodeEnded == False) :
            _, _, episodeEnded = self.runOneStep()

        self.endEpisode()

        return


    def runFullTraining(self):
        # TODO : Keep running episodes until convergence of training
        for _ in range(10): self.runOneEpisode()

