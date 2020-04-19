

import random
import copy

import Agent.Agent as Agent
import Agent.Policy as Policy
import Agent.V as V


class Agent_dynamicProgramming(Agent.Agent):

    def __init__(self, gamma=0.8):
        super().__init__()
        print("New DP Agent")
        self.name = "DP_Agent"
        self.gamma = gamma


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
        actionDistribution = self.policy(self.state) # Select action distribution from policy
        actionDistribution = sorted(actionDistribution, key=lambda x : x[1]) # Sort action distribution
        actionPair = actionDistribution[0] # Select most probable actionPair
        action = actionPair[0] # (action, actionProbability) -> action
        print(f"[{self.name}] Action {action} chosen !")
        return action


    def onTransition(self, previousState, action, newState, reward, environment):
        self._valueIteration(environment)
        print(f"[{self.name}] : Value Iteration done")

        self._computeGreedyPolicy(environment)
        # TODO : Compare new and old policy and stop if needed
        print(f"[{self.name}] : Greedy Policy computed")


    def onEpisodeEnd(self, previousEpisodesStates):
        print(f"[{self.name}] : Nothing to do at the end of an episode")

