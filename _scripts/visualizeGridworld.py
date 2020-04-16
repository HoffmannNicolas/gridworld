

import os
import sys

sourcePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(sourcePath)


import Gridworld.Gridworld as Gridworld


gridworld = Gridworld.Gridworld()
gridworld()

# Start Episode
gridworld.startEpoch()

possibleActions = gridworld.possibleActions()

agentAction = gridworld.agent.choseAction(possibleActions)

reward, episodeEnded = gridworld.step(agentAction)

print("reward ", reward)
print("episodeEnded ", episodeEnded)
