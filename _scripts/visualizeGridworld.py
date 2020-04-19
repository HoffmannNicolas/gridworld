

import os
import sys

sourcePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(sourcePath)

import Agent.Agent_random as Agent_random
import Agent.Agent_dynamicProgramming as Agent_dynamicProgramming
import Agent.Agent_MC_FirstVisit_V as Agent_MC_FirstVisit_V

import Gridworld.Gridworld as Gridworld
import Gridworld.GridworldVisualizer as GridworldVisualizer


# Start training
# agent = Agent_random.Agent_random()
# agent = Agent_dynamicProgramming.Agent_dynamicProgramming()
agent = Agent_MC_FirstVisit_V.Agent_MC_FirstVisit_V()

gridworld = Gridworld.Gridworld(agent, gridWidth=5, gridHeight=5, numberOfObstacles=5)

visualizer = GridworldVisualizer.GridworldVisualizer(gridworld)

# Strat episode
gridworld.startEpisode()
imagesGrid = []
imagesV = []

for _ in range(3):
    imagesGrid.append(visualizer.visualizeGrid())
    imagesV.append(visualizer.visualizeV())

maxSteps = 200
stepNumber = 0
episodeEnded = False
while (stepNumber < maxSteps) :
    print(f"\nStep {stepNumber}")

    if (episodeEnded):
        gridworld.startEpisode()
        episodeEnded = False
    else: nextState, reward, episodeEnded = gridworld.runOneStep()

    imagesGrid.append(visualizer.visualizeGrid())
    imagesV.append(visualizer.visualizeV())
    stepNumber += 1


for _ in range(3):
    imagesGrid.append(visualizer.visualizeGrid())
    imagesV.append(visualizer.visualizeV())


print("Computation finished after " + str(stepNumber) + " steps.")
print("episodeEnded : ", episodeEnded)

imagesGrid[0].save(f'_temporary/Step{stepNumber}_{agent.name}_grid.gif', save_all=True, append_images=imagesGrid[1:], optimize=True, duration=40, loop=0)
imagesV[0].save(f'_temporary/Step{stepNumber}_{agent.name}__V.gif', save_all=True, append_images=imagesV[1:], optimize=True, duration=40, loop=0)


