from tkinter import *
import tkinter as tk

class drumGUI(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.button1 = Button(bg = "white", text = "base", font = "Arial", relief= "solid", width = 10, height = 5)
        self.button1.pack()
        self.button1.place(x =137, y = 0 )
        self.button2 = Button(bg = "red", text = "snap", font = "Arial", relief = "solid", width = 10, height = 5)
        self.button2.pack()
        self.button2.place(x = 22, y = 0)
        self.button3 = Button(bg = "orange", text = "kick", font = "Arial", relief = "solid", width = 10, height = 5)
        self.button3.pack()
        self.button3.place(x = 254, y = 0)
        self.button4 = Button(bg = "blue", text = "scratch", font = "Arial", relief = "solid", width = 10, height = 5)
        self.button4.pack()
        self.button4.place(x = 254, y = 130)
        self.button6 = Button(bg = "yellow", text = "clap", font = "Arial", relief = "solid", width = 10, height = 5)
        self.button6.pack()
        self.button6.place(x = 137, y = 130)
        self.button7 = Button(bg = "pink", text = "kick", font = "Arial", relief = "solid", width = 10, height = 5)
        self.button7.pack()
        self.button7.place(x = 137, y = 260)
        self.button8 = Button(bg = "purple", text = "snare", font = "Arial", relief = "solid", width = 10, height = 5)
        self.button8.pack()
        self.button8.place(x = 254, y = 260)
        self.button9 = Button(bg = "cyan", text = "cat", font = "Arial", relief = "solid", width = 10, height = 5)
        self.button9.pack()
        self.button9.place(x = 22, y = 260)
        self.button5 = Button(bg = "green", text = "dog", font = "Arial", relief = "solid", width = 10, height = 5)
        self.button5.pack()
        self.button5.place(x = 22, y = 130)

window = Tk()
window.geometry("400x400")
window.title("Drumpad")
d = drumGUI(window)
window.mainloop()