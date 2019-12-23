from tkinter import Tk, Label, Button, Canvas
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
        self.label.place(x= 100, y= 25)

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.place(x= 200, y= 25)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.place(x= 300, y= 25)


    def greet(self):
        print("Greetings!")

    def drawGrid(self,Canvas):
        #64 R x 90 C 7
        sqaSize = 20 
        for c in range(64):
            for r in range(36):
                print(r,c)
                #Create Rect Parameters are (X0,y0,X1,Y1) (X0,Y0) Is top Left Corner (X1,Y1) Is Bottom Right Corner 
                Canvas.create_rectangle(c*sqaSize, r*sqaSize, (c+1)*sqaSize, (r+1)*sqaSize)
              # Canvas.create_rectangle(r, c, r*sqaSize, c*sqaSize)
                


root = Tk()
my_gui = main(root)
root.mainloop()

