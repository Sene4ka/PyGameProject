import pygame
from hero import Hero
from mob import Mob
from final import Final
from screeninfo import get_monitors
import sqlite3
from death import Death
from pygame import mixer


def load_image(name):
    # функция загрузки картинок
    image = pygame.image.load(name)
    return image


def points(point, width, height, screen):
    # выводим счет
    font = pygame.font.SysFont('comic sans ms', 50)
    txt = font.render(f'Счет: {point}', True, (0, 0, 0))
    txt_x = width * 0.01
    txt_y = height * 0.01
    pygame.draw.rect(screen, (0, 0, 0), (txt_x - 10, txt_y - 10,
                                         txt.get_width() + 20, txt.get_height() + 20), 3)
    screen.blit(txt, (txt_x, int(height * 0.01)))



class Map:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.width, self.height = int(str(get_monitors()[0]).split('width=')[1][:4]), \
                                  int(str(get_monitors()[0]).split('height=')[1][:4]) - 76


    def draw(self, screen, hero_type, song, p):
        # создаем экран
        bg = pygame.image.load("main_fon.jpg")
        # создаем фон
        fon = pygame.transform.scale(bg, (self.width, self.height))
        bg_sprites = pygame.sprite.Group()
        bg_sprite = pygame.sprite.Sprite()
        bg_sprite.image = fon
        bg_sprite.rect = bg_sprite.image.get_rect()
        bg_sprite.rect.x = 0
        bg_sprite.rect.y = 0
        bg_sprites.add(bg_sprite)
        bg_sprites.draw(screen)
        # создаем невидимый Surface для очистки спрайтов
        screen1 = pygame.Surface((self.width, self.height))
        screen1.set_alpha(255)
        # создаем машину
        hero_sprites = pygame.sprite.Group()
        sprite = Hero(hero_sprites, hero_type)
        hero_sprites.add(sprite)
        # количество баллов
        self.p = p
        # калибруем позиции и границы передвижения
        pos1 = self.height * 0.8
        pos2 = self.height * 0.50
        mpos = self.height * 0.71
        running = True
        move = 0
        clock = pygame.time.Clock()
        fps = 1000
        # создаем мобов
        targets = pygame.sprite.Group()
        mob = Mob(self.width + self.width * 0.2)
        targets.add(mob)
        self.con = sqlite3.connect("spn.db")
        self.cur = self.con.cursor()
        # рисуем спрайты и начинаем цикл
        hero_sprites.draw(screen)
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(-1)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                # проверяем на нажатие клавиш
                if event.type == pygame.KEYDOWN:
                    key = event.key
                    if key == pygame.K_UP or key == pygame.K_w:
                        move = -self.height * 0.2 * (1 / 50)
                        sprite.update((0, move))
                        if sprite.get_y() < pos2:
                            sprite.rect.y = pos2
                        hero_sprites.clear(screen, screen1)
                        bg_sprites.draw(screen)
                    elif key == pygame.K_DOWN or key == pygame.K_s:
                        move = self.height * 0.2 * (1 / 50)
                        sprite.update((0, move))
                        if sprite.get_y() > pos1:
                            sprite.rect.y = pos1
                        hero_sprites.clear(screen, screen1)
                        bg_sprites.draw(screen)
                # проверяем на поднятие клавиш
                if event.type == pygame.KEYUP:
                    key = event.key
                    if key == pygame.K_UP or key == pygame.K_w:
                        if move == -self.height * 0.2 * (1 / 50):
                            move = 0
                        hero_sprites.clear(screen, screen1)
                    elif key == pygame.K_DOWN or key == pygame.K_s:
                        if move == self.height * 0.2 * (1 / 50):
                            move = 0
                        hero_sprites.clear(screen, screen1)
            # двигаем мобов
            mob.rect.x -= mob.move
            targets.clear(screen, screen1)
            # не даем машине выйти за границы
            if sprite.get_y() >= pos1 or sprite.get_y() <= pos2:
                move = 0
            if sprite.get_y() > pos1:
                sprite.rect.y = pos1
            elif sprite.get_y() < pos2:
                sprite.rect.y = pos2
            # двигаем машину
            if pos2 <= sprite.get_y() <= pos1:
                sprite.update((0, move))
                hero_sprites.clear(screen, screen1)
            # проверяем выход моба за экран
            if mob.rect.x <= self.width * 0 - self.width * 0.2:
                targets.clear(screen, screen1)
                targets.remove(mob)
                mob = Mob(self.width + self.width * 0.2)
                targets.add(mob)
            # проверяем столкновения с машиной
            if mob.rect.x <= sprite.rect.x + self.width * 0.3:
                if mob.get_y() < mpos:
                    if sprite.get_y() <= mpos:
                        name = mob.target
                        res = self.cur.execute("""SELECT * FROM Heroes
                                                  WHERE Hero = '{}'""".format(name)).fetchall()
                        type = str(res[0][1])
                        x = mob.rect.x
                        targets.clear(screen, screen1)
                        targets.remove(mob)
                        mob = Mob((self.width + self.width * 0.2) + (x + (self.width * 0.2)))
                        targets.add(mob)
                        if type == 'Друг':
                            self.p -= 5
                        elif type == 'Монстр':
                            self.p += 5
                        elif type == 'Враг':
                            d = Death()
                elif mob.get_y() > mpos:
                    if sprite.get_y() > mpos:
                        name = mob.target
                        res = self.cur.execute("""SELECT * FROM Heroes
                                                  WHERE Hero = '{}'""".format(name)).fetchall()
                        type = str(res[0][1])
                        x = mob.rect.x
                        targets.clear(screen, screen1)
                        targets.remove(mob)
                        mob = Mob((self.width + self.width * 0.2) + (x + (self.width * 0.2)))
                        targets.add(mob)
                        if type == 'Друг':
                            self.p -= 5
                        elif type == 'Монстр':
                            self.p += 5
                        elif type == 'Враг':
                            d = Death()

                        # начисление очков
            # рисуем все спрайты и обновляем
            if self.p == 40:
                m = Final()
            if self.p == 0:
                m = Death()
            clock.tick(fps)
            bg_sprites.draw(screen)
            targets.draw(screen)
            hero_sprites.draw(screen)
            # выводим очки
            points(self.p, self.width, self.height, screen)
            pygame.display.flip()
        pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    size = width, height = int(str(get_monitors()[0]).split('width=')[1][:4]), \
                           int(str(get_monitors()[0]).split('height=')[1][:4]) - 76
    screen = pygame.display.set_mode(size)
    m = Map()
    m.draw(screen, "Dean", 'carry_on.mp3')
pygame.quit()