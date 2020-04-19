

import random

import Agent.Agent as Agent
import Agent.Policy as Policy
import Agent.V as V


class Agent_random(Agent.Agent):

    def __init__(self):
        super().__init__()
        print("New Random Agent")
        self.name = "RandomAgent"


    def onEpisodeStart(self, environment, verbose=False):
        print(f"[{self.name}] : Ready for new episode.")


    def choseAction(self, environment):
        return self._choseRandomAction(environment, verbose=False)


    def onTransition(self, environment, verbose=False):
        print(f"[{self.name}] : Time to learn, but random agents do not learn !")


    def onEpisodeEnd(self, verbose=False):
        print(f"[{self.name}] : Nothing to do at the end of an episode either.")

