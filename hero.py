import pygame
import os
from screeninfo import get_monitors


def load_image(name):
    fullname = os.path.join('sprites', name)
    image = pygame.image.load(fullname)
    return image


class Hero(pygame.sprite.Sprite):
    def __init__(self, group, hero_type):
        super().__init__()
        pygame.init()
        width, height = int(str(get_monitors()[0]).split('width=')[1][:4]), \
                        int(str(get_monitors()[0]).split('height=')[1][:4]) - 76
        if hero_type == 'Dean':
            image = load_image("hero1.png")
            image1 = pygame.transform.scale(image, (int(width * 0.3), int(height * 0.3)))
        elif hero_type == 'Sam':
            image = load_image("Impala.png")
            image1 = pygame.transform.scale(image, (int(width * 0.3), int(height * 0.3)))
        self.image = image1
        self.rect = self.image.get_rect()
        self.rect.x = width * 0.35
        self.rect.y = height * 0.5

    def update(self, coords):
        self.rect = self.rect.move(coords[0], coords[1])

    def get_y(self):
        return self.rect.y



