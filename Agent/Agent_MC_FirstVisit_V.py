

import random
import copy

import Agent.Agent as Agent
import Agent.Policy as Policy
import Agent.V as V


class Agent_MC_FirstVisit_V(Agent.Agent):

    def __init__(self, gamma=0.8):
        super().__init__()
        print("New MC_FirstVisit_V Agent")
        self.name = "MC_FirstVisit_V_Agent"
        self.gamma = gamma
        
        self.returns = None # Specific to MC, this object contains the returns to be averaged, for all state


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
        actionDistribution = self.policy(self.state) # Select action distribution from policy
        print("actionDistribution : ", actionDistribution)
        actionDistribution = sorted(actionDistribution, key=lambda x : x[1]) # Sort action distribution
        actionPair = random.choice(actionDistribution) # Select one action from the distribution. By construction, they shall all have same probability.
        action = actionPair[0] # (action, actionProbability) -> action
        print(f"[{self.name}] Action {action} chosen !")
        return action


    def onTransition(self, previousState, action, newState, reward, environment):
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


