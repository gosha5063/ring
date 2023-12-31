import pygame as pg
import sys
import serial
from screeninfo import get_monitors

m_soft = {1: [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4],
     2: [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4],
     3: [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4],
     4: [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4],
          5: [5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,9],
          6: [5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,9],
          7: [5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,9],
          8: [5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,9],
          9: [5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,9],
          10: [11]*16,
          11: [11]*16}
m_hard = {1: [5,5,5,5, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4],
     2: [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4],
     3: [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4],
     4: [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4],
          5: [5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9],
          6: [5, 5, 5, 10, 10, 10, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9],
          7: [5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9],
          8: [5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9],
          9: [5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 1,1,1,1],
          10: [11]*16,
          11:[5]*16
          }
imgs = [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11]
class Page:
    def __init__(self):
        self.weigth, self.height = get_monitors()[0].width, get_monitors()[0].height
        print(self.weigth,self.height)
        self.id = 1
    def draw(self,sc, koord, click):
        koord = min(koord,15)
        if click:
            map_g = m_hard
        else:
            map_g = m_soft
        if (map_g[self.id][koord]!=-1):
            self.id = map_g[self.id][koord]
            dog_surf = pg.image.load(f'menu_media/{str(imgs[self.id])}.png')
            dog_surf = pg.transform.scale(dog_surf,(self.weigth,self.height))
            dog_rect = dog_surf.get_rect()
            sc.blit(dog_surf, dog_rect)




def main():
    weigth, height = get_monitors()[0].width+100, get_monitors()[0].height+140
    Menu_Page = Page()
    sc = pg.display.set_mode((weigth, height))
    sc.fill((0, 0, 0))
    while 1:
        line = int(my_serial.readline().decode("UTF-8"))

        for i in pg.event.get():
            if i.type == pg.QUIT:
                sys.exit()
            if i.type == pg.KEYUP:
                if i.key == pg.K_SPACE:
                    Menu_Page.draw(sc=sc, koord=line, click = True)

        Menu_Page.draw(sc=sc, koord=line, click = False)
        pg.display.update()
        pg.time.delay(20)
if __name__ == '__main__':
    my_serial = serial.Serial(port='com12   ', baudrate=9600)
    main()