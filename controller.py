
from pyfirmata import Arduino,SERVO,util
from time import sleep

port='COM11'
pin=6
board=Arduino(port)

board.digital[pin].mode=SERVO

def rotateServo(pin,angle):
    board.digital[pin].write(angle)
    sleep(0.0001)
    print("success")
def led(Amt):
    for j in range(0,Amt):
        for i in range(0,180):
                rotateServo(6,i)
        for i in range(180,1,-1):
                rotateServo(6,i)

def led1(pin):
    for i in range(0,180):
              rotateServo(pin,i)
    for i in range(180,1,-1):
              rotateServo(pin,i)
              


