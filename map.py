import pygame


class Map:
    def __init__(self, screen):
        self.screen = screen

    def draw(self):
        self.screen.fill((0, 0, 0))
        # прорисовка карты
