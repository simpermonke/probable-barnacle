from tkinter import *
import tkinter as tk
import pygame
import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

led2 = 13
led3 = 12
led4 = 6
led5 = 5
led6 = 8 #CEO
led8 = 9 #MISO
led9 = 20
led10 = 21
led11 = 22
led12 = 23
led13 = 24
led14 = 25
led15 = 26
led16 = 27
led17 = 18
led18 = 19
led19 = 7 #CE1
led20 = 10 #MOSI
led21 = 11 #SCLK
led22 = 15 #RX
led23 = 3 #SCL
led24 = 2 #SDA
led25 = 0 #ID_SD
led26 = 1 #ID_SC
led27 = 4
led28 = 14 #TX
led29 = 16



pygame.init()
root = tk.Tk()
root.title("The Blazin' Chords")
root.geometry('700x350')
root.configure(background='dark blue')

#start of the gutiar
randombox = Button(bg = "white", width = 65, height = 11)
randombox.pack()
randombox.place(x=120, y=0)

def ledon():
    sound1 = pygame.mixer.Sound("GuitarHighE.wav")
    guitarHighstring = pygame.mixer.Sound.play(sound1)
    e = [19, 11, 16]
    GPIO.setup(e, GPIO.OUT)
    GPIO.output(e, GPIO.HIGH)
    sleep (0.5)
    GPIO.output(e, GPIO.LOW)
    sleep(0.5)
        
guitarstring1 = lambda: ledon()
gutiarstring1 = Button(bg = "#FF0000", width = 60, height = 1, text="e", fg = "white", command = guitarstring1)
gutiarstring1.pack()

def ledon2():
    sound2 = pygame.mixer.Sound("GuitarBString.wav")
    guitarstring2 = pygame.mixer.Sound.play(sound2)
    b = [20,15,13]
    GPIO.setup(b, GPIO.OUT)
    GPIO.output(b, GPIO.HIGH)
    sleep (0.5)
    GPIO.output(b, GPIO.LOW)
    sleep(0.5)

bstringsound = lambda: ledon2()
gutiarstring2 = Button(bg = "#FF1212", width = 60, height = 1, text = "b", fg = "white", command = bstringsound)
gutiarstring2.pack()


def ledon3():
    sound3 = pygame.mixer.Sound("GuitarGString.wav")
    guitarstring3 = pygame.mixer.Sound.play(sound3)
    g = [21, 14, 12]
    GPIO.setup(g, GPIO.OUT)
    GPIO.output(g, GPIO.HIGH)
    sleep (0.5)
    GPIO.output(g, GPIO.LOW)
    sleep(0.5)


gstringnote = lambda: ledon3()
gutiarstring3 = Button(bg = "#FF3636", width = 60, height = 1, text = "g", fg = "white", command = gstringnote)
gutiarstring3.pack()

def ledon4():
    sound4 = pygame.mixer.Sound("GuitarDString.wav")
    guitarstring4 = pygame.mixer.Sound.play(sound4)
    d = [22, 27, 6]
    GPIO.setup(d, GPIO.OUT)
    GPIO.output(d, GPIO.HIGH)
    sleep (0.5)
    GPIO.output(d, GPIO.LOW)
    sleep(0.5)


dstringnote = lambda: ledon4()
gutiarstring4 = Button(bg = "#FF5151", width = 60, height = 1, text = "d", fg = "white", command = dstringnote)
gutiarstring4.pack()


def ledon5():
    sound5 = pygame.mixer.Sound("GuitarAString.wav")
    guitarstring5 = pygame.mixer.Sound.play(sound5)
    a = [23, 3, 5]
    GPIO.setup(a, GPIO.OUT)
    GPIO.output(a, GPIO.HIGH)
    sleep (0.5)
    GPIO.output(a, GPIO.LOW)
    sleep(0.5)

astringnote = lambda: ledon5()
gutiarstring5 = Button(bg = "#FF6666", width = 60, height = 1, text = "a", fg = "white", command = astringnote)
gutiarstring5.pack()

def ledon6():
    sound6 = pygame.mixer.Sound("GuitarLow-E.wav")
    guitarstring6 = pygame.mixer.Sound.play(sound6)
    E = [24, 2, 4]
    GPIO.setup(E, GPIO.OUT)
    GPIO.output(E, GPIO.HIGH)
    sleep (0.5)
    GPIO.output(E, GPIO.LOW)
    sleep(0.5)

