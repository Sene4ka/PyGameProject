import pygame


class Map:
    def __init__(self):
        pass

    def draw(self):
        pygame.init()
        size = 1350, 720
        screen = pygame.display.set_mode(size)
        screen.fill((0, 0, 0))
        # прорисовка карты
