

import os
import sys

sourcePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(sourcePath)

import Agent.Agent_random as Agent_random
import Agent.Agent_dynamicProgramming as Agent_dynamicProgramming
import Agent.Agent_MC_FirstVisit_V as Agent_MC_FirstVisit_V
import Agent.Agent_nStepTD_V as Agent_nStepTD_V

import Gridworld.Gridworld as Gridworld
import Gridworld.GridworldVisualizer as GridworldVisualizer


# Start training
# agent = Agent_random.Agent_random()
# agent = Agent_dynamicProgramming.Agent_dynamicProgramming(epsilon=0.8)
agent = Agent_MC_FirstVisit_V.Agent_MC_FirstVisit_V(epsilon=0.8)
# agent = Agent_nStepTD_V.Agent_nStepTD_V(numberOfSteps=1, epsilon=0.8, alpha=0.3)

gridworld = Gridworld.Gridworld(agent, gridWidth=8, gridHeight=8, numberOfObstacles=15, exploringStates=True)

visualizer = GridworldVisualizer.GridworldVisualizer(gridworld)

# Strat episode
gridworld.startEpisode()
imagesGrid = []
imagesV = []

for _ in range(5): imagesV.append(visualizer.visualizeV())

maxNumberOfEpisodes = 100
episodeNumber = 0
while (episodeNumber < maxNumberOfEpisodes) :

    numberOfSteps = gridworld.runOneEpisode(verbose=False)
    imagesV.append(visualizer.visualizeV())
    episodeNumber += 1

    print(f"Episode {episodeNumber} ; {numberOfSteps} steps")

for _ in range(5): imagesV.append(visualizer.visualizeV())


print("Computation finished after " + str(episodeNumber) + " steps.")

imagesV[0].save(f'_temporary/Episode{episodeNumber}_{agent.name}.gif', save_all=True, append_images=imagesV[1:], optimize=True, duration=40, loop=0)