estringnote = lambda: ledon6()
gutiarstring6 = Button(bg = "#FF7575", width = 60, height = 1, text = "E", fg = "white", command = estringnote)  
gutiarstring6.pack()


randombox1 = Button(bg = "black", width = 60, height = 9)
randombox1.pack()
randombox1.place(x=136, y=220)


def lightOn1():
    note1 = pygame.mixer.Sound("cNote.wav")
    button1 = pygame.mixer.Sound.play(note1)
    whitekeys = [1, 2, 4, 5, 6, 7, 8, 10, 11, 12, 13, 16, 17, 19, 18, 20, 21, 22, 23, 24, 25, 26]
    GPIO.setup(whitekeys, GPIO.OUT)
    GPIO.output(whitekeys, GPIO.HIGH)
    sleep (0.5)
    GPIO.output(whitekeys, GPIO.LOW)
    sleep(0.5)
    

cnotesound = lambda: lightOn1()
button1 = Button(bg= "white", relief = "solid", width = 5, height = 6, text = "C", font = "Arial", command = cnotesound)
button1.pack()
button1.place(x=165, y=250)

def lightOn2():
    note2 = pygame.mixer.Sound("dNote.wav")
    button2 = pygame.mixer.Sound.play(note2)
    whitekeys = [1, 2, 4, 5, 6, 7, 8, 10, 11, 12, 13, 16, 17, 19, 18, 20, 21, 22, 23, 24, 25, 26]
    GPIO.setup(whitekeys, GPIO.OUT)
    GPIO.output(whitekeys, GPIO.HIGH)
    sleep (0.5)
    GPIO.output(whitekeys, GPIO.LOW)
    sleep(0.5)

dnotesound = lambda: lightOn2()
button2 = Button(bg= "white", relief = "solid", width = 5, height = 6, text = "D", font = "Arial", command = dnotesound)
button2.pack()
button2.place(x=218, y=250)

def lightOn3():
    note3 = pygame.mixer.Sound("eNote.wav")
    button3 = pygame.mixer.Sound.play(note3)
    whitekeys = [1, 2, 4, 5, 6, 7, 8, 10, 11, 12, 13, 16, 17, 19, 18, 20, 21, 22, 23, 24, 25, 26]
    GPIO.setup(whitekeys, GPIO.OUT)
    GPIO.output(whitekeys, GPIO.HIGH)
    sleep (0.5)
    GPIO.output(whitekeys, GPIO.LOW)
    sleep(0.5)

enotesound = lambda: lightOn3()
button3 = Button(bg= "white", relief = "solid", width = 5, height = 6, text = "E", font = "Arial", command = enotesound)
button3.pack()
button3.place(x=271, y=250)

def lightOn4():
    note4 = pygame.mixer.Sound("fNote.wav")
    button4 = pygame.mixer.Sound.play(note4)
    whitekeys = [1, 2, 4, 5, 6, 7, 8, 10, 11, 12, 13, 16, 17, 19, 18, 20, 21, 22, 23, 24, 25, 26]
    GPIO.setup(whitekeys, GPIO.OUT)
    GPIO.output(whitekeys, GPIO.HIGH)
    sleep (0.5)
    GPIO.output(whitekeys, GPIO.LOW)
    sleep(0.5)

fnotesound = lambda: lightOn4()
button4 = Button(bg= "white", relief = "solid", width = 5, height = 6, text = "F", font = "Arial", command = fnotesound)
button4.pack()
button4.place(x=324, y=250)

def lightOn5():
    note5 = pygame.mixer.Sound("gNote.wav")
    button5 = pygame.mixer.Sound.play(note5)
    whitekeys = [1, 2, 4, 5, 6, 7, 8, 10, 11, 12, 13, 16, 17, 19, 18, 20, 21, 22, 23, 24, 25, 26]
    GPIO.setup(whitekeys, GPIO.OUT)
    GPIO.output(whitekeys, GPIO.HIGH)
    sleep (0.5)
    GPIO.output(whitekeys, GPIO.LOW)
    sleep(0.5)

gnotesound = lambda: lightOn5()
button5 = Button(bg= "white", relief = "solid", width = 5, height = 6, text = "G", font = "Arial", command = gnotesound)
button5.pack()
button5.place(x=377, y=250)

