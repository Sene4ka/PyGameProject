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
        bg = pygame.image.load("main_fon.jpg")
        fon = pygame.transform.scale(bg, (width, height))
        screen.blit(fon, (0, 0))
        bg_sprites = pygame.sprite.Group()
        bg_sprite = pygame.sprite.Sprite()
        bg_sprite.image = fon
        bg_sprite.rect = bg_sprite.image.get_rect()
        bg_sprite.rect.x = 0
        bg_sprite.rect.y = 0
        bg_sprites.add(bg_sprite)
        bg_sprites.draw(screen)
        screen1 = pygame.Surface((width, height))
        screen1.set_alpha(255)
        hero_sprites = pygame.sprite.Group()
        sprite = Hero(hero_sprites, hero_type)
        hero_sprites.add(sprite)
        pos1 = height * 0.5
        pos2 = height * 0.3
        running = True
        pos = True
        move = 0
        clock = pygame.time.Clock()
        fps = 1000
        hero_sprites.draw(screen)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    key = event.key
                    if key == pygame.K_w:
                        move = -(height * 0.2 * (1 / 25))
                        sprite.update((0, move))
                        bg_sprites.draw(screen)
                        hero_sprites.clear(screen, screen1)
                    elif key == pygame.K_s:
                        move = (height * 0.2 * (1 / 25))
                        sprite.update((0, move))
                        bg_sprites.draw(screen)
                        hero_sprites.clear(screen, screen1)
            if  pos2 <= sprite.get_y() <= pos1:
                sprite.update((0, move))
                bg_sprites.draw(screen)
                hero_sprites.clear(screen, screen1)
                bg_sprites.draw(screen)
            if sprite.get_y() == pos1 or sprite.get_y() == pos2:
                move = 0
            hero_sprites.draw(screen)
            clock.tick(fps)
            pygame.display.flip()
        pygame.display.update()

