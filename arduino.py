from pyfirmata import Arduino,SERVO,util
from time import sleep

port='COM10'
pin=10
board=Arduino(port)

board.digital[pin].mode=SERVO

def rotateServo(pin,angle):
    board.digital[pin].write(angle)
    sleep(0.015)

while True:
    x=input("input: ")
    if x=="1":
        for i in range(0,180):
            rotateServo(pin,i)
    elif x=="2":
        for i in range(0,90):
            rotateServo(pin,i)
    elif x=="3":
        for i in range(0,270):
            rotateServo(pin,i)