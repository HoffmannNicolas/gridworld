

import os
import sys

sourcePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(sourcePath)


import Gridworld.Gridworld as Gridworld

gridworld = Gridworld.Gridworld()

gridworld()
