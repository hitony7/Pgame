import tkinter as tk                # python 3
from tkinter import font as tkfont # python 3
import game as game    #Import game class

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.title("Flappy Bird")
        self.geometry("1280x720")
        self.resizable(False, False)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

                #create canvas
        canvas1 = tk.Canvas(self, background = "#D2D2D2",
                                            width = 1280, height =  720)
        canvas1.pack(padx = 10, pady = 10)
        #add quit button

        windowWidth = 1280
        windowheight = 720
        ButtonWidth = 100 
        ButtonHight = 50
        #xpos get proper center consider the size of the button
        xpos = (windowWidth/2) - (ButtonWidth/2)

        startButton = tk.Button(self, text = "Start Game", command=lambda: controller.show_frame("PageOne"))
        startButton.place(height=ButtonHight, width=ButtonWidth, x=xpos, y=300)
        loadButton = tk.Button(self, text = "Load Picture", command=lambda: controller.show_frame("PageTwo"))
        loadButton.place(height=ButtonHight, width=ButtonWidth, x=xpos, y= 400)
        exitbutton= tk.Button(self, text = "Exit",command=lambda: controller.show_frame("PageTwo"))
        exitbutton.place(height=ButtonHight, width=ButtonWidth, x=xpos, y= 500)



class PageOne(tk.Frame):
    import game as game    #Import game class
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        canvas1 = game
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()