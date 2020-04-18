


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
        self.goalColor = (50, 255, 50)
        
        self.cellBorderColor = (50, 50, 50)
        
        self.agentColor = (255, 255, 0)
        


    def draw(self):

        image = Image.new(
            'RGB', 
            (self.gridworld.gridWidth * self.cellWidth, self.gridworld.gridHeight * self.cellHeight), 
            self.emptyCellColor
        )

        image = self._drawGrid(image)

        image = self._drawAgent(image)
        
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





