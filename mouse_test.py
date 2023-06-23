from pynput import mouse
import pygame
def set_position(koord,koord_finish):
    m.move(koord[0] - koord_finish[0], koord[1] - koord_finish[1])
m = mouse.Controller
radius = 30
screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
set_position(m.position,(screen_width // 2, screen_height // 2))





