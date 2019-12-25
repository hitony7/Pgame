from tkinter import Tk, Label, Button, Canvas, StringVar
from tkinter.ttk import Combobox
from Sqaure import sqaure
#36 ROWS and 64 COL
grids = [[0 for _ in range(36)] for _ in range(64)]
class main:
    def __init__(self, master):
        self.master = master

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

        self.startM = Button(master, text="Start Marker", command=self.greet)
        self.startM.place(x= 300, y= 15)

        self.endM = Button(master, text="End Marker", command=self.greet)
        self.endM.place(x= 400, y= 15)

        self.endM = Button(master, text="Draw", command=self.greet)
        self.endM.place(x= 500, y= 15)

        self.clearB = Button(master, text="Clear", command=self.greet)
        self.clearB.place(x= 600, y= 15)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.place(x= 1200, y= 15)


    def greet(self):
        print("Greetings!")

    def drawGrid(self,Canvas):
        #64 COl x  36 ROW
        sqaSize = 20 
        for c in range(64):
            for r in range(36):
                #Create Rect Parameters are (X0,y0,X1,Y1) (X0,Y0) Is top Left Corner (X1,Y1) Is Bottom Right Corner 
                Canvas.create_rectangle(c*sqaSize, r*sqaSize, (c+1)*sqaSize, (r+1)*sqaSize, tags="rec" + str(c) + "," + str(r),  fill = "#D2D2D2") 
                grids[c][r] = sqaure(c, r, wall = False, start = False, end = False)
                print(grids[c][r].getxy(),c ,"," , r)
                Canvas.tag_bind("rec" + str(c) + "," + str(r), '<ButtonPress-1>', self.onObjectClick) 
                Canvas.tag_bind("rec" + str(c) + "," + str(r), '<Enter>', self.onHover) 

    def onObjectClick(self,event):                  
        print('Got object click', event.x, event.y)
        print(event.widget.find_closest(event.x, event.y))
        item = event.widget.find_closest(event.x, event.y)
        tags = self.canvas1.gettags(item)
        print(tags)
        self.canvas1.itemconfig(event.widget.find_closest(event.x, event.y), fill="blue")# change color4
        #set data struct 
        #get tag of clicked object
        # change value of clicked object  

    def onHover(self,event):
        print(event.x, event.y)
        print(event.widget.find_closest(event.x, event.x))
        item = event.widget.find_closest(event.x, event.y)
        tags = self.canvas1.gettags(item)
        print(tags)
        #self.canvas1.itemconfig(event.widget.find_closest(event.x, event.y), fill="blue") # change color

root = Tk()
my_gui = main(root)
root.mainloop()

