#imports
from optparse import Values
from re import U
from tkinter import *
#guitar libary
GuitarButtonData =[
    {'row': 1, 'col': 0, 'value': "High-E string"},
    {'row': 2, 'col': 0, 'value': "B String"},
    {'row': 3, 'col': 0, 'value': "G String"},
    {'row': 4, 'col': 0, 'value': "D String"},
    {'row': 5, 'col': 0, 'value': "A String"},
    {'row': 6, 'col': 0, 'value': "Low-E String"}
]
    #import images
        #make strings
        #make backgroud
    #import sound files
    #make the gutiar class
#make varable for when you are/aren't using a pi
USING_RPI = False
#make gutiar gui class
class GuitarGUI(Frame):
    def __init__(self, master):  
        #import from frame class
        Frame.__init__(self, master, bg = 'orange')
        #make if statement for if you are using a pi
        if (USING_RPI):
            master.attributes('fullscreen', True)
        self.setUPGUI()
    #make def that sets the back ground color for each string
    def mGB(self, row, col, value):
        bgColor = 'white'
        if value == 'High-E string':
            bgColor = 'red'
        if value == 'B string':
            bgColor = 'orange'
        if value == 'G string':
            bgColor = 'yellow'
        if value == 'D string':
            bgColor = 'green'
        if value == 'A string':
            bgColor ='blue'
        if value == 'Low-E String':
            bgColor = 'indigo'
        #make button varible
        button = Button(
            self, 
            font = ('TextGyreAdventor', 25), 
            text = value,
            bg = bgColor, 
            #keep the function from running till it is pressed
            command = lambda: self.handleButtonPress(value)
        )
        #setting what the dictionarying place means
        button.gird(row = row, column = col, sticky = NSEW)
    
    def setUpGUI(self):
        #dislplay
        self.display = Label(self, text ='', anchor=E, bg='white', fg='black', height=1, font=(name, size))
        #manage geomiry (w/grid)
        self.display.grid(row=0, column=0, columnspan=4, sticky=NSEW)
        #configure rowns an coloums 
        for row in range(1,7):
            Grid.rowconfigure(self, row, weight = 1)
        for column in range(0,1):
            Grid.columconfigure(self, column, weight = 1)
        #create buttons
        for button in GuitarButtonData:
            self.nameButton(button['row'], button['col'], button['value'])
        #pack the GUI
        self.pack(fill = BOTH, expand = 1)
#piano libary
PianoButtonData = [
    {'row': 1, 'col': 0, 'value':'C'},
    {'row': 1, 'col': 1, 'value':'C'},
    {'row': 2, 'col': 1, 'value':'C'},

    {'row': 1, 'col': 1, 'value':'C#'},
    {'row': 1, 'col': 2, 'value':'C#'},

    {'row': 2, 'col': 2, 'value':'D'},
    {'row': 3, 'col': 0, 'value':'D'},
    {'row': 3, 'col': 1, 'value':'D'},
    {'row': 4, 'col': 1, 'value':'C'},

    {'row': 1, 'col': 0, 'value':'D#'},

    {'row': 1, 'col': 0, 'value':'E'},

    {'row': 1, 'col': 0, 'value':'F'},

    {'row': 1, 'col': 0, 'value':'F#'},

    {'row': 1, 'col': 0, 'value':'G'},

    {'row': 1, 'col': 0, 'value':'G#'},

    {'row': 1, 'col': 0, 'value':'A'},

    {'row': 1, 'col': 0, 'value':'A#'},

    {'row': 1, 'col': 0, 'value':'B'},
]
USING_RPI = False
class PianoGUI(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, bg = 'orange')
        if (USING_RPI):
            master.attributes('fullscreen', True)
        self.setUPGUI()
    def mGB(self, row, col, value):
        bgColor = 'white'
        if value == 'A':
            bgColor = 'red'
        if value == 'B':
            bgColor = 'orange'
        if value == 'C':
            bgColor = 'yellow'
        if value == 'D':
            bgColor = 'green'
        if value == 'E':
            bgColor ='blue'
        if value == 'F':
            bgColor = 'indigo'
        if value == 'G':
            bgColor = 'blue'

        button = Button(
            self, 
            font = ('TextGyreAdventor', 25), 
            text = value,
            bg = bgColor, 
            command = lambda: self.handleButtonPress(value)
        )

        button.gird(row = row, column = col, sticky = NSEW)
    
    def setUpGUI(self):
        #dislplay
        self.display = Label(self, text ='', anchor=E, bg='white', fg='black', height=1, font=(name, size))
        #manage geomiry (w/grid)
        self.display.grid(row=0, column=0, columnspan=4, sticky=NSEW)
        #configure rowns an coloums 
        for row in range(7):
            Grid.rowconfigure(self, row, weight = 1)
        for column in range(4):
            Grid.columconfigure(self, column, weight = 1)
        #create buttons
        for button in PianoButtonData:
            self.nameButton(button['row'], button['col'], button['value'])
        #pack the GUI
        self.pack(fill = BOTH, expand = 1)
    #import images
        #make piano keys
        #import background
    #import sound files
