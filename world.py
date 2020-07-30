class World(object):

    def __init__(self, world):
        self.startPosition = [-1, -1]
        self.world = world

    # Get start position of maze
    def getStartPosition(self):
        # Check we already found start position
        if self.startPosition[0] != -1 & self.startPosition[1] != -1:
            return self.startPosition

        # Default return value
        startPosition = [0, 0]

        # Loop over rows
        for rowIndex in range(len(self.world)):
            # Loop over columns
            for colIndex in range(len(self.world[rowIndex])):
                # 2 is the type for start position
                if self.world[rowIndex][colIndex] == 2:
                    self.startPosition = [colIndex, rowIndex]
                    return [colIndex, rowIndex]

    # Gets value for position of maze
    def getPositionValue(self, x, y):
        if (x < 0 or y < 0 or x >= len(self.world) or y >= len(self.world[0])):
            return 1
        return self.world[y][x]

    def printWorld(self):
        colNum = 0
        rowNum = 0
        for row in self.world:
            colNum = 0
            for char in row:
                print(char, '\t', end="")
                colNum += 1
            print('\n')
            rowNum += 1

    # Check if position is wall
    def isWall(self, x, y):
        return self.getPositionValue(x, y) == 1

    # Gets maximum index of x position
    def getMaxX(self):
        return len(self.world[0])-1

    # Gets maximum index of y position
    def getMaxY(self):
        return len(self.world)-1

    # Scores a maze route
    def scoreRoute(self, route):
        score = 0
        visited = [[False] * (self.getMaxY()+1)
                   for i in range(self.getMaxX()+1)]
        # Loop over route and score each move
        for routeStep in route:
            step = routeStep
            if (self.world[step[1]][step[0]] == 3 and visited[step[1]][step[0]] == False):
                # Increase score for correct move
                score += 1
                # Remove reward
                visited[step[1]][step[0]] = True
        return score
