import pyfirmata
comport='COM7'
board=pyfirmata.Arduino(comport)

led_1=board.get_pin('d:13:o')
led_2=board.get_pin('d:12:o')
led_3=board.get_pin('d:11:o')
led_4=board.get_pin('d:10:o')
led_5=board.get_pin('d:9:o')

def led(selectionList):
    if selectionList[0]!=-1 and selectionList[1]!=-1 and selectionList[2]!=-1:
        if selectionList[0]==1:
            led_1.write(0)
            led_2.write(0)
            led_3.write(0)
            led_4.write(0)
            led_5.write(0)
        elif totalFingers==1:
            led_1.write(1)
            led_2.write(0)
            led_3.write(0)
            led_4.write(0)
            led_5.write(0)
        elif totalFingers==2:
            led_1.write(1)
            led_2.write(1)
            led_3.write(0)
            led_4.write(0)
            led_5.write(0)
        elif totalFingers==3:
            led_1.write(1)
            led_2.write(1)
            led_3.write(1)
            led_4.write(0)
            led_5.write(0)
        elif totalFingers==4:
            led_1.write(1)
            led_2.write(1)
            led_3.write(1)
            led_4.write(1)
            led_5.write(0)
        elif totalFingers==5:
            led_1.write(1)
            led_2.write(1)
            led_3.write(1)
            led_4.write(1)
            led_5.write(1)