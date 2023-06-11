import time
import pygame
import sys

class PulsatingCircle:
    def __init__(self, screen, color, center, radius,num):
        self.screen = screen
        self.color = color
        self.center = center
        self.radius = radius
        self.num = num - 1
        self.pulse_speed = 1  # Скорость пульсации
        self.min_radius = 10  # Минимальный радиус круга
        self.max_radius = 15  # Максимальный радиус круга
        self.is_mouse_over = False

    def update(self,finish):
        if self.is_mouse_over:
            self.radius = 0
            print(pygame.mouse.get_pos())
            finish[self.num] = True
        # else:
        #     self.radius += self.pulse_speed
        #     if self.radius >= self.max_radius:
        #         self.radius = self.max_radius

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.center, self.radius)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            if self.is_mouse_over:
                if not self.is_point_inside(mouse_pos):
                    self.is_mouse_over = False
            else:
                if self.is_point_inside(mouse_pos):
                    self.is_mouse_over = True

    def is_point_inside(self, point):
        return (point[0] - self.center[0]) ** 2 + (point[1] - self.center[1]) ** 2 <= self.radius ** 2


def check_if_true(s):
    for i in s:
        if not i:
            return False
    return True
def main():
    pygame.init()
    screen_width, screen_height = pygame.display.Info().current_w,pygame.display.Info().current_h
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Pulsating Circle")
    font = pygame.font.Font(None, 80)

    start_time = time.time()
    clock = pygame.time.Clock()
    radius = 30
    circle = PulsatingCircle(screen, (255, 165, 0), (screen_width // 2, screen_height // 2), radius,1)
    circle2 = PulsatingCircle(screen, (255, 165, 0), (radius,radius), radius,2)
    circle3 = PulsatingCircle(screen, (255, 165, 0), (screen_width-radius,radius), radius,3)
    circle4 = PulsatingCircle(screen, (255, 165, 0), (radius,screen_height-radius), radius,4)
    circle5 = PulsatingCircle(screen, (255, 165, 0), (screen_width-radius,screen_height-radius), radius,5)

    circles = [
        circle,
        circle2,
        circle3,
        circle4,
        circle5,
    ]
    finish = [False,
              False,
              False,
              False,
              False,
        ]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or check_if_true(finish):
                print(seconds)
                pygame.quit()
                sys.exit()
            for circ in circles:
                circ.handle_event(event)
        screen.fill((0,0,0))

        for circ in circles:
            circ.update(finish)
            circ.draw()
        seconds = (time.time() - start_time)
        timer_text = font.render("{:.2f}".format(seconds), True, (255,255,255))
        timer_rect = timer_text.get_rect(center=(screen_width // 2, screen_height // 2 - 2*radius))
        screen.blit(timer_text, timer_rect)
        print(finish)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
