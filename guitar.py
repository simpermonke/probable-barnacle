import tkinter as tk
from tkinter import *
# declaring the guitar class 
class guitarGUI(Frame): # inherits from the Frame class
    def __init__(self, master) :
        Frame.__init__(self, master)
        # declaring all the buttons
        # I've set x and y coordinates for buttons 1-6. This is how to move buttons around.
        self.button1 = Button(master, bg = "red", width = 150)
        self.button1.pack()
        self.button1.place(x= 0, y = 0)
        self.button2 = Button(master, bg = "orange", width = 150)
        self.button2.pack()
        self.button2.place(x= 0, y = 55)
        self.button3 = Button(master, bg = "yellow", width = 150)
        self.button3.pack()
        self.button3.place(x= 0, y = 110)
        self.button4 = Button(master, bg = "green", width = 150)
        self.button4.pack()
        self.button4.place(x= 0, y = 165)
        self.button5 = Button(master, bg = "blue", width = 150)
        self.button5.pack()
        self.button5.place(x= 0, y = 220)
        self.button6 = Button(master, bg = "purple", width = 150)
        self.button6.pack()
        self.button6.place(x= 0, y = 275)
window = Tk()
#the geometry method sets the width and height for you. No need for width and height variables.
window.geometry("800x300")
# if you see this, my title doesn't work help
window.title = ('Guitar')
g = guitarGUI(window)
window.mainloop()
