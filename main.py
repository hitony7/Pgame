from tkinter import *
#using tkinter which use the concept of widgets

#This the root widget(The Window)
root = Tk()
root.title("Flappy Bird")
root.geometry("1280x720")
root.resizable(False, False)

#tkinter has 3 layout managers
#pack:  horizontal and vertical boxes
#grid: two dimensional grid
#place: absolute positioning

#function that handle button press
def startGame():
    print("Run Game")

def loadPic():
    print("Load Pic")

def exitGame():
    print("Exit")

windowWidth = 1280
windowheight = 720
ButtonWidth = 100 
ButtonHight = 50
#xpos get proper center consider the size of the button
xpos = (windowWidth/2) - (ButtonWidth/2)

startButton = Button(root, text = "Start Game", command=startGame)
startButton.place(height=ButtonHight, width=ButtonWidth, x=xpos, y=300)
loadButton = Button(root, text = "Load Picture", command=loadPic)
loadButton.place(height=ButtonHight, width=ButtonWidth, x=xpos, y= 400)
exitbutton= Button(root, text = "Exit",command=exitGame)
exitbutton.place(height=ButtonHight, width=ButtonWidth, x=xpos, y= 500)

 
root.mainloop()