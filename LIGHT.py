import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
outpins = [17,16]
#led = 17
#led1 = 16
led2 = 13
led3 = 12
led4 = 6
led5 = 5
led6 = 8 #CE0
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

#Light Pattern for Drum Pad
AA = [18,19,20]
AB = [21, 22, 23]
AC = [3, 2, 1]
BA = [17, 16, 13]
BB = [12, 6, 5]
BC = [0, 14, 8]
CA = [27, 26, 24]
CB = [25, 4, 7]
CC = [10, 9, 15]

GPIO.setup(AA, GPIO.OUT)
GPIO.output(AA, GPIO.HIGH)
sleep(0.5)
GPIO.output(AA, GPIO.LOW)
sleep(0.5)

GPIO.setup(AB, GPIO.OUT)
GPIO.output(AB, GPIO.HIGH)
sleep(0.5)
GPIO.output(AB, GPIO.LOW)
sleep(0.5)

GPIO.setup(AC, GPIO.OUT)
GPIO.output(AC, GPIO.HIGH)
sleep(0.5)
GPIO.output(AC, GPIO.LOW)
sleep(0.5)

GPIO.setup(BA, GPIO.OUT)
GPIO.output(BA, GPIO.HIGH)
sleep(0.5)
GPIO.output(BA, GPIO.LOW)
sleep(0.5)

GPIO.setup(BB, GPIO.OUT)
GPIO.output(BB, GPIO.HIGH)
sleep(0.5)
GPIO.output(BB, GPIO.LOW)
sleep(0.5)

GPIO.setup(BC, GPIO.OUT)
GPIO.output(BC, GPIO.HIGH)
sleep(0.5)
GPIO.output(BC, GPIO.LOW)
sleep(0.5)

GPIO.setup(CA, GPIO.OUT)
GPIO.output(CA, GPIO.HIGH)
sleep(0.5)
GPIO.output(CA, GPIO.LOW)
sleep(0.5)
GPIO.setup(CB, GPIO.OUT)
GPIO.output(CB, GPIO.HIGH)
sleep(0.5)
GPIO.output(CB, GPIO.LOW)
sleep(0.5)
GPIO.setup(CC, GPIO.OUT)
GPIO.output(CC, GPIO.HIGH)
sleep(0.5)
GPIO.output(CC, GPIO.LOW)
sleep(0.5)

#Light Pattern for Gutiar
e = [3, 0, 10]
b = [22, 6, 4]
g = [20, 13, 24]
d = [21, 12, 25]
a = [19, 16, 26]
E = [23, 5, 7]

GPIO.setup(e, GPIO.OUT)
GPIO.output(e, GPIO.HIGH)
sleep(0.5)
GPIO.output(e, GPIO.LOW)
sleep(0.5)
GPIO.setup(b, GPIO.OUT)
GPIO.output(b, GPIO.HIGH)
sleep(0.5)
GPIO.output(b, GPIO.LOW)
sleep(0.5)
GPIO.setup(g, GPIO.OUT)
GPIO.output(g, GPIO.HIGH)
sleep(0.5)
GPIO.output(g, GPIO.LOW)
sleep(0.5)
GPIO.setup(d, GPIO.OUT)
GPIO.output(d, GPIO.HIGH)
sleep(0.5)
GPIO.output(d, GPIO.LOW)
sleep(0.5)
GPIO.setup(a, GPIO.OUT)
GPIO.output(a, GPIO.HIGH)
sleep(0.5)
GPIO.output(a, GPIO.LOW)
sleep(0.5)
GPIO.setup(E, GPIO.OUT)
GPIO.output(E, GPIO.HIGH)
sleep(0.5)
GPIO.output(E, GPIO.LOW)
sleep(0.5)

#Light Pattern for Piano
blackKeys = [17,16,13,12,6,5]
GPIO.setup(blackKeys, GPIO.OUT)
GPIO.output(blackKeys, GPIO.HIGH)
sleep(0.5)
GPIO.output(blackKeys, GPIO.LOW)
sleep(0.5)
whiteKeys = [18,19,20,21,22,23,3,2,1,0,14,8,24,25,26,27,4,7,9,10,15]
GPIO.setup(whiteKeys, GPIO.OUT)
GPIO.output(whiteKeys, GPIO.HIGH)
sleep(0.5)
GPIO.output(whiteKeys, GPIO.LOW)
sleep(0.5)

