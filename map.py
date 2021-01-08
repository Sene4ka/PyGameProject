import os
import sys
import pygame
from hero import Hero
from enemy import Enemy
from screeninfo import get_monitors


def load_image(name):
    fullname = os.path.join('sprites', name)
    image = pygame.image.load(fullname)
    return image


class Map:
    def __init__(self):
        pygame.init()

    def draw(self, screen, hero_type):
        width, height = int(str(get_monitors()[0]).split('width=')[1][:4]), \
                        int(str(get_monitors()[0]).split('height=')[1][:4]) - 76
        bg = pygame.image.load("fon6.jpg")
        fon = pygame.transform.scale(bg, (width, height))
        screen.blit(fon, (0, 0))
        hero_sprites = pygame.sprite.Group()
        sprite = pygame.sprite.Sprite()
        if hero_type == 'Dean':
            image = load_image("hero1.png")
            image1 = pygame.transform.scale(image, (int(width * 0.3), int(height * 0.3)))
            sprite.image = image1
        elif hero_type == 'Sam':
            image = load_image("hero2.png")
            image1 = pygame.transform.scale(image, (int(width * 0.3), int(height * 0.3)))
            sprite.image = image1
        sprite.rect = sprite.image.get_rect()
        sprite.rect.x = width * 0.35
        sprite.rect.y = height * 0.4
        hero_sprites.add(sprite)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                hero_sprites.draw(screen)
            pygame.display.flip()
        pygame.display.update()

