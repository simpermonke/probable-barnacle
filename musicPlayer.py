#imports
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
    #the C button
    {'row': 1, 'col': 0, 'value':'C'},
    {'row': 2, 'col': 0, 'value':'C'},
    {'row': 3, 'col': 0, 'value':'C'},
    {'row': 4, 'col': 0, 'value':'C'},
    {'row': 5, 'col': 0, 'value':'C'},
    #the c# button
    {'row': 1, 'col': 1, 'value':'C#'},
    {'row': 2, 'col': 1, 'value':'C#'},
    {'row': 3, 'col': 1, 'value':'C#'},
    #the D button
    {'row': 4, 'col': 1, 'value':'D'},
    {'row': 5, 'col': 1, 'value':'D'},
    {'row': 1, 'col': 2, 'value':'D'},
    {'row': 2, 'col': 2, 'value':'D'},
    {'row': 3, 'col': 2, 'value':'D'},
    {'row': 4, 'col': 2, 'value':'D'},
    {'row': 1, 'col': 2, 'value':'D'},
    #the D# button
    {'row': 1, 'col': 0, 'value':'D#'},
    {'row': 2, 'col': 1, 'value':'D#'},
    {'row': 3, 'col': 2, 'value':'D#'},
    #the E button
    {'row': 4, 'col': 3, 'value':'E'},
    {'row': 5, 'col': 4, 'value':'E'},
    #the F button
    {'row': 1, 'col': 4, 'value':'F'},
    {'row': 2, 'col': 4, 'value':'F'},
    {'row': 3, 'col': 4, 'value':'F'},
    {'row': 4, 'col': 4, 'value':'F'},
    {'row': 5, 'col': 4, 'value':'F'},
    {'row': 4, 'col': 5, 'value':'F'},
    {'row': 5, 'col': 5, 'value':'F'},
    #the F# button
    {'row': 1, 'col': 5, 'value':'F#'},
    {'row': 2, 'col': 5, 'value':'F#'},
    {'row': 3, 'col': 5, 'value':'F#'},
    #the G button
    {'row': 1, 'col': 6, 'value':'G'},
    {'row': 2, 'col': 6, 'value':'G'},
    {'row': 3, 'col': 6, 'value':'G'},
    {'row': 4, 'col': 6, 'value':'G'},
    {'row': 5, 'col': 6, 'value':'G'},
    #the G# button
    {'row': 1, 'col': 7, 'value':'G#'},
    {'row': 2, 'col': 7, 'value':'G#'},
    {'row': 3, 'col': 7, 'value':'G#'},
    #the A button
    {'row': 4, 'col': 7, 'value':'A'},
    {'row': 5, 'col': 7, 'value':'A'},
    {'row': 1, 'col': 8, 'value':'A'},
    {'row': 2, 'col': 8, 'value':'A'},
    {'row': 3, 'col': 8, 'value':'A'},
    {'row': 4, 'col': 8, 'value':'A'},
    {'row': 5, 'col': 8, 'value':'A'},
    #the A# button
    {'row': 1, 'col': 9, 'value':'A#'},
    {'row': 2, 'col': 9, 'value':'A#'},
    {'row': 3, 'col': 9, 'value':'A#'},
    #the B button
    {'row': 4, 'col': 9, 'value':'B'},
    {'row': 5, 'col': 9, 'value':'B'},
]
USING_RPI = False
class PianoGUI(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, bg = 'orange')
        if (USING_RPI):
            master.attributes('fullscreen', True)
        self.setUPGUI()
    def mGB(self, row, col, value):
        #set when the background color is what 
        bgColor = 'white'
        #seting it to white if it would be white on a regualr piano
        if value == ('A', 'B', 'C', 'D', 'E', 'F', 'G'):
            bgColor = 'white'
        #setting it to black if it would be on a regualr piano
        else: 
            bgColor = 'black'
        #making the button
        button = Button(
            self, 
            font = ('TextGyreAdventor', 25), 
            text = value,
            bg = bgColor, 
            command = lambda: self.handleButtonPress(value)
        )
        button.gird(row = row, column = col, sticky = NSEW)
    #setting up the gui
    def setUpGUI(self):
        #dislplay
        self.display = Label(self, text ='', anchor=E, bg='white', fg='grey', height=1, font=('name', 'size'))
        #manage geomiry (w/grid)
        self.display.grid(row=0, column=0, columnspan=4, sticky=NSEW)
        #configure rowns an coloums 
        for row in range(1, 5):
            Grid.rowconfigure(self, row, weight = 1)
        for column in range(0, 10):
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
    {'row': 1, 'col': 0, 'value': 'base'},
    {'row': 1, 'col': 1, 'value': 'snap'},
    {'row': 1, 'col': 2, 'value': 'clap'},
    #row 2
    {'row': 2, 'col': 0, 'value': 'kick'},
    {'row': 2, 'col': 1, 'value': 'snare'},
    {'row': 2, 'col': 2, 'value': 'tap'},
    #row 3
    {'row': 3, 'col': 0, 'value': 'cat'},
    {'row': 3, 'col': 1, 'value': 'dog'},
    {'row': 3, 'col': 2, 'value': 'scratch'}, 
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
        if value == 'base':
            bgColor = 'red'
        if value == 'snap':
            bgColor = 'orange'
        if value == 'kick':
            bgColor = 'orange'
        if value == 'clap':
            bgColor = 'yellow'
        if value == 'snare':
            bgColor = 'yellow'
        if value == 'cat':
            bgColor = 'yellow'
        if value == 'tap':
            bgColor = 'green'
        if value == 'dog':
            bgColor = 'green'
        if value == 'scratch':
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
        self.display = Label(self, text ='', anchor=E, bg='white', fg='black', height=1, font=('name', 'size'))
        #manage geomiry (w/grid)
        self.display.grid(row=0, column=0, columnspan=4, sticky=NSEW)
        #configure rowns an coloums 
        for row in range(1, 5):
            Grid.rowconfigure(self, row, weight = 1)
        for column in range(0, 5):
            Grid.columconfigure(self, column, weight = 1)
        #create buttons
        for button in DrumButtonData:
            self.nameButton(button['row'], button['col'], button['value'])
        #pack the GUI
        self.pack(fill = BOTH, expand = 1)
    def handelButtonPress(self, value):
        #make a loop function that makes it to where when the button is pressed, it is white
#sets the varible windo = to the tk function
window = Tk()
#gives the window a title
window.title("Drum Pad")
#sets a varible to call the function
r = DrumGUI(Frame)
#shows the image
window.mainloop()
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