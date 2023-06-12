import serial
import mouse
my_serial = serial.Serial(port='com11', baudrate=9600)
x,y = 0,0
pos_kursor = [920, 540]
pos_kursor_finish = [920, 540]
from_middle_left_px = 5
from_middle_right_px = 920/40
from_middle_hight_px = rom_middle_down_px = 540/90
# def chet(koord,):
#     if 0 <= koord[0] <= 920 and 0 <= koord[1] <= 540:
#         return from_middle_left_px, from_middle_hight_px
#

controll = mouse.Mouse()
lastx = 0;
lasty =0;
while 1:
    try:
        line = my_serial.readline()
        koord = ord(line.decode('UTF-8').split()[0]) - 100
        if 1:
            if koord%2 == 1:
                controll.movement(0,int((koord-lasty) * 2*1080/180))
                lasty=koord
            else:
                controll.movement(-int((koord - lastx) * 4*1920 / 180),0)
                lastx = koord



        print(x,y,koord)



    except:
        print("Ошибка передачи")
    #


