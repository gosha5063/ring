import time
import pygame
from pygame.locals import *
from collections import deque

f = open('scroll_1.txt')

pygame.init()
w, h = 905, 1167
screen = pygame.display.set_mode((w, h))

img = pygame.image.load('1_1.png')
img_rect = img.get_rect()
img_rect.center = w // 2, h // 2

RED = (255, 0, 0)
GRAY = (150, 150, 150)

animation = pygame.image.load('animation.jpg')
animation_rect = animation.get_rect()

menu_pics_x = {
    1: [5, 0, 2],
    2: [0, 1, 3],
    3: [0, 2, 4],
    4: [0, 3, 0],
    5: [0, 0, 6],
    6: [0, 5, 7],
    7: [0, 6, 8],
    8: [0, 7, 0]
}

menu_pics_load = {
    1: [pygame.image.load('2_1.png'), 0, pygame.image.load('1_2.png')],
    2: [0, pygame.image.load('1_1.png'), pygame.image.load('1_3.png')],
    3: [0, pygame.image.load('1_2.png'), pygame.image.load('1_4.png')],
    4: [0, pygame.image.load('1_3.png'), 0],
    5: [0, 0, pygame.image.load('2_2.png')],
    6: [0, pygame.image.load('2_1.png'), pygame.image.load('2_3.png')],
    7: [0, pygame.image.load('2_2.png'), pygame.image.load('2_4.png')],
    8: [0, pygame.image.load('2_3.png'), 0]
}

current_pic_num = 1
time = 0
time_mass = [0] * 3
running = True

target_time = 50
acceleration_lasts = deque()
time_acceleration = 0

fl = 0
confirmation = 0

while running:

    y = int(f.readline().strip())
    time += 1
    time_acceleration += 1
    time_mass[y] += 1

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    if len(acceleration_lasts) == 2:
        if acceleration_lasts[0] == acceleration_lasts[1] != 0:
            if time_acceleration == target_time:
                target_time //= 1.1
                time_acceleration = 0
        else:
            target_time = 50

    print(time_mass)

    if time >= target_time:

        if time_mass[1] >= target_time * 0.8:
            time = 0
            time_mass = [0] * 3
            time_acceleration = 0

            img = menu_pics_load[current_pic_num][1]
            current_pic_num = menu_pics_x[current_pic_num][1]

            acceleration_lasts.append(1)

            confirmation = 0
            fl = 0

        elif time_mass[2] >= target_time * 0.8:
            time = 0
            time_mass = [0] * 3
            time_acceleration = 0

            img = menu_pics_load[current_pic_num][2]
            current_pic_num = menu_pics_x[current_pic_num][2]

            acceleration_lasts.append(2)

            confirmation = 0
            fl = 0

        elif time_mass[0] >= target_time * 0.8:

            time = 0
            time_mass = [0] * 3
            time_acceleration = 0

            if confirmation == 5:
                img = menu_pics_load[current_pic_num][0]
                current_pic_num = menu_pics_x[current_pic_num][0]
                fl = 0

            fl = 1
            confirmation += 1

            acceleration_lasts.append(0)

    if len(acceleration_lasts) == 3:
        acceleration_lasts.popleft()

    rect = img.get_rect()
    rect.center = w // 2, h // 2
    screen.fill(GRAY)

    if fl == 1:
        screen.blit(animation, animation_rect)
        pygame.draw.rect(screen, RED, animation_rect, 1)
    else:
        screen.blit(img, img_rect)
        pygame.draw.rect(screen, RED, img_rect, 1)

    pygame.display.update()
