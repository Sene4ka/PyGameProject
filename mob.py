import pygame
from screeninfo import get_monitors
import random


# создаем спрайт моба
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.heroes = ['Meg.png', 'Leviafan.png', 'Castiel.png', 'Bobby.png', 'Azazel.png']
        self.target = random.choice(self.heroes)
        self.image = pygame.image.load(self.target)
        self.width, self.height = int(str(get_monitors()[0]).split('width=')[1][:4]), \
                                  int(str(get_monitors()[0]).split('height=')[1][:4]) - 76
        self.image = pygame.transform.scale(self.image, (int(self.width * 0.08), int(self.height * 0.14)))
        self.rect = self.image.get_rect()
        self.rect.x = self.width - self.width * 0.1
        self.rect.y = random.choice([self.height * 0.68, self.height * 0.84])
        self.move = self.width * 0.2 * (1/100)

    def get_y(self):
        # возвращаем y
        return self.rect.y