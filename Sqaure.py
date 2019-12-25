class sqaure:
    def __init__(self, x, y, wall, start, end):
        self.x = x 
        self.y = y
        self.wall = wall
        self.start = start
        self.end = end

    def getxy(self):
        return (self.x,self.y)

    def toString(self):
        return ("x=" + str(self.x) + "/y=" + str(self.y) + "/WALL=" + str(self.wall) +"/START=" + str(self.start) + "/END=" + str(self.end) )