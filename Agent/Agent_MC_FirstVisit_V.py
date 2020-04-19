

import random
import copy

import Agent.Agent as Agent
import Agent.Policy as Policy
import Agent.V as V


class Agent_MC_FirstVisit_V(Agent.Agent):

    def __init__(self, gamma=0.8, epsilon=1):
        super().__init__()
        print("New MC_FirstVisit_V Agent")
        self.gamma = gamma
        assert (epsilon >= 0 and epsilon <= 1), f"Espilon {epsilon} out of bound : 0 <= Epsilon <= 1"
        self.epsilon = epsilon
        
        self.returns = None # Specific to MC, this object contains the returns to be averaged, for all state
        self.name = "MC_FirstVisit_V_Agent"
        if (self.epsilon < 1): self.name = self.name + f"_eps{self.epsilon}"


    def onEpisodeStart(self, environment):
        if (self.V == None):
            self.V = V.V(environment, initialValue=0)
            print(f"[{self.name}] : V set up")

        if (self.policy == None):
            self.policy = Policy.Policy(environment)
            self._computeGreedyPolicy(environment)
            print(f"[{self.name}] : Policy set up")

        if (self.returns == None):
            self.returns = {}
            for state in environment.states():
                if not(isinstance(state, str)): state = str(state)
                self.returns[state] = []
            print(f"[{self.name}] : Returns set up")

        self.episode = []
        print(f"[{self.name}] : Ready to record a new episode")


    def choseAction(self, environment):
        if (self.epsilon == 1): return self._sampleActionFromPolicy(environment, verbose=True)
        else: return self._epsilonGreedyActionFromPolicy(environment, verbose=True)


    def onTransition(self, previousState, action, nextState, reward, environment):
        self.episode.append((previousState, action, reward))
        print(f"[{self.name}] Step recorded !")


    def onEpisodeEnd(self, environment):
        print("self.episode : ", self.episode)

        previousEpisodesStates = [state for state, action, reward in self.episode]
        G = 0
        for stepNumber, (state, action, reward) in enumerate(self.episode[::-1]): # Loop through episode from end to start
            G = self.gamma * G + reward

            previousEpisodesStates.pop() # Remove last element of that list (which corresponds to current time step)
            if state not in previousEpisodesStates:
                self.returns[str(state)].append(G)
                averageG = sum(self.returns[str(state)]) / len(self.returns[str(state)])
                self.V.setValue(state, averageG) 
        print(f"[{self.name}] V updated !")

        self._computeGreedyPolicy(environment)
        print(f"[{self.name}] Policy updated !")


