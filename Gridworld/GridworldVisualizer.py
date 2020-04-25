

import math
from PIL import Image, ImageDraw


class GridworldVisualizer():

    def __init__(self, gridworld):
        print("New Drawer")

        self.gridworld = gridworld

        self.cellWidth = 20 # Pixels
        self.cellHeight = 20 # Pixels

        self.emptyCellColor = (100, 100, 100)
        self.wallColor = (100, 100, 100)
        self.startColor = (50, 50, 255)
        self.goalColor = (150, 255, 150)
        
        self.cellBorderColor = (50, 50, 50)
        
        self.agentColor = (255, 255, 0)

        self.obstacleColor = (100, 50, 50)
        
        self.highestVColor = (0, 255, 0)
        


    def visualizeGrid(self):

        image = Image.new(
            'RGB', 
            (self.gridworld.gridWidth * self.cellWidth, self.gridworld.gridHeight * self.cellHeight), 
            self.emptyCellColor
        )

        image = self._drawGrid(image)

        image = self._drawAgent(image)

        image = self._drawObstacles(image)
        
        return image



    def visualizeV(self):

        image = Image.new(
            'RGB', 
            (self.gridworld.gridWidth * self.cellWidth, self.gridworld.gridHeight * self.cellHeight), 
            self.emptyCellColor
        )
        image = self._drawV(image)

        image = self._drawPolicyArrows(image)

        image = self._drawGrid(image)

        image = self._drawAgent(image)

        image = self._drawObstacles(image)        
        
        return image


    def visualizeQ(self):

        image = Image.new(
            'RGB', 
            (self.gridworld.gridWidth * self.cellWidth, self.gridworld.gridHeight * self.cellHeight), 
            self.emptyCellColor
        )
        image = self._drawGrid(image)

        image = self._drawQArrows(image)
        
        image = self._drawPolicyArrows(image)

        image = self._drawAgent(image)

        image = self._drawObstacles(image)        
        
        return image


    def _drawAgent(self, image):
    
        imageDraw = ImageDraw.Draw(image)
        leftCoord = self.gridworld.agent.state[0] * self.cellWidth
        rightCoord = leftCoord + self.cellWidth - 1

        topCoord = self.gridworld.agent.state[1] * self.cellHeight
        bottomCoord = topCoord + self.cellHeight - 1

        margin = 2
        imageDraw.ellipse((leftCoord+margin, topCoord+margin, rightCoord-margin, bottomCoord-margin), fill=self.agentColor)

        return image


    def _drawObstacles(self, image):
    
        imageDraw = ImageDraw.Draw(image)

        for obstacleState in self.gridworld.obstacles:
            leftCoord = obstacleState[0] * self.cellWidth
            rightCoord = leftCoord + self.cellWidth - 1

            topCoord = obstacleState[1] * self.cellHeight
            bottomCoord = topCoord + self.cellHeight - 1

            margin = 2
            imageDraw.ellipse((leftCoord+margin, topCoord+margin, rightCoord-margin, bottomCoord-margin), fill=self.obstacleColor)

        return image


    def _drawGrid(self, image):

        imageDraw = ImageDraw.Draw(image)

        # Draw start cell
        startCellLeftCoord = self.gridworld.startState[0] * self.cellWidth
        startCellRightCoord = startCellLeftCoord + self.cellWidth - 1
        startCellTopCoord = self.gridworld.startState[1] * self.cellHeight
        startCellBottomCoord = startCellTopCoord + self.cellWidth - 1
        imageDraw.rectangle(
            [
                (startCellLeftCoord, startCellTopCoord), 
                (startCellRightCoord, startCellBottomCoord), 
            ], 
            self.startColor
        )

        # Draw goal cell
        goalCellLeftCoord = self.gridworld.goalState[0] * self.cellWidth
        goalCellRightCoord = goalCellLeftCoord + self.cellWidth - 1
        goalCellTopCoord = self.gridworld.goalState[1] * self.cellHeight
        goalCellBottomCoord = goalCellTopCoord + self.cellWidth - 1
        imageDraw.rectangle(
            [
                (goalCellLeftCoord, goalCellTopCoord), 
                (goalCellRightCoord, goalCellBottomCoord), 
            ], 
            self.goalColor
        )

        # Draw cells
        for cellCoordX in range(self.gridworld.gridWidth):
            for cellCoordY in range(self.gridworld.gridHeight):
                imageDraw.line(
                    [(cellCoordX * self.cellWidth, cellCoordY * self.cellHeight), ((cellCoordX+1) * self.cellWidth - 1, cellCoordY * self.cellHeight)], 
                    fill = self.cellBorderColor, 
                    width = 0
                )
                imageDraw.line(
                    [((cellCoordX+1) * self.cellWidth - 1, cellCoordY * self.cellHeight), ((cellCoordX+1) * self.cellWidth - 1, (cellCoordY+1) * self.cellHeight - 1)], 
                    fill = self.cellBorderColor, 
                    width = 0
                )
                imageDraw.line(
                    [((cellCoordX+1) * self.cellWidth - 1, (cellCoordY+1) * self.cellHeight - 1), (cellCoordX * self.cellWidth, (cellCoordY+1) * self.cellHeight - 1)], 
                    fill = self.cellBorderColor, 
                    width = 0
                )
                imageDraw.line(
                    [(cellCoordX * self.cellWidth, (cellCoordY+1) * self.cellHeight - 1), (cellCoordX * self.cellWidth, cellCoordY * self.cellHeight)], 
                    fill = self.cellBorderColor, 
                    width = 0
                )

        return image


    def _drawV(self, image):

        imageDraw = ImageDraw.Draw(image)

        # Draw V levels
        for cellCoordX in range(self.gridworld.gridWidth):
            for cellCoordY in range(self.gridworld.gridHeight):

                Vstate = self.gridworld.agent.V((cellCoordX, cellCoordY)) # Vstate := V(state)
                # Vstate = math.log(1 + Vstate)
                Vstate = math.sqrt(Vstate)
                cellColor = tuple([int(a*Vstate + b * (1-Vstate)) for (a, b) in zip(self.highestVColor, self.emptyCellColor)])

                imageDraw.rectangle(
                    [
                        (cellCoordX * self.cellWidth, cellCoordY * self.cellHeight), 
                        ((cellCoordX+1) * self.cellWidth-1, (cellCoordY+1) * self.cellHeight-1), 
                    ], 
                    cellColor
                )

        return image


    def _drawQArrows(self, image):

        imageDraw = ImageDraw.Draw(image)

        # Design of top arrow. This design is rotated for the other arrows (right, bottom and left arrows).
        startXShift = 0.3
        startYShift = 0.20
        sideXShift = 0.1
        sideYShift = 0.1
        arrows = {}
        arrows["UP"] = {}
        arrows["UP"]["start"] = (startXShift * self.cellWidth, startYShift * self.cellHeight)
        arrows["UP"]["point"] = (startXShift * self.cellWidth, -startYShift * self.cellHeight)
        arrows["UP"]["side1"] = ((startXShift - sideXShift) * self.cellWidth, (startYShift - sideYShift) * self.cellHeight)
        arrows["UP"]["side2"] = ((startXShift + sideXShift) * self.cellWidth, (startYShift - sideYShift) * self.cellHeight)

        def rotate(coord, angle_deg):
            # [x', y'] = [cos  sin] |x|
            #            [-sin cos] |y|
            x = coord[0]
            y = coord[1]
            angle_rad = 3.1415 * angle_deg / 180
            cos = math.cos(angle_rad)
            sin = math.sin(angle_rad)
            rotatedCoords = [cos * x + sin * y, -sin * x + cos * y]
            rotatedCoords = [round(rotatedCoords[0], 2), round(rotatedCoords[1], 2)]
            return rotatedCoords

        def rotateArrow(arrow, angle_deg):
            result = {}
            for key in arrow.keys():
                result[key] = rotate(arrow[key], angle_deg)
            return result

        def addToArrow(arrow, coord):
            for key in arrow.keys():
                arrow[key] = [arrowCoord + extCoord for arrowCoord, extCoord in zip(arrow[key], coord)]

        arrows["LEFT"] = rotateArrow(arrows["UP"], 90)
        addToArrow(arrows["LEFT"], (0, self.cellHeight))

        arrows["DOWN"] = rotateArrow(arrows["UP"], 180)
        addToArrow(arrows["DOWN"], (self.cellWidth, self.cellHeight))

        arrows["RIGHT"] = rotateArrow(arrows["UP"], 270)
        addToArrow(arrows["RIGHT"], (self.cellWidth, 0))

        # Draw Q arrows
        for cellCoordX in range(self.gridworld.gridWidth):
            for cellCoordY in range(self.gridworld.gridHeight):
                state = (cellCoordX, cellCoordY)
                
                topLeftCoord = (cellCoordX * self.cellWidth, cellCoordY * self.cellHeight)

                for action in self.gridworld.possibleActions(state):
                    stateActionValue = self.gridworld.agent.Q(state, action) # Q(state, action)
                    stateActionValue = math.sqrt(stateActionValue)
                    arrowColor = tuple([int(a*stateActionValue + b * (1-stateActionValue)) for (a, b) in zip(self.highestVColor, self.emptyCellColor)])

                    # Compute 4 arrow points :
                    startCoord = tuple([arrowCoord + cellCoord for arrowCoord, cellCoord in zip(arrows[action]["start"], topLeftCoord)])
                    pointCoord = tuple([arrowCoord + cellCoord for arrowCoord, cellCoord in zip(arrows[action]["point"], topLeftCoord)])
                    sideCoord_1 = tuple([arrowCoord + cellCoord for arrowCoord, cellCoord in zip(arrows[action]["side1"], topLeftCoord)])
                    sideCoord_2 = tuple([arrowCoord + cellCoord for arrowCoord, cellCoord in zip(arrows[action]["side2"], topLeftCoord)])
                    # Draw arrow
                    imageDraw.line((startCoord, pointCoord, sideCoord_1, pointCoord, sideCoord_2), fill=arrowColor)

        return image


    def _drawPolicyArrows(self, image):

        imageDraw = ImageDraw.Draw(image)

        # Design of top arrow. This design is rotated for the other arrows (right, bottom and left arrows).
        startXShift = 0.5
        startYShift = 0.3
        sideXShift = 0.1
        sideYShift = 0.1
        arrows = {}
        arrows["UP"] = {}
        arrows["UP"]["start"] = (startXShift * self.cellWidth, (1-startYShift) * self.cellHeight)
        arrows["UP"]["point"] = (startXShift * self.cellWidth, startYShift * self.cellHeight)
        arrows["UP"]["side1"] = ((startXShift - sideXShift) * self.cellWidth, (startYShift + sideYShift) * self.cellHeight)
        arrows["UP"]["side2"] = ((startXShift + sideXShift) * self.cellWidth, (startYShift + sideYShift) * self.cellHeight)

        def rotate(coord, angle_deg):
            # [x', y'] = [cos  sin] |x|
            #            [-sin cos] |y|
            x = coord[0]
            y = coord[1]
            angle_rad = 3.1415 * angle_deg / 180
            cos = math.cos(angle_rad)
            sin = math.sin(angle_rad)
            rotatedCoords = [cos * x + sin * y, -sin * x + cos * y]
            rotatedCoords = [round(rotatedCoords[0], 2), round(rotatedCoords[1], 2)]
            return rotatedCoords

        def rotateArrow(arrow, angle_deg):
            result = {}
            for key in arrow.keys():
                result[key] = rotate(arrow[key], angle_deg)
            return result

        def addToArrow(arrow, coord):
            for key in arrow.keys():
                arrow[key] = [arrowCoord + extCoord for arrowCoord, extCoord in zip(arrow[key], coord)]

        arrows["LEFT"] = rotateArrow(arrows["UP"], 90)
        addToArrow(arrows["LEFT"], (0, self.cellHeight))

        arrows["DOWN"] = rotateArrow(arrows["UP"], 180)
        addToArrow(arrows["DOWN"], (self.cellWidth, self.cellHeight))

        arrows["RIGHT"] = rotateArrow(arrows["UP"], 270)
        addToArrow(arrows["RIGHT"], (self.cellWidth, 0))

        # Draw Q arrows
        for cellCoordX in range(self.gridworld.gridWidth):
            for cellCoordY in range(self.gridworld.gridHeight):
                state = (cellCoordX, cellCoordY)
                
                if (state in self.gridworld.obstacles):
                    continue

                topLeftCoord = (cellCoordX * self.cellWidth, cellCoordY * self.cellHeight)

                actionDistribution = self.gridworld.agent.policy(state)
                actionPair = actionDistribution[0]
                action = actionPair[0]

                arrowColor = (255, 255, 255)

                # Compute 4 arrow points :
                startCoord = tuple([arrowCoord + cellCoord for arrowCoord, cellCoord in zip(arrows[action]["start"], topLeftCoord)])
                pointCoord = tuple([arrowCoord + cellCoord for arrowCoord, cellCoord in zip(arrows[action]["point"], topLeftCoord)])
                sideCoord_1 = tuple([arrowCoord + cellCoord for arrowCoord, cellCoord in zip(arrows[action]["side1"], topLeftCoord)])
                sideCoord_2 = tuple([arrowCoord + cellCoord for arrowCoord, cellCoord in zip(arrows[action]["side2"], topLeftCoord)])
                # Draw arrow
                imageDraw.line((startCoord, pointCoord, sideCoord_1, pointCoord, sideCoord_2), fill=arrowColor)

        return image


