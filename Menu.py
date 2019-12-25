class sqaure:
    def __init__(self, x, y, wall, start, end):
        self.x = x 
        self.y = y
        self.wall = False
        self.start = False
        self.end = False 

    def getxy(self):
        return (self.x,self.y)

