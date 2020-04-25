

import random
import copy

import Agent.Agent as Agent
import Agent.Policy as Policy
import Agent.Q as Q


class Agent_nStepTD_Q_offPolicy(Agent.Agent):

    def __init__(self, gamma=0.8, epsilon=1, alpha=0.9, numberOfSteps=1, verbose=False):
        super().__init__()
        print(f"New {numberOfSteps}StepTD_Q_offPolicy Agent")
        self.gamma = gamma
        assert (epsilon >= 0 and epsilon <= 1), f"Espilon {epsilon} out of bound : 0 <= Epsilon <= 1"
        self.epsilon = epsilon
        self.numberOfSteps = numberOfSteps
        self.alpha = alpha
        self.verbose = verbose
        
        self.name = f"{numberOfSteps}StepTD_Q_Agent_offPolicy (Q-learning)"
        if (self.epsilon < 1): self.name = self.name + f"_eps{self.epsilon}"
        self.name = self.name + f"_alpha{self.alpha}"


    def onEpisodeStart(self, environment, verbose=False):
        if (self.Q == None):
            self.Q = Q.Q(environment)
            print(f"[{self.name}] : Q set up")

        if (self.policy == None):
            self.policy = Policy.Policy(environment)
            self._computeGreedyPolicy_fromQ(environment)
            print(f"[{self.name}] : Policy set up")
        

    def choseAction(self, environment, verbose=False):
        if (self.epsilon == 1): return self._sampleActionFromPolicy(environment, verbose=self.verbose)
        else: return self._epsilonGreedyActionFromPolicy(environment, verbose=self.verbose)


    def onTransition(self, previousState, action, state, reward, environment, verbose=False):
        # "Reinforcement Learning, An Introduction" Second edition, Sutton & Barto (p.131 6.8)

        bestNextActionValue = -1
        for nextAction in environment.possibleActions(state):
            if (self.Q(state, nextAction) > bestNextActionValue):
                bestNextActionValue = self.Q(state, nextAction)
        valueError = reward + self.gamma * bestNextActionValue - self.Q(previousState, action)
        newValue = self.Q(previousState, action) + self.alpha * valueError
        self.Q.setValue(previousState, action, newValue)
        if (self.verbose): print(f"[{self.name}] : Q updated !")

        self._computeGreedyPolicy_fromQ(environment)
        if (self.verbose): print(f"[{self.name}] : Policy updated !")


    def onEpisodeEnd(self, environment, verbose=False):
        if (verbose): print(f"[{self.name}] : No process after episode")

