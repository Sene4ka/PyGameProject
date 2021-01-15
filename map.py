import os
import pygame
from hero import Hero
from screeninfo import get_monitors
import random


def load_image(name):
    fullname = os.path.join('sprites', name)
    image = pygame.image.load(fullname)
    return image

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.heroes = ['Meg.png', 'Leviafan.png', 'Castiel.png', 'Bobby.png', 'Azazel.png']
        target = random.choice(self.heroes)
        self.image = pygame.image.load(target)
        self.width, self.height = int(str(get_monitors()[0]).split('width=')[1][:4]), \
                                  int(str(get_monitors()[0]).split('height=')[1][:4]) - 76
        self.image = pygame.transform.scale(self.image, (int(self.width * 0.08), int(self.height * 0.14)))
        self.rect = self.image.get_rect()
        self.rect.x = self.width - self.width * 0.1
        self.rect.y = random.randrange((self.height * 0.6 - self.height * 0.1), int(self.height - self.height * 0.1))
        self.move = random.randrange(1, 8)


class Map:
    def __init__(self):
        pygame.init()

    def update(self):
        Mob().rect.x -= Mob().move

    def draw(self, screen, hero_type):
        self.width, self.height = int(str(get_monitors()[0]).split('width=')[1][:4]), \
                                  int(str(get_monitors()[0]).split('height=')[1][:4]) - 76
        bg = pygame.image.load("main_fon.jpg")
        fon = pygame.transform.scale(bg, (self.width, self.height))
        screen.blit(fon, (0, 0))
        bg_sprites = pygame.sprite.Group()
        bg_sprite = pygame.sprite.Sprite()
        bg_sprite.image = fon
        bg_sprite.rect = bg_sprite.image.get_rect()
        bg_sprite.rect.x = 0
        bg_sprite.rect.y = 0
        bg_sprites.add(bg_sprite)
        bg_sprites.draw(screen)
        screen1 = pygame.Surface((self.width, self.height))
        screen1.set_alpha(255)
        hero_sprites = pygame.sprite.Group()
        sprite = Hero(hero_sprites, hero_type)
        hero_sprites.add(sprite)
        pos1 = self.height * 0.5
        pos2 = self.height * 0.3
        running = True
        pos = True
        move = 0
        clock = pygame.time.Clock()
        fps = 1000
        hero_sprites.draw(screen)
        targets = pygame.sprite.Group()
        for i in range(8):
            t = Mob()
            hero_sprites.add(t)
            targets.add(t)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    key = event.key
                    if key == pygame.K_UP:
                        move = -(self.height * 0.2 * (1 / 25))
                        sprite.update((0, move))
                        bg_sprites.draw(screen)
                        hero_sprites.clear(screen, screen1)
                    elif key == pygame.K_DOWN:
                        move = (self.height * 0.2 * (1 / 25))
                        sprite.update((0, move))
                        bg_sprites.draw(screen)
                        hero_sprites.clear(screen, screen1)
            hero_sprites.draw(screen)
            clock.tick(fps)
            Mob().rect.x -= Mob().move
            targets.draw(screen)
            pygame.display.flip()
            if  pos2 <= sprite.get_y() <= pos1:
                sprite.update((0, move))
                bg_sprites.draw(screen)
                hero_sprites.clear(screen, screen1)
                bg_sprites.draw(screen)
            if sprite.get_y() == pos1 or sprite.get_y() == pos2:
                move = 0
            pygame.display.flip()
        pygame.display.update()
pygame.quit()
