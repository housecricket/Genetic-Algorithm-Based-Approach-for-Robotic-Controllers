''' 
for facing 
0 is north, 
1 is east,
2 is south, 
and 3 is west
'''
from world import World
class Robot:

    ''' Initalize a robot with controller '''
    def __init__(self, sensorActions, world, maxMoves):
        self.sensorActions = self.calcSensorActions(sensorActions)
        self.world = world
        startPos = self.world.getStartPosition()
        self.xPosition = startPos[0]
        self.yPosition = startPos[1]
        self.sensorVal = -1
        self.heading = 1
        self.maxMoves = maxMoves
        self.moves = 0
        self.route = []
        self.route.append(startPos)

    ''' Runs the robot's actions based on sensor inputs '''
    def run(self):
        while (True):
            self.moves += 1

            # Break if the robot stops moving
            if self.getNextAction() == 0:
                return
            
            # Break if we reach a maximum number of moves
            if self.moves > self.maxMoves:
                return

            # Run action
            self.makeNextAction()
    
    ''' Runs the next action '''
    def makeNextAction(self):
        # If move forward
        if self.getNextAction() == 1:
            currentX = self.xPosition
            currentY = self.yPosition

            # Move depending on current direction
            if 0 == self.heading:
                self.yPosition += -1
                if self.yPosition < 0:
                    self.yPosition = 0
            
            if 1 == self.heading:
                self.xPosition += 1
                if self.xPosition > self.world.getMaxX():
                    self.xPosition = self.world.getMaxX()

            if 2 == self.heading:
                self.yPosition += 1
                if self.yPosition > self.world.getMaxY():
                    self.yPosition = self.world.getMaxY()
            
            if 3 == self.heading:
                self.xPosition += -1
                if self.xPosition < 0:
                    self.xPosition = 0

            # We can't move here
            if (self.world.isWall(self.xPosition, self.yPosition) == True):
                self.xPosition = currentX
                self.yPosition = currentY

            else:
                if (currentX != self.xPosition | currentY != self.yPosition):
                    self.route.append(self.getPosition())
        elif self.getNextAction == 2:
            if 0 == self.heading:
                self.heading = 1
            elif 1 == self.heading:
                self.heading = 2
            elif 2 == self.heading:
                self.heading = 3
            elif 3 == self.heading:
                self.heading = 0
        
        elif self.getNextAction == 3:
            if 0 == self.heading:
                self.heading = 3
            elif 1 == self.heading:
                self.heading = 0
            elif 2 == self.heading:
                self.heading = 1
            elif 3 == self.heading:
                self.heading = 2

        # Reset sensor value
        self.sensorVal = -1
                
    ''' Get next action depending on sensor mapping '''
    def getNextAction(self):
        return self.sensorActions[self.getSensorValue()]

    def getSensorValue(self):
        # If sensor value has already been calculated
        if self.sensorVal > -1:
            return self.sensorVal

        frontSensor = frontLeftSensor = frontRightSensor = leftSensor = rightSensor = backSensor = False

        # Find which sensors have been activated
        if self.getHeading() == 0:
            frontSensor = self.world.isWall(self.xPosition, self.yPosition-1)
            frontLeftSensor = self.world.isWall(self.xPosition-1, self.yPosition-1)
            frontRightSensor = self.world.isWall(self.xPosition+1, self.yPosition-1)
            leftSensor = self.world.isWall(self.xPosition-1, self.yPosition)
            rightSensor = self.world.isWall(self.xPosition+1, self.yPosition)
            backSensor = self.world.isWall(self.xPosition, self.yPosition+1)
        elif self.getHeading() == 1:
            frontSensor = self.world.isWall(self.xPosition+1, self.yPosition)
            frontLeftSensor = self.world.isWall(self.xPosition+1, self.yPosition-1)
            frontRightSensor = self.world.isWall(self.xPosition+1, self.yPosition+1)
            leftSensor = self.world.isWall(self.xPosition, self.yPosition-1)
            rightSensor = self.world.isWall(self.xPosition, self.yPosition+1)
            backSensor = self.world.isWall(self.xPosition-1, self.yPosition)
        elif self.getHeading() == 2:
            frontSensor = self.world.isWall(self.xPosition, self.yPosition+1)
            frontLeftSensor = self.world.isWall(self.xPosition+1, self.yPosition+1)
            frontRightSensor = self.world.isWall(self.xPosition-1, self.yPosition+1)
            leftSensor = self.world.isWall(self.xPosition+1, self.yPosition)
            rightSensor = self.world.isWall(self.xPosition-1, self.yPosition)
            backSensor = self.world.isWall(self.xPosition, self.yPosition-1)
        else:
            frontSensor = self.world.isWall(self.xPosition-1, self.yPosition)
            frontLeftSensor = self.world.isWall(self.xPosition-1, self.yPosition+1)
            frontRightSensor = self.world.isWall(self.xPosition-1, self.yPosition-1)
            leftSensor = self.world.isWall(self.xPosition, self.yPosition+1)
            rightSensor = self.world.isWall(self.xPosition, self.yPosition-1)
            backSensor = self.world.isWall(self.xPosition+1, self.yPosition)

        # Calculate sensor value
        sensorVal = 0
        if frontSensor == True:
            sensorVal += 1
        if frontLeftSensor == True:
            sensorVal += 2
        if frontRightSensor == True:
            sensorVal += 4
        if leftSensor == True:
            sensorVal += 8
        if rightSensor == True:
            sensorVal += 16
        if backSensor == True:
            sensorVal += 32
        self.sensorVal = sensorVal
        return sensorVal

        
    ''' Map robot's sensor data to actions from binary string '''
    def calcSensorActions(self, sensorActionsStr):
        # How many actions are there?
        numActions = int(len(sensorActionsStr)/2)
        sensorActions = [None] * numActions

        # Loop through actions
        for sensorValue in range(numActions):
            # Get sensor action
            sensorAction = 0
            if sensorActionsStr[sensorValue*2] == 1:
                sensorAction += 2
            if sensorActionsStr[sensorValue*2+1] == 1:
                sensorAction += 1
            # Add to sensor-action map
            sensorActions[sensorValue] = sensorAction

        return sensorActions

    ''' Get robot's position '''
    def getPosition(self):
        return [self.xPosition, self.yPosition]

    ''' Get robot's heading '''
    def getHeading(self):
        return self.heading

    ''' Returns robot's complete route around the maze '''
    def getRoute(self):
        return self.route

    ''' Returns route in printable format '''
    def printRoute(self):
        route = ""
        for routeStep in self.route:
            step = [None] * routeStep
            route += "{" + step[0] + "," + step[1] + "}"
        return route