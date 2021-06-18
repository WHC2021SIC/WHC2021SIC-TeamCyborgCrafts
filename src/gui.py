# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 21:11:08 2021

@author: hsbbd
"""

import tkinter as tk
from tkinter import ttk

  
 
LARGEFONT =("Verdana", 35)
  
class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Simple Prog")
         
        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Craft, Train, Train1, Train2, Games, Game1, Game2):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  
# first window frame startpage
  
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
         
        # label of frame Layout 2
        label = ttk.Label(self, text ="Welcome to VTTV", font = LARGEFONT)
         
        # putting the grid in its place by using
        # grid
        label.grid(row = 0, column = 0, padx = 10, pady = 10)
  
        button1 = ttk.Button(self, text ="Craft",
        command = lambda : controller.show_frame(Craft))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 0, padx = 10, pady = 10)
  
        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text ="Train",
        command = lambda : controller.show_frame(Train))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 0, padx = 10, pady = 10)
        
        button3 = ttk.Button(self, text ="Games",
        command = lambda : controller.show_frame(Games))
     
        # putting the button in its place by
        # using grid
        button3.grid(row = 3, column = 0, padx = 10, pady = 10)
  
  
          
  
  
# second window frame page1
class Craft(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
  
        label = ttk.Label(self, text ="Craft", font = LARGEFONT)
        label.grid(row = 0, column = 0, padx = 10, pady = 10)
        
        button3 = ttk.Button(self, text ="Home",
                            command = lambda : controller.show_frame(StartPage))
     
        # putting the button in its place by
        # using grid
        button3.grid(row = 1, column = 0, padx = 10, pady = 10)
  
  
  
# third window frame page2
class Train(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Numbers",
                            command = lambda : controller.show_frame(Train1))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 0, column = 0, padx = 10, pady = 10)
  
        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="Letters",
                            command = lambda : controller.show_frame(Train2))
        
        # putting the button in its place by
        # using grid
        button2.grid(row = 1, column = 0, padx = 10, pady = 10)
        
        button3 = ttk.Button(self, text ="Home",
                            command = lambda : controller.show_frame(StartPage))
     
        # putting the button in its place by
        # using grid
        button3.grid(row = 2, column = 0, padx = 10, pady = 10)
        
class Train1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
  
        label = ttk.Label(self, text ="Numbers", font = LARGEFONT)
        label.grid(row = 0, column = 0, padx = 10, pady = 10)
        
        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="Home",
                            command = lambda : controller.show_frame(StartPage))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 1, column = 0, padx = 10, pady = 10)
        
class Train2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
  
        label = ttk.Label(self, text ="Letters", font = LARGEFONT)
        label.grid(row = 0, column = 0, padx = 10, pady = 10)
        
        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="Home",
                            command = lambda : controller.show_frame(StartPage))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 1, column = 0, padx = 10, pady = 10)
        
        

class Games(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Whack a Mole",
                            command = lambda : controller.show_frame(Game1))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="Simon Vibes",
                            command = lambda : controller.show_frame(Game2))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
        
        button3 = ttk.Button(self, text ="Home",
                    command = lambda : controller.show_frame(StartPage))
     
        # putting the button in its place by
        # using grid
        button3.grid(row = 3, column = 1, padx = 10, pady = 10)
        
class Game1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
  
        label = ttk.Label(self, text ="Whack a Mole", font = LARGEFONT)
        label.grid(row = 0, column = 0, padx = 10, pady = 10)
        
        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="Home",
                            command = lambda : controller.show_frame(StartPage))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 1, column = 0, padx = 10, pady = 10)
  
class Game2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
  
        label = ttk.Label(self, text ="Simon Vibes", font = LARGEFONT)
        label.grid(row = 0, column = 0, padx = 10, pady = 10)
        
        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="Home",
                            command = lambda : controller.show_frame(StartPage))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 1, column = 0, padx = 10, pady = 10)
        
  
  
# Driver Code
app = tkinterApp()
app.mainloop()