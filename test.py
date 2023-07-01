# import matplotlib.pyplot as plt
# import numpy as np
#
# xs = [15, 50,
# 70,
# 130,
# 250,
# 300,
# 400,
# 580,
# 690,
# 780,
# 900,
# 1000]
# ys = [80,30,
# 20,
# 10,
# 5,
# 4,
# 3,
# 2,
# 1.66,
# 1.5,
# 1.33,
# 1.2]
#
# plt.plot(xs, ys)
# plt.show()
import serial
my_serial = serial.Serial(port='com11', baudrate=115200)
while True:
    line = my_serial.readline()
    print(line)
