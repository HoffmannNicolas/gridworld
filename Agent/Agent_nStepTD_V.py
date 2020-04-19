

import random
import copy

import Agent.Agent as Agent
import Agent.Policy as Policy
import Agent.V as V


class Agent_nStepTD_V(Agent.Agent):

    def __init__(self, gamma=0.8, epsilon=1, alpha=0.9, numberOfSteps=1, verbose=False):
        super().__init__()
        print(f"New {numberOfSteps}StepTD_V Agent")
        self.gamma = gamma
        assert (epsilon >= 0 and epsilon <= 1), f"Espilon {epsilon} out of bound : 0 <= Epsilon <= 1"
        self.epsilon = epsilon
        self.numberOfSteps = numberOfSteps
        self.alpha = alpha
        self.verbose = verbose
        
        self.name = f"{numberOfSteps}StepTD_V_Agent"
        if (self.epsilon < 1): self.name = self.name + f"_eps{self.epsilon}"
        self.name = self.name + f"_alpha{self.alpha}"


    def onEpisodeStart(self, environment):
        if (self.V == None):
            self.V = V.V(environment)
            print(f"[{self.name}] : V set up")

        if (self.policy == None):
            self.policy = Policy.Policy(environment)
            self._computeGreedyPolicy(environment)
            print(f"[{self.name}] : Policy set up")


    def choseAction(self, environment):
        if (self.epsilon == 1): return self._sampleActionFromPolicy(environment, verbose=self.verbose)
        else: return self._epsilonGreedyActionFromPolicy(environment, verbose=self.verbose)


    def onTransition(self, previousState, action, nextState, reward, environment):
        # "Reinforcement Learning, An Introduction" Second edition, Sutton & Barto (p.120 6.2)

        valueError = reward + self.gamma * self.V(nextState) - self.V(previousState)
        newValue = self.V(previousState) + self.alpha * valueError
        self.V.setValue(previousState, newValue)
        if (self.verbose): print(f"[{self.name}] : V updated !")

        self._computeGreedyPolicy(environment)
        if (self.verbose): print(f"[{self.name}] : Policy updated !")


    def onEpisodeEnd(self, environment):
        print(f"[{self.name}] : No process after episode")

