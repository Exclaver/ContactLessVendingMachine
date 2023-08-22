import pyfirmata
port='COM7'
board=pyfirmata.Arduino(port)

def rotateServo(pin,angle):
    board.digital[pin].write(angle)
    sleep(0.015)




def led(selectionList):
    if selectionList[2]==1:
        for j in range(selectionList[2]):
                for i in range(0,180):
                    rotateServo(selectionList[0],360)
    
            