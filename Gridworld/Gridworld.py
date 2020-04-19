

import os
import sys
sourcePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(sourcePath)

import numpy as np
import random


class Gridworld():


    def __init__(self, agent, gridWidth=20, gridHeight=5, numberOfObstacles=20):
        print("New Gridworld")
        self.name = "Gridworld"

        self.gridHeight = gridHeight
        self.gridWidth = gridWidth

        self.grid = np.zeros((self.gridHeight, self.gridWidth), dtype=int)

        # In Gridworld, a state is a coordinate.
        self.startState = self._generateObjectState()
        self.goalState = self._generateObjectState()

        self.numberOfObstacles = numberOfObstacles
        self.obstacles = []
        for _ in range(self.numberOfObstacles):
            obstacleCoord = self._generateObjectState()
            if (obstacleCoord != self.startState and obstacleCoord != self.goalState) :
                # TODO : Also check if a path still exists from startState to goalState
                self.obstacles.append(obstacleCoord)

        self.agent = agent

        self.episodeIsRunning = False


    def _generateObjectState(self):
        return (random.randint(0, self.gridWidth-1), # X-coord
            random.randint(0, self.gridHeight-1)) # Y-coord


    def states(self):
        return [(xCoord, yCoord) for xCoord in range(self.gridWidth) for yCoord in range(self.gridHeight)]


    def emptyStates(self):
        states = self.states()
        emptyStates = [state for state in states if (state not in self.obstacles)]
        return emptyStates
    

    def _transition(self, currentState, action):
    
        nextState = currentState
            # Apply transition without constraints
        if (action == "UP") : nextState = (nextState[0], nextState[1]-1)
        if (action == "DOWN") : nextState = (nextState[0], nextState[1]+1)
        if (action == "LEFT") : nextState = (nextState[0]-1, nextState[1])
        if (action == "RIGHT") : nextState = (nextState[0]+1, nextState[1])
            # Apply constraints
        if (nextState[0] < 0 or nextState[0] > (self.gridWidth-1)) : # Horizontally out of bounds
            nextState = currentState
        if (nextState[1] < 0 or nextState[1] > (self.gridHeight-1)) : # Vertically out of bounds
            nextState = currentState
        if (nextState in self.obstacles): nextState = currentState # Bounced into obstacle

        nextStepProbability = 1 # Deterministic transition
        reward, episodeEnded = self._reward(currentState, nextState)
        
        return [(nextState, nextStepProbability, reward, episodeEnded)] # Returns a list of all possible next steps


    def _reward(self, currentState, nextState):
        nextReward = 0
        episodeEnded = False
        if (currentState != self.goalState and nextState == self.goalState):
            nextReward = 1
            episodeEnded = True
        return nextReward, episodeEnded


    def startEpisode(self):
        print(f"[{self.name}] : New episode started !")
        self.agent.state = self.startState
        self.agent.onEpisodeStart(self)
        self.episodeIsRunning = True


    def endEpisode(self):
        print(f"[{self.name}] : Episode ended")
        self.episodeIsRunning = False
        self.agent.onEpisodeEnd(self)


    def possibleActions(self, state):
        return ("UP", "DOWN", "LEFT", "RIGHT")


    def runOneStep(self):
        if (self.episodeIsRunning == False):
            print(f"[{self.name}] : No episode Running : start one with gridworld.startEpisode()")
            return

        agentAction = self.agent.choseAction(self)

        currentState = self.agent.state
        nextState, nextStateProbability, reward, episodeEnded = self._transition(currentState, agentAction)[0] # Gridworld deterministic : Only one poccible next step
        self.agent.state = nextState

        self.agent.onTransition(currentState, agentAction, nextState, reward, self)

        if (episodeEnded) : self.endEpisode()

        return nextState, reward, episodeEnded


    def runOneEpisode(self):
        if not(self.episodeIsRunning):
            self.startEpisode()
        
        episodeEnded = False
        while (episodeEnded == False) :
            _, _, episodeEnded = self.runOneStep()

        self.endEpisode()

        return


    def runFullTraining(self):
        # TODO : Keep running episodes until convergence of policy
        for _ in range(10): self.runOneEpisode()

