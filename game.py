import tkinter as tk
class game(tk.Canvas):
    def __init__(self,master, **kwargs):
        super().__init__(master, **kwargs)
        self.background = "#D2D2D2"
        self.width = 1280
        self.height =  720
        self.pack()
 
