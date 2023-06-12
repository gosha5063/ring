import serial
import mouse
import time
import numpy as np

my_serial = serial.Serial(port='com12', baudrate=200000)
my_serial.write(b"{some ASCII comand}\r\n")
controll = mouse.Mouse()
steck_x = []
steck_a = []
steck_y = []
steck_len = 10
while 1:
    line = my_serial.readline()
    line = line.decode('UTF-8')
    if len(steck_x) == steck_len:
        win = 50
        filt = np.ones(win) / win
        res_x = np.convolve(steck_x, filt, mode='same')
        res_y = np.convolve(steck_y, filt, mode='same')
        res_a = np.convolve(steck_y, filt, mode='same')
        controll.movement_array(res_x,res_y,res_a,win)
        steck_x = []
        steck_y = []
        steck_a = []

    steck_x.append(-float(line.split()[0]))
    steck_y.append(-float(line.split()[1]))
    steck_a.append(float(line.split()[2]))
    print(line)

