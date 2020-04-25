

import random
import copy

import Agent.Agent as Agent
import Agent.Policy as Policy
import Agent.Q as Q


class Agent_nStepTD_Q(Agent.Agent):

    def __init__(self, gamma=0.8, epsilon=1, alpha=0.9, numberOfSteps=1, verbose=False):
        super().__init__()
        print(f"New {numberOfSteps}StepTD_Q Agent")
        self.gamma = gamma
        assert (epsilon >= 0 and epsilon <= 1), f"Espilon {epsilon} out of bound : 0 <= Epsilon <= 1"
        self.epsilon = epsilon
        self.numberOfSteps = numberOfSteps
        self.alpha = alpha
        self.verbose = verbose
        
        self.name = f"{numberOfSteps}StepTD_Q_Agent"
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
        
        self.episode = [] # Used to store temporary information in-between spets for later update


    def choseAction(self, environment, verbose=False):
        if (self.epsilon == 1): return self._sampleActionFromPolicy(environment, verbose=self.verbose)
        else: return self._epsilonGreedyActionFromPolicy(environment, verbose=self.verbose)


    def onTransition(self, previousState, action, nextState, reward, environment, verbose=False):
        # "Reinforcement Learning, An Introduction" Second edition, Sutton & Barto (p.120 6.2)

        if (len(self.episode) == 0):
            # This is the very first step, we cannot make updates because we miss some information. We only store information for later use
            self.episode.append(action)
            return

        previousAction = self.episode[0]
        valueError = reward + self.gamma * self.Q(nextState, action) - self.Q(previousState, previousAction)
        newValue = self.Q(previousState, previousAction) + self.alpha * valueError
        self.Q.setValue(previousState, action, newValue)
        self.episode[0] = action # Remember current action for later updates
        if (self.verbose): print(f"[{self.name}] : Q updated !")

        self._computeGreedyPolicy_fromQ(environment)
        if (self.verbose): print(f"[{self.name}] : Policy updated !")


    def onEpisodeEnd(self, environment, verbose=False):
        if (verbose): print(f"[{self.name}] : No process after episode")

