import pygame
from hero import Hero
from screeninfo import get_monitors
import random


def load_image(name):
    image = pygame.image.load(name)
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
        self.move = self.width * 0.2 * (1/50)


class Map:
    def __init__(self):
        pygame.init()

    def update(self, mob):
        mob.rect.x -= mob.move

    def draw(self, screen, hero_type):
        self.width, self.height = int(str(get_monitors()[0]).split('width=')[1][:4]), \
                                  int(str(get_monitors()[0]).split('height=')[1][:4]) - 76
        bg = pygame.image.load("fon6.jpg")
        fon = pygame.transform.scale(bg, (self.width, self.height))
        screen.blit(fon, (0, 0))
        font = pygame.font.SysFont('comic sans ms', 50)
        txt = font.render('Счет: ', True, (255, 255, 255))
        txt_x = self.width // 2 - txt.get_width() // 2
        txt_y = int(self.height * 0.2)
        pygame.draw.rect(screen, (255, 255, 255), (txt_x - 10, txt_y + 10,
                                                   txt.get_width() + 20, txt.get_height() + 20), 3)
        screen.blit(txt, (txt_x, int(self.height * 0.1)))
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
        pos1 = self.height * 0.55
        pos2 = self.height * 0.35
        running = True
        move = 0
        clock = pygame.time.Clock()
        fps = 1000
        hero_sprites.draw(screen)
        targets = pygame.sprite.Group()
        mob = Mob()
        targets.add(mob)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.KEYDOWN:
                    key = event.key
                    if key == pygame.K_UP or key == pygame.K_w:
                        move = -self.height * 0.2 * (1 / 50)
                        sprite.update((0, move))
                        hero_sprites.clear(screen, screen1)
                        bg_sprites.draw(screen)
                    elif key == pygame.K_DOWN or key == pygame.K_s:
                        move = self.height * 0.2 * (1 / 50)
                        sprite.update((0, move))
                        hero_sprites.clear(screen, screen1)
                        bg_sprites.draw(screen)
                if event.type == pygame.KEYUP:
                    key = event.key
                    if key == pygame.K_UP or key == pygame.K_w:
                        if move == -self.height * 0.2 * (1 / 50):
                            move = 0
                        hero_sprites.clear(screen, screen1)
                        bg_sprites.draw(screen)
                    elif key == pygame.K_DOWN or key == pygame.K_s:
                        if move == self.height * 0.2 * (1 / 50):
                            move = 0
                        hero_sprites.clear(screen, screen1)
                        bg_sprites.draw(screen)
            mob.rect.x -= mob.move
            targets.clear(screen, screen1)
            bg_sprites.draw(screen)
            if pos2 <= sprite.get_y() <= pos1:
                sprite.update((0, move))
                hero_sprites.clear(screen, screen1)
                bg_sprites.draw(screen)
            if sprite.get_y() >= pos1 or sprite.get_y() <= pos2:
                move = 0
            clock.tick(fps)
            targets.draw(screen)
            hero_sprites.draw(screen)
            pygame.display.flip()
        pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    size = width, height = int(str(get_monitors()[0]).split('width=')[1][:4]), \
                           int(str(get_monitors()[0]).split('height=')[1][:4]) - 76
    screen = pygame.display.set_mode(size)
    m = Map()
    m.draw(screen, "Dean")
pygame.quit()
