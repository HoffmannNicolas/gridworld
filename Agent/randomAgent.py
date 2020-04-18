

import random

import Agent.Agent as Agent


class randomAgent(Agent.Agent):

    def __init__(self):
        print("New Random Agent")
        self.name = "RandomAgent"


    def onEpisodeStart(self):
        print(f"[{self.name}] : Nothing to set up before an episode.")


    def choseAction(self, possibleActions):
        action = random.choice(possibleActions)
        print(f"[{self.name}] Action {action} chosen !")
        return action


    def onTransition(self):
        print(f"[{self.name}] : Time to learn, but random agents do not learn !")


    def onEpisodeEnd(self):
        print(f"[{self.name}] : Nothing to do at the end of an episode either.")