def lightOn6():
    note6 = pygame.mixer.Sound("aNote.wav")
    button6 = pygame.mixer.Sound.play(note6)
    whitekeys = [1, 2, 4, 5, 6, 7, 8, 10, 11, 12, 13, 16, 17, 19, 18, 20, 21, 22, 23, 24, 25, 26]
    GPIO.setup(whitekeys, GPIO.OUT)
    GPIO.output(whitekeys, GPIO.HIGH)
    sleep (0.5)
    GPIO.output(whitekeys, GPIO.LOW)
    sleep(0.5)

anotesound = lambda: lightOn6()
button6 = Button(bg= "white", relief = "solid", width = 5, height = 6, text = "A", font = "Arial", command = anotesound)
button6.pack()
button6.place(x=430, y=250)

def lightOn7():
    note7 = pygame.mixer.Sound("bNote.wav")
    button7 = pygame.mixer.Sound.play(note7)
    whitekeys = [1, 2, 4, 5, 6, 7, 8, 10, 11, 12, 13, 16, 17, 19, 18, 20, 21, 22, 23, 24, 25, 26]
    GPIO.setup(whitekeys, GPIO.OUT)
    GPIO.output(whitekeys, GPIO.HIGH)
    sleep (0.5)
    GPIO.output(whitekeys, GPIO.LOW)
    sleep(0.5)

bnotesound = lambda: lightOn7()
button7 = Button(bg= "white", relief = "solid", width = 5, height = 6, text = "B", font = "Arial", command = bnotesound)
button7.pack()
button7.place(x=483, y=250)
# these are the small black ones


def lightOn8():
    sharp1 = pygame.mixer.Sound("PianoCSharp.wav")
    button1A = pygame.mixer.Sound.play(sharp1)
    blackkeys = [3, 27, 14, 15, 11, 9]
    GPIO.setup(blackkeys, GPIO.OUT)
    GPIO.output(blackkeys, GPIO.HIGH)
    sleep (0.5)
    GPIO.output(blackkeys, GPIO.LOW)
    sleep(0.5)

csharpsound = lambda: lightOn8()
button1A = Button(bg = "black", width = 2, height = 3, text = "C#", font = "Arial", fg = "white", command = csharpsound)
button1A.pack()
button1A.place(x=207, y=250)


def lightOn9():
    sharp2 = pygame.mixer.Sound("d.wav")
    button2A = pygame.mixer.Sound.play(sharp2)
    blackkeys = [3, 27, 14, 15, 11, 9]
    GPIO.setup(blackkeys, GPIO.OUT)
    GPIO.output(blackkeys, GPIO.HIGH)
    sleep (0.5)
    GPIO.output(blackkeys, GPIO.LOW)
    sleep(0.5)

dsharpsound = lambda: lightOn9()
button2A = Button(bg = "black", width = 2, height = 3, text = "D#", font = "Arial", fg = "white", command = dsharpsound)
button2A.pack()
button2A.place(x=260, y=250)

def lightOn10():
    sharp3 = pygame.mixer.Sound("f.wav")
    button3A = pygame.mixer.Sound.play(sharp3)
    blackkeys = [3, 27, 14, 15, 11, 9]
    GPIO.setup(blackkeys, GPIO.OUT)
    GPIO.output(blackkeys, GPIO.HIGH)
    sleep (0.5)
    GPIO.output(blackkeys, GPIO.LOW)
    sleep(0.5)

fsharpsound = lambda: lightOn10()
button3A = Button(bg = "black", width = 2, height = 3, text = "F#", font = "Arial", fg = "white", command = fsharpsound)
button3A.pack()
button3A.place(x=420, y=250)


def lightOn11():
    sharp4 = pygame.mixer.Sound("g.wav")
    button4A = pygame.mixer.Sound.play(sharp4)
    blackkeys = [3, 27, 14, 15, 11, 9]
    GPIO.setup(blackkeys, GPIO.OUT)
    GPIO.output(blackkeys, GPIO.HIGH)
    sleep (0.5)
    GPIO.output(blackkeys, GPIO.LOW)
    sleep(0.5)
    
gsharpsound = lambda: lightOn11()
button4A = Button(bg = "black", width = 2, height = 3, text = "G#", font = "Arial", fg = "white", command = gsharpsound)
button4A.pack()
button4A.place(x=365, y=250)

