import pygame
import sqlite3
from screeninfo import get_monitors


class Menu:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.count = 0
        pygame.display.set_caption('Supernatural: Team free will')
        size = self.width, self.height = int(str(get_monitors()[0]).split('width=')[1][:4]), \
                               int(str(get_monitors()[0]).split('height=')[1][:4]) - 76
        self.screen = pygame.display.set_mode(size)
        bg = pygame.image.load("fon.jpg")
        self.bg = pygame.transform.scale(bg, (self.width, self.height))
        self.kn1 = pygame.image.load("Knopka.png")
        self.kn2 = pygame.image.load("Knopka2.png")
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.kn2, (self.width * 0.3, self.height * 0.5))
        self.screen.blit(self.kn1, (self.width * 0.7, self.height * 0.5))
        f = pygame.font.SysFont('comic sans ms', 50)
        self.con = sqlite3.connect("spn.db")  # соединение с бд
        self.cur = self.con.cursor()
        self.heroes = ['Meg.png', 'Leviafan.png', 'Castiel.png', 'Bobby.png', 'Azazel.png']
        self.text = f.render("Познакомься с героями!", False, (0, 0, 0))
        self.text_x = self.width // 2 - self.text.get_width() // 2
        self.text_y = int(self.height * 0.1)
        self.coors = (self.text_x, self.text_y)
        pygame.draw.rect(self.screen, (0, 0, 0), (self.text_x - 5, self.text_y - 5, self.text.get_width() + 10, self.text.get_height() + 10), 4)
        pygame.draw.rect(self.screen, (169, 169, 169),
                         (self.text_x - 5 + 4, self.text_y - 5 + 4, self.text.get_width() + 10 - 6, self.text.get_height() + 10 - 6))
        self.screen.blit(self.text, self.coors)
        geroy = self.heroes[self.count]
        res = self.cur.execute("""SELECT * FROM Heroes
                                  WHERE Hero = '{}'""".format(geroy)).fetchall()
        new_im = pygame.image.load(geroy)
        self.new_im = pygame.transform.scale(new_im, (int(self.width * 0.24), int(self.height * 0.45)))
        self.font_name = pygame.font.SysFont('comic sans ms', 50)
        self.font_type = pygame.font.SysFont('comic sans ms', 37)
        self.font_descr = pygame.font.SysFont('comic sans ms', 20)
        name = self.font_name.render('Мэг', False, (169, 169, 169))
        tip = self.font_type.render(str(res[0][1]), False, (169, 169, 169))
        d = str(res[0][2]).split('. ')
        descr1 = self.font_descr.render(str(d[0] + '.'), False, (169, 169, 169))
        if len(d) > 1:
            descr2 = self.font_descr.render(str(d[1]), False, (169, 169, 169))
        else:
            descr2 = ''
        self.coor_im_x = self.width * 0.36
        self.coor_im_y = self.height * 0.3
        self.coor_n_x = self.width * 0.44
        self.coor_n_y = self.height * 0.75
        self.coor_t_x = self.width * 0.45
        self.coor_t_y = self.height * 0.8
        if len(d[0]) >= 100:
            self.coor_d_x1 = self.width * 0.2
        elif len(d[0]) >= 85:
            self.coor_d_x1 = self.width * 0.25
        else:
            self.coor_d_x1 = self.width * 0.33
        if len(d[1]) >= 100:
            self.coor_d_x2 = self.width * 0.25
        elif len(d[1]) >= 85:
            self.coor_d_x2 = self.width * 0.25
        else:
            self.coor_d_x2 = self.width * 0.33
        self.coor_d_y1 = self.height * 0.85
        self.coor_d_y2 = self.height * 0.87
        self.screen.blit(self.new_im, (self.coor_im_x, self.coor_im_y))
        self.screen.blit(name, (self.coor_n_x, self.coor_n_y))
        self.screen.blit(tip, (self.coor_t_x, self.coor_t_y))
        self.screen.blit(descr1, (self.coor_d_x1, self.coor_d_y1))
        self.screen.blit(descr2, (self.coor_d_x2, self.coor_d_y2))
        pygame.display.update()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if self.width * 0.7 <= x <= (self.width * 0.7 + self.kn1.get_width()) and self.height * 0.5 <= y <= (self.height * 0.5 + self.kn1.get_height()):
                        self.count += 1
                        self.new_hero()
                    elif self.width * 0.3 <= x <= (self.width * 0.3 + self.kn2.get_width()) and self.height * 0.5 <= y <= (self.height * 0.5 + self.kn2.get_height()):
                        self.count -= 1
                        self.new_hero()

    def new_hero(self):
        num = self.count % 5
        geroy = self.heroes[num]
        if geroy == 'Meg.png':
            name = 'Мэг'
        if geroy == 'Leviafan.png':
            name = 'Левиафан'
        if geroy == 'Castiel.png':
            name = 'Кастиэль'
        if geroy == 'Bobby.png':
            name = 'Бобби'
        if geroy == 'Azazel.png':
            name = 'Азазель'
        res = self.cur.execute("""SELECT * FROM Heroes
                                  WHERE Hero = '{}'""".format(geroy)).fetchall()
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.kn2, (self.width * 0.3, self.height * 0.5))
        self.screen.blit(self.kn1, (self.width * 0.7, self.height * 0.5))
        pygame.draw.rect(self.screen, (0, 0, 0),
                         (self.text_x - 5, self.text_y - 5, self.text.get_width() + 10, self.text.get_height() + 10), 4)
        pygame.draw.rect(self.screen, (169, 169, 169),
                         (self.text_x - 5 + 4, self.text_y - 5 + 4, self.text.get_width() + 10 - 6,
                          self.text.get_height() + 10 - 6))
        self.screen.blit(self.text, self.coors)
        new_im = pygame.image.load(geroy)
        self.new_im = pygame.transform.scale(new_im, (int(self.width * 0.24), int(self.height * 0.45)))
        name = self.font_name.render(name, False, (169, 169, 169))
        tip = self.font_type.render(str(res[0][1]), False, (169, 169, 169))
        d = str(res[0][2]).split('. ')
        descr1 = self.font_descr.render(str(d[0] + '.'), False, (169, 169, 169))
        if len(d) > 1:
            descr2 = self.font_descr.render(str(d[1]), False, (169, 169, 169))
        else:
            descr2 = ''
        if len(d[0]) >= 100:
            self.coor_d_x1 = self.width * 0.2
        elif len(d[0]) >= 85:
            self.coor_d_x1 = self.width * 0.25
        else:
            self.coor_d_x1 = self.width * 0.33
        if len(d[1]) >= 100:
            self.coor_d_x2 = self.width * 0.2
        elif len(d[1]) >= 85:
            self.coor_d_x2 = self.width * 0.25
        else:
            self.coor_d_x2 = self.width * 0.33
        self.screen.blit(self.new_im, (self.coor_im_x, self.coor_im_y))
        self.screen.blit(name, (self.coor_n_x, self.coor_n_y))
        self.screen.blit(tip, (self.coor_t_x, self.coor_t_y))
        self.screen.blit(descr1, (self.coor_d_x1, self.coor_d_y1))
        self.screen.blit(descr2, (self.coor_d_x2, self.coor_d_y2))
        pygame.display.update()

if __name__ == '__main__':
    start = Menu()