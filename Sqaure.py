class sqaure:
    def __init__(self, x, y, wall, start, end):
        self.x = x 
        self.y = y
        self.wall = wall
        self.start = start
        self.end = end

    def getxy(self):
        return (self.x,self.y)
