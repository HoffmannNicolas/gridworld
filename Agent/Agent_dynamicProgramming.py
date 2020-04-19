

import random
import copy

import Agent.Agent as Agent
import Agent.Policy as Policy
import Agent.V as V


class Agent_dynamicProgramming(Agent.Agent):

    def __init__(self, gamma=0.8, epsilon=1):
        super().__init__()
        print("New DP Agent")
        self.gamma = gamma
        self.epsilon = epsilon
        self.name = "DP_Agent"
        if (self.epsilon < 1): self.name = self.name + f"_eps{self.epsilon}"


    def onEpisodeStart(self, environment):
        if (self.V == None):
            self.V = V.V(environment)
            self.V.setValue(environment.goalState, 0)
            print(f"[{self.name}] : V set up")

        if (self.policy == None):
            self.policy = Policy.Policy(environment)
            self._computeGreedyPolicy(environment)
            print(f"[{self.name}] : Policy set up")


    def choseAction(self, environment):
        if (self.epsilon == 1): return self._sampleActionFromPolicy(environment, verbose=True)
        else: return self._epsilonGreedyActionFromPolicy(environment, verbose=True)


    def onTransition(self, previousState, action, newState, reward, environment):
        self._valueIteration(environment)
        print(f"[{self.name}] : Value Iteration done")

        self._computeGreedyPolicy(environment)
        # TODO : Compare new and old policy and stop if needed
        print(f"[{self.name}] : Greedy Policy computed")


    def onEpisodeEnd(self, previousEpisodesStates):
        print(f"[{self.name}] : Nothing to do at the end of an episode")

