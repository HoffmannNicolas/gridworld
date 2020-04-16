

import os
import sys

sourcePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(sourcePath)


import Gridworld.Gridworld as Gridworld


gridworld = Gridworld.Gridworld()
gridworld()


# Start Episode
gridworld.startEpoch()

episodeEnded = False
while not(episodeEnded):
	possibleActions = gridworld.possibleActions()

	agentAction = gridworld.agent.choseAction(possibleActions)

	print(gridworld.agent)
	reward, episodeEnded = gridworld.step(agentAction)
	print(gridworld.agent)

print("reward ", reward)
print("episodeEnded ", episodeEnded)
