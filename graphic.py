import serial
from matplotlib import pyplot
import numpy as np
import time
my_serial = serial.Serial(port='com12', baudrate=200000)
my_serial.write(b"{some ASCII comand}\r\n")

stack_x = []
stack_y = []
stack_time = []
start_time = time.time()
for i in range(1000):
    line = my_serial.readline().decode('UTF-8')
    print(line)
    stack_time.append(start_time-time.time())
    stack_x.append(-float(line.split()[0]))
    stack_y.append(-float(line.split()[1]))

pyplot.plot( stack_time,stack_x,'r',label = 'x angle')
win = 150
filt = np.ones(win)/win
# res = np.convolve(stack_x, filt, mode='same')
# pyplot.plot(stack_time, res, 'r')



# pyplot.plot( stack_time,stack_y, label = 'y_angle')
pyplot.ylabel('angle')
pyplot.xlabel('time')
fig = pyplot.figure()
pyplot.show()

