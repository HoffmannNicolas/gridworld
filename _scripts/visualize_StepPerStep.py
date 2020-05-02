

import os
import sys

sourcePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(sourcePath)

import Agent.Agent_random as Agent_random
import Agent.Agent_dynamicProgramming as Agent_dynamicProgramming
import Agent.Agent_MC_FirstVisit_V as Agent_MC_FirstVisit_V
import Agent.Agent_nStepTD_V as Agent_nStepTD_V
import Agent.Agent_nStepTD_Q as Agent_nStepTD_Q

import Gridworld.Gridworld as Gridworld
import Gridworld.Gridworld_Vanilla as Gridworld_Vanilla
import Gridworld.Gridworld_Cliff as Gridworld_Cliff
import Gridworld.GridworldVisualizer as GridworldVisualizer

# Start training
# agent = Agent_random.Agent_random()
# agent = Agent_dynamicProgramming.Agent_dynamicProgramming(epsilon=0.8)
# agent = Agent_MC_FirstVisit_V.Agent_MC_FirstVisit_V(epsilon=0.8)
# agent = Agent_nStepTD_V.Agent_nStepTD_V(numberOfSteps=1, epsilon=0.8, alpha=0.3)
agent = Agent_nStepTD_Q.Agent_nStepTD_Q(numberOfSteps=1, epsilon=0.8, alpha=0.3)

# gridworld = Gridworld.Gridworld(agent, gridWidth=10, gridHeight=5, numberOfObstacles=20)
# gridworld = Gridworld_Vanilla.Gridworld_Vanilla(agent)
gridworld = Gridworld_Cliff.Gridworld_Cliff(agent)

visualizer = GridworldVisualizer.GridworldVisualizer(gridworld)

# Strat episode
gridworld.startEpisode()
imagesGrid = []
imagesValueFunction = []

for _ in range(3):
    imagesGrid.append(visualizer.visualizeGrid())
    # imagesValueFunction.append(visualizer.visualizeQ())

maxSteps = 500
stepNumber = 0
episodeEnded = False
while (stepNumber < maxSteps) :
    print(f"\nStep {stepNumber}")

    if (episodeEnded):
        gridworld.startEpisode()
        episodeEnded = False
    else: nextState, reward, episodeEnded = gridworld.runOneStep(verbose=True)

    imagesGrid.append(visualizer.visualizeGrid())
    # imagesValueFunction.append(visualizer.visualizeQ())
    stepNumber += 1


for _ in range(3):
    imagesGrid.append(visualizer.visualizeGrid())
    # imagesValueFunction.append(visualizer.visualizeQ())


print("Computation finished after " + str(stepNumber) + " steps.")
print("episodeEnded : ", episodeEnded)

# imagesGrid[0].save(f'_temporary/gridworldCliff.png')
imagesGrid[0].save(f'_temporary/Step{stepNumber}_{agent.name}_{gridworld.name}_grid.gif', save_all=True, append_images=imagesGrid[1:], optimize=True, duration=40, loop=0)
# imagesValueFunction[0].save(f'_temporary/Step{stepNumber}_{agent.name}_{gridworld.name}.gif', save_all=True, append_images=imagesValueFunction[1:], optimize=True, duration=40, loop=0)


