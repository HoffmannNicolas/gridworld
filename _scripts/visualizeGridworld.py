

import os
import sys

sourcePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(sourcePath)

import Agent.randomAgent as randomAgent
import Agent.dynamicProgrammingAgent as dynamicProgrammingAgent

import Gridworld.Gridworld as Gridworld
import Gridworld.GridworldVisualizer as GridworldVisualizer


# Start training
agent = dynamicProgrammingAgent.dynamicProgrammingAgent()
# agent = randomAgent.randomAgent()
gridworld = Gridworld.Gridworld(agent)

visualizer = GridworldVisualizer.GridworldVisualizer(gridworld)

# Strat episode
gridworld.startEpisode()
imagesGrid = []
imagesV = []

for _ in range(3):
    imagesGrid.append(visualizer.visualizeGrid())
    imagesV.append(visualizer.visualizeV())

maxSteps = 20
stepNumber = 0
episodeEnded = False
while not(episodeEnded) and (stepNumber <= maxSteps) :
    print(f"\nStep {stepNumber}")
    nextState, reward, episodeEnded = gridworld.runOneStep()

    imagesGrid.append(visualizer.visualizeGrid())
    imagesV.append(visualizer.visualizeV())
    stepNumber += 1

for _ in range(3):
    imagesGrid.append(visualizer.visualizeGrid())
    imagesV.append(visualizer.visualizeV())


print("Computation finished after " + str(stepNumber) + " steps.")
print("episodeEnded : ", episodeEnded)

imagesGrid[0].save('_temporary/episode_grid.gif', save_all=True, append_images=imagesGrid[1:], optimize=False, duration=40, loop=0)
imagesV[0].save('_temporary/episode_V.gif', save_all=True, append_images=imagesV[1:], optimize=False, duration=40, loop=0)


