from pynput.mouse import Controller
import mouse as mp

class Mouse():
    def __init__(self):
        self.mouse = Controller()

    def set_position(self,koord, koord_finish):
        self.mouse.move(koord_finish[0] - koord[0],koord_finish[1] - koord[1])

    def value_of_pos(self,koord,porog,speed):
        finish_koord = 0
        if abs(koord) > porog:
            finish_koord = abs(koord)*speed/koord
        return finish_koord

    def movement(self,x,y):

        self.mouse.move(x,y)
    # def movement_array(self,array_x,array_y,acsel_y,ln):
    #     const = ln//10
    #     for i in range(ln//10):
    #         grad_s_x, grad_s_y = self.value_of_pos(koord= sum(array_x[i*const:i*const+const])/10, porog=5, speed=3), \
    #         self.value_of_pos(koord= sum(array_y[i*const:i*const+const])/10, porog=5, speed=3)
    #         self.mouse.move(grad_s_y, grad_s_x)
