import mouse
import time
import serial
my_serial = serial.Serial(port='com11', baudrate=115200)
controller = mouse.Mouse()
mouse_for_koord = mouse.Controller()
screen = (1279, 719)
def rows(x,y):
    '''функция для расчета координат'''
    if abs(mouse_for_koord.position[0] - x*screen[0]) >= 10 and abs(mouse_for_koord.position[1] - y*screen[1]) >= 10:
        x = x*screen[0]
        y = y*screen[1]
        return (x,y)
    elif abs(mouse_for_koord.position[1] - y*screen[1]) >= 10:
        y = y*screen[1]
        return (mouse_for_koord.position[0],y)
    elif abs(mouse_for_koord.position[0] - x*screen[0]) >= 10:
        x = x * screen[0]
        return (x,mouse_for_koord.position[1])
    return mouse_for_koord.position
controller.set_position(mouse_for_koord.position,(screen[0]/2,screen[1]/2))
x_start, y_start = map(float, my_serial.readline().decode('UTF-8').split())

while True:
    print(my_serial.readline())
    x,y = map(float,my_serial.readline().decode('UTF-8').split())
    print(x,y)
    x -= x_start
    controller.set_position(mouse_for_koord.position,rows(x,y))
