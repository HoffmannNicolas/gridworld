

from abc import abstractmethod


class Agent():

    def __init__(self):
        print("New agent created")
        self.state = None

    @abstractmethod
    def onEpisodeStart(self): pass
        # Set-up the ressources specific for an episode

    @abstractmethod
    def choseAction(self, possibleActions): pass
        # Select chosen action to the environment

    @abstractmethod
    def onTransition(self): pass
        # Computations after an action has been chosen and the environment computed the transition

    @abstractmethod
    def onEpisodeEnd(self): pass
        # Computations of the end of an episode

