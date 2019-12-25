from tkinter import Tk, Label, Button, Canvas, StringVar
from tkinter.ttk import Combobox
from Sqaure import sqaure
#36 ROWS and 64 COL
grids = [[0 for _ in range(36)] for _ in range(64)]
class main:
    def __init__(self, master):
        self.master = master
        #Default button booleans 
        self.startB = False
        self.endB   = False
        self.wallB  = True #Drawing Walls default
        #Null Value of Grid for no start and end markers
        self.lastStartxy = (-1,-1) 
        self.lastEndxy = (-1,-1)
        master.title("A simple GUI")
        master.geometry("1280x820")
        master.resizable(False, False)
        
        self.canvas1 = Canvas(master, background = "#D2D2D2",
                                            width = 1280, height =  720)
        self.canvas1.place(y = 50)
        self.drawGrid(self.canvas1)

        self.label = Label(master, text="This is our first GUI!")
        self.label.place(x= 100, y= 15)

        w = Combobox(master, values=[
                                    "Dijkstra's algorithm", 
                                    "A* algorithm",
                                    "March",
                                    "April"])
        w.current(0)
        print(w.current(), w.get())
        w.place(x= 900, y= 15)

        #Input Buttons
        self.greet_button = Button(master, text="Find Path", command=self.greet)
        self.greet_button.place(x= 800, y= 15)

        self.startM = Button(master, text="Start Marker", command=self.startMode)
        self.startM.place(x= 300, y= 15)

        self.endM = Button(master, text="End Marker", command=self.endMode)
        self.endM.place(x= 400, y= 15)

        self.drawM = Button(master, text="Draw", command=self.wallMode)
        self.drawM.place(x= 500, y= 15)

        self.clearB = Button(master, text="Clear", command=self.greet)
        self.clearB.place(x= 600, y= 15)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.place(x= 1200, y= 15)


    def greet(self):
        print("Greetings!")

    #Change of Booleans when Button is Clicked
    def startMode(self):
        print("start")
        self.startB = True
        self.wallB = False
        self.endB  = False

    def endMode(self):
        print("END")
        self.startB = False
        self.wallB = False
        self.endB  = True

    def wallMode(self):
        self.startB = False
        self.wallB = True
        self.endB  = False

    def drawGrid(self,Canvas):
        #64 COl x  36 ROW
        sqaSize = 20 
        for c in range(64):
            for r in range(36):
                #Create Rect Parameters are (X0,y0,X1,Y1) (X0,Y0) Is top Left Corner (X1,Y1) Is Bottom Right Corner 
                Canvas.create_rectangle(c*sqaSize, r*sqaSize, (c+1)*sqaSize, (r+1)*sqaSize, tags="rec:" + str(c) + "," + str(r),  fill = "#D2D2D2") 
                grids[c][r] = sqaure(c, r, wall = False, start = False, end = False)
                print(grids[c][r].getxy(),c ,"," , r)
                Canvas.tag_bind("rec:" + str(c) + "," + str(r), '<ButtonPress-1>', self.onObjectClick) 
                Canvas.tag_bind("rec:" + str(c) + "," + str(r), '<Enter>', self.onHover) 

    def onObjectClick(self,event):                  
        print('Got object click', event.x, event.y)
        print(event.widget.find_closest(event.x, event.y))
        item = event.widget.find_closest(event.x, event.y)
        tag = self.canvas1.gettags(item)
        print(tag)
        #get tag of clicked object
        xy = self.stringSpliter(tag)
        x = int(xy[0])
        y = int(xy[1])
        # change value of clicked object depending on what boolean button is true
        if(self.wallB):
            if(grids[x][y].start == True):
                self.lastStartxy = (-1,-1) 
            if(grids[x][y].end == True):
                self.lastEndxy = (-1,-1) 
            self.canvas1.itemconfig(event.widget.find_closest(event.x, event.y), fill="Black")# change color 
            grids[x][y].wall = True
            grids[x][y].start = False
            grids[x][y].end  = False
        elif(self.startB):
            if(grids[x][y].end == True):
                self.lastEndxy = (-1,-1) 
            #if Start Mark is placed the remove the last start marker
            if(self.lastStartxy != (-1,-1)):        #No need to replace if no start marker
                laststartx = self.lastStartxy[0]    #Get x from tuple
                laststarty = self.lastStartxy[1]    #Get y from tuple
                #Set previous startBlock to old color and reset booleans so square object is blank  
                self.canvas1.itemconfig(event.widget.find_withtag("rec:" + str(laststartx) + "," + str(laststarty)), fill="#D2D2D2") 
            self.canvas1.itemconfig(event.widget.find_closest(event.x, event.y), fill="Red")# change color
            grids[x][y].start = True
            grids[x][y].wall = False
            grids[x][y].end  = False
            self.lastStartxy = (x, y) 
            print(self.lastStartxy)
        elif(self.endB):
            if(grids[x][y].start == True):
                self.lastStartxy = (-1,-1) 
            #if end Mark is placed the remove the last end marker
            if(self.lastEndxy != (-1,-1)):    #No need to replace if no end marker
                lastendx = self.lastEndxy[0]
                lastendy = self.lastEndxy[1]
                #Set previous startBlock to old color and reset boolean so square object is blank  
                self.canvas1.itemconfig(event.widget.find_withtag("rec:" + str(lastendx) + "," + str(lastendy)), fill="#D2D2D2")
                grids[lastendx][lastendy].resetB()
            self.canvas1.itemconfig(event.widget.find_closest(event.x, event.y), fill="Green")# change color
            grids[x][y].end = True
            grids[x][y].start = False
            grids[x][y].wall  = False
            self.lastEndxy = (x, y) 

        print(grids[x][y].toString())
    
    def stringSpliter(self,tag):
        tupleF = tag[0]             #ELEMENT 0 is TAG OF REC, ELEMEMENT 1 is Current 
        a = tupleF.rsplit(":")      #Split REC: part of tag 
        b = a[1].rsplit(",")        #Split X(ROW), Y(COL)
        return b                    #RETURN A LIST [X, Y]


    def onHover(self,event):
       # print(event.x, event.y)
       # print(event.widget.find_closest(event.x, event.x))
       #item = event.widget.find_closest(event.x, event.y)
      #  tags = self.canvas1.gettags(item)
       # print(tags)
       pass
        #self.canvas1.itemconfig(event.widget.find_closest(event.x, event.y), fill="blue") # change color

root = Tk()
my_gui = main(root)
root.mainloop()