#durm libary
DrumButtonData = [
    #row 1
    {'row': 1, 'col': 0, 'value': 'x'},
    {'row': 1, 'col': 1, 'value': 'x'},
    {'row': 1, 'col': 2, 'value': 'x'},
    {'row': 1, 'col': 3, 'value': 'x'},
    {'row': 1, 'col': 5, 'value': 'x'},
    #row 2
    {'row': 2, 'col': 0, 'value': 'x'},
    {'row': 2, 'col': 1, 'value': 'x'},
    {'row': 2, 'col': 2, 'value': 'x'},
    {'row': 2, 'col': 3, 'value': 'x'},
    {'row': 2, 'col': 4, 'value': 'x'},
    #row 3
    {'row': 3, 'col': 0, 'value': 'x'},
    {'row': 3, 'col': 1, 'value': 'x'},
    {'row': 3, 'col': 2, 'value': 'x'},
    {'row': 3, 'col': 3, 'value': 'x'},
    {'row': 3, 'col': 4, 'value': 'x'},
    #row 4
    {'row': 4, 'col': 0, 'value': 'x'},
    {'row': 4, 'col': 1, 'value': 'x'},
    {'row': 4, 'col': 2, 'value': 'x'},
    {'row': 4, 'col': 3, 'value': 'x'},
    {'row': 4, 'col': 4, 'value': 'x'},
    #row 5
    {'row': 5, 'col': 0, 'value': 'x'},
    {'row': 5, 'col': 1, 'value': 'x'},
    {'row': 5, 'col': 2, 'value': 'x'},
    {'row': 5, 'col': 3, 'value': 'x'},
    {'row': 5, 'col': 4, 'value': 'x'}
]
USING_RPI = False
class DrumGUI(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, bg = 'orange')
        if (USING_RPI):
            master.attributes('fullscreen', True)
        self.setUPGUI()
    def mGB(self, row, col, value):
        bgColor = 'white'

        button = Button(
            self, 
            font = ('TextGyreAdventor', 25), 
            text = value,
            bg = bgColor, 
            command = lambda: self.handleButtonPress(value)
        )

        button.gird(row = row, column = col, sticky = NSEW)
    
    def setUpGUI(self):
        #dislplay
        self.display = Label(self, text ='', anchor=E, bg='white', fg='black', height=1, font=(name, size))
        #manage geomiry (w/grid)
        self.display.grid(row=0, column=0, columnspan=4, sticky=NSEW)
        #configure rowns an coloums 
        for row in range(7):
            Grid.rowconfigure(self, row, weight = 1)
        for column in range(4):
            Grid.columconfigure(self, column, weight = 1)
        #create buttons
        for button in DrumButtonData:
            self.nameButton(button['row'], button['col'], button['value'])
        #pack the GUI
        self.pack(fill = BOTH, expand = 1)
    #import images
        #make it a grid
        #make the lines and sqares diffent colors
    #import sound files

#make home page
#made drop-down menu

#record funtion

#playback funtion

#save function
    #have delete function

#main program
    #set up main page
        #set up GUI's for opening
        #set up drop down menu
            #images and sounds

#call funtions