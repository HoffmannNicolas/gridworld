

import os
import sys

sourcePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(sourcePath)

import Gridworld.Gridworld as Gridworld
import Gridworld.GridworldVisualizer as GridworldVisualizer

gridworld = Gridworld.Gridworld()
gridworld()




# Start Episode
gridworld.startEpoch()

visualizer = GridworldVisualizer.GridworldVisualizer(gridworld)
images = []
for _ in range(3): images.append(visualizer.draw())

maxSteps = 200
stepNumber = 0
episodeEnded = False
while not(episodeEnded) and (stepNumber < maxSteps) :
    possibleActions = gridworld.possibleActions()

    agentAction = gridworld.agent.choseAction(possibleActions)

    reward, episodeEnded = gridworld.step(agentAction)

    images.append(visualizer.draw())
    stepNumber += 1

for _ in range(3): images.append(visualizer.draw())


print("Episode finished after " + str(stepNumber) + " steps.")
print("episodeEnded : ", episodeEnded)

images[0].save('_temporary/episode.gif', save_all=True, append_images=images[1:], optimize=False, duration=40, loop=0)