def lightOn12():
    sharp5 = pygame.mixer.Sound("a.wav")
    button5A = pygame.mixer.Sound.play(sharp5)
    blackkeys = [3, 27, 14, 15, 11, 9]
    GPIO.setup(blackkeys, GPIO.OUT)
    GPIO.output(blackkeys, GPIO.HIGH)
    sleep (0.5)
    GPIO.output(blackkeys, GPIO.LOW)
    sleep(0.5)

asharpsound = lambda: lightOn12()
button5A = Button(bg = "black", width = 2, height = 3, text = "A#", font = "Arial", fg = "white", command = asharpsound)
button5A.pack()
button5A.place(x=475, y=250)

#the drumpad


greybox = Button(bg = "grey", width = 9, height = 8 )
greybox.pack()
greybox.place(x = 690, y = 103)
greybox1 = Button(bg = "grey", width = 9, height = 8 )
greybox1.pack()
greybox1.place(x = 22, y = 103)


def drumpads1():
    snare1 = pygame.mixer.Sound("snare.wav")
    drumpad1 = pygame.mixer.Sound.play(snare1)
    drumkeys = [26, 1, 4, 18, 11, 13]
    GPIO.setup(drumkeys, GPIO.OUT)
    GPIO.output(drumkeys, GPIO.HIGH)
    sleep (0.5)
    GPIO.output(drumkeys, GPIO.LOW)
    sleep(0.5)

snaresound = lambda: drumpads1()
drumpad1 = Button(bg = "red", width = 5, height = 2, text = "snare", font = "Arial", fg = "white", command = snaresound)
drumpad1.pack()
drumpad1.place(x = 30, y = 120)


def drumpads2():
    cymbol1 = pygame.mixer.Sound("cymbol.wav")
    drumpad1 = pygame.mixer.Sound.play(cymbol1)
    drumkeys = [18, 9, 17, 26, 0, 8, 22, 27, 6]
    GPIO.setup(drumkeys, GPIO.OUT)
    GPIO.output(drumkeys, GPIO.HIGH)
    sleep (0.5)
    GPIO.output(drumkeys, GPIO.LOW)
    sleep(0.5)

cymbolsound = lambda: drumpads2()
drumpad3 = Button(bg = "white", width = 5, height = 2, text = "cymbol", font = "Arial", fg = "black", command = cymbolsound)
drumpad3.pack()
drumpad3.place(x = 700, y = 120)


def drumpads3():
    kick1 = pygame.mixer.Sound("21KICK.wav")
    drumpad2 = pygame.mixer.Sound.play(kick1)
    drumkeys = [20, 15, 13, 24, 2, 4, 22, 27, 6]
    GPIO.setup(drumkeys, GPIO.OUT)
    GPIO.output(drumkeys, GPIO.HIGH)
    sleep (0.5)
    GPIO.output(drumkeys, GPIO.LOW)
    sleep(0.5)

kicksound = lambda: drumpads3()
drumpad2 = Button(bg = "white", width = 5, height = 2, text = "kick", font = "Arial", fg = "black", command = kicksound)
drumpad2.pack()
drumpad2.place(x = 30, y = 170)

def drumpads4():
    drum1 = pygame.mixer.Sound("hitom.wav")
    drumpad4 = pygame.mixer.Sound.play(drum1)
    drumkeys = [21, 22, 23, 27, 12, 6, 5]
    GPIO.setup(drumkeys, GPIO.OUT)
    GPIO.output(drumkeys, GPIO.HIGH)
    sleep (0.5)
    GPIO.output(drumkeys, GPIO.LOW)
    sleep(0.5)

drumsound = lambda: drumpads4()
drumpad4 = Button(bg = "red", width = 5, height = 2, text = "drum", font = "Arial", fg = "white", command = drumsound)
drumpad4.pack()
drumpad4.place(x = 700, y = 170)


#playback button
playback = Button(bg = "grey", width = 7, height = 1, text = "playback", font = "Arial", fg = "black")
playback.pack()
playback.place(x = 680, y = 7)
record = Button(bg = "grey", width = 7, height = 1, text = "record", font = "Arial", fg = "black")
record.pack()
record.place(x = 9, y = 7)

root.mainloop()


