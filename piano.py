from tkinter import *
import tkinter as tk
class pianoGUI(Frame):
    def __init__(self, master) :
        Frame.__init__(self, master)
        # creating the piano keys
        # these are the big white ones
        self.button1 = Button(master, bg= "white", relief = "solid", width = 7, height = 11, text = "C", font = "Arial")
        self.button1.pack()
        self.button1.place(x=0, y=139)
        self.button2 = Button(master, bg= "white", relief = "solid", width = 7, height = 11, text = "D", font = "Arial")
        self.button2.pack()
        self.button2.place(x=85, y=139)
        self.button3 = Button(master, bg= "white", relief = "solid", width = 7, height = 11, text = "E", font = "Arial")
        self.button3.pack()
        self.button3.place(x=170, y=139)
        self.button4 = Button(master, bg= "white", relief = "solid", width = 7, height = 11, text = "F", font = "Arial")
        self.button4.pack()
        self.button4.place(x=255, y=139)
        self.button5 = Button(master, bg= "white", relief = "solid", width = 7, height = 11, text = "G", font = "Arial")
        self.button5.pack()
        self.button5.place(x=340, y=139)
        self.button6 = Button(master, bg= "white", relief = "solid", width = 7, height = 11, text = "A", font = "Arial")
        self.button6.pack()
        self.button6.place(x=425, y=139)
        self.button7 = Button(master, bg= "white", relief = "solid", width = 7, height = 11, text = "B", font = "Arial")
        self.button7.pack()
        self.button7.place(x=510, y=139)
        # these are the small black ones
        self.button1A = Button(master, bg = "black", width = 4, height = 9)
        self.button1A.pack()
        self.button1A.place(x=68, y=140)
        self.button2A = Button(master, bg = "black", width = 4, height = 9)
        self.button2A.pack()
        self.button2A.place(x=150, y=140)
        self.button3A = Button(master, bg = "black", width = 4, height = 9)
        self.button3A.pack()
        self.button3A.place(x=405, y=140)
        self.button4A = Button(master, bg = "black", width = 4, height = 9)
        self.button4A.pack()
        self.button4A.place(x=320, y=140)
        self.button4A = Button(master, bg = "black", width = 4, height = 9)
        self.button4A.pack()
        self.button4A.place(x=490, y=140)

        
window = Tk()
window.title = ("Piano")
#the geometry method sets the width and height for you. No need for width and height variable
window.geometry("600x400")
# if you see this, my title doesn't work help
g = pianoGUI(window)
window.mainloop()