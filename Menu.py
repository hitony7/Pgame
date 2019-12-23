from tkinter import Tk, Canvas, Frame, Button
from tkinter import BOTH, W, NW, SUNKEN, TOP, X, FLAT, LEFT

class Menu(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    #function that handle button press
    def initUI(self):
        self.parent.title("Layout Test")
        self.config(bg = '#F0F0F0')
        self.pack(fill = BOTH, expand = 1)
                #create canvas
        canvas1 = Canvas(self, relief = FLAT, background = "#D2D2D2",
                                            width = 1280, height =  720)
        canvas1.pack(side = TOP, anchor = NW, padx = 10, pady = 10)
        #add quit button

        windowWidth = 1280
        windowheight = 720
        ButtonWidth = 100 
        ButtonHight = 50
        #xpos get proper center consider the size of the button
        xpos = (windowWidth/2) - (ButtonWidth/2)

        startButton = Button(canvas1, text = "Start Game", command=startGame)
        startButton.place(height=ButtonHight, width=ButtonWidth, x=xpos, y=300)
        loadButton = Button(canvas1, text = "Load Picture", command=loadPic)
        loadButton.place(height=ButtonHight, width=ButtonWidth, x=xpos, y= 400)
        exitbutton= Button(canvas1, text = "Exit",command=exitGame)
        exitbutton.place(height=ButtonHight, width=ButtonWidth, x=xpos, y= 500)

#function that handle button press
def startGame():
    print("Run Game")
    
def loadPic():
    print("Load Pic")

def exitGame():
    print("Exit")



def main():
    root = Tk()
    root.geometry("1280x720")
    root.resizable(False, False)
    root.title('Flappy Bird')
    app = Menu(root)
    app.mainloop()

if __name__ == '__main__':
    main()