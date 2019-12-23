from tkinter import Tk, Label, Button, Canvas, StringVar
from tkinter.ttk import Combobox


class main:
    def __init__(self, master):
        self.master = master

        master.title("A simple GUI")
        master.geometry("1280x820")
        master.resizable(False, False)
        
        canvas1 = Canvas(master, background = "#D2D2D2",
                                            width = 1280, height =  720)
        canvas1.place(y = 50)
        self.drawGrid(canvas1)

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

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.place(x= 800, y= 15)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.place(x= 1200, y= 15)


    def greet(self):
        print("Greetings!")

    def drawGrid(self,Canvas):
        #64 R x 90 C 7
        sqaSize = 20 
        for c in range(64):
            for r in range(36):
                #Create Rect Parameters are (X0,y0,X1,Y1) (X0,Y0) Is top Left Corner (X1,Y1) Is Bottom Right Corner 
                Canvas.create_rectangle(c*sqaSize, r*sqaSize, (c+1)*sqaSize, (r+1)*sqaSize)
                


root = Tk()
my_gui = main(root)
root.mainloop()

