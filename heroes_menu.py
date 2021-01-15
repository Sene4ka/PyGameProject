import pygame
import sqlite3
from Winchester import WinchesterChoose
# модуль, позволяющий нам узнать размеры экрана
from screeninfo import get_monitors


class Menu:
    def __init__(self):
        # инициализируем pygame
        pygame.init()
        pygame.font.init()
        # переменная, с помощью которой отслеживается номер героя, о котором читает пользователь
        self.count = 0

    def draw(self, screen):
        pygame.display.set_caption('Supernatural: Team free will')
        # узнаю рамеру экрана пользователя с помощью get_monitors()
        size = self.width, self.height = int(str(get_monitors()[0]).split('width=')[1][:4]), \
                                         int(str(get_monitors()[0]).split('height=')[1][:4]) - 76
        self.screen = screen
        # загружаю фон
        bg = pygame.image.load("fon.jpg")
        # меняю рамер изображения фона под размеры экрана
        self.bg = pygame.transform.scale(bg, (self.width, self.height))
        # загружаю картинку кнопки-стрелочки вправо
        self.kn1 = pygame.image.load("Knopka.png")
        # загружаю картинку кнопки-стрелочки влево
        self.kn2 = pygame.image.load("Knopka2.png")
        # вывожу их на экран
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.kn2, (self.width * 0.3, self.height * 0.5))
        # все координаты подсчитываются в процентном виде, чтобы на любом экране интерфейс выглядел одинаково
        self.screen.blit(self.kn1, (self.width * 0.7, self.height * 0.5))
        # шрифт для заголовка
        f = pygame.font.SysFont('comic sans ms', 50)
        # соединение с бд
        self.con = sqlite3.connect("spn.db")
        self.cur = self.con.cursor()
        # создаю список с названиями файлов, в которых находятся картинки героев
        self.heroes = ['Meg.png', 'Leviafan.png', 'Castiel.png', 'Bobby.png', 'Azazel.png']
        # заголовок
        self.text = f.render("Познакомься с героями!", False, (0, 0, 0))
        # его координаты, расчитывающиеся в общем виде
        # get_width() - узнаем размер текста
        self.text_x = self.width // 2 - self.text.get_width() // 2
        self.text_y = int(self.height * 0.1)
        self.coors = (self.text_x, self.text_y)
        # рамка для заголовка
        pygame.draw.rect(self.screen, (0, 0, 0),
                         (self.text_x - 5, self.text_y - 5, self.text.get_width() + 10, self.text.get_height() + 10), 4)
        # фон для заголовка
        pygame.draw.rect(self.screen, (169, 169, 169),
                         (self.text_x - 5 + 4, self.text_y - 5 + 4,
                          self.text.get_width() + 10 - 6, self.text.get_height() + 10 - 6))
        self.screen.blit(self.text, self.coors)
        self.next = f.render("Далее", False, (0, 0, 0))
        # координаты
        self.text_next1 = self.width // 2 - self.next.get_width() // 2
        self.text_next2 = int(self.height * 0.2)
        # рамка и фон для заголовка
        pygame.draw.rect(self.screen, (0, 0, 0), (self.text_next1 - 5, self.text_next2 - 5, self.next.get_width() + 10,
                                                  self.next.get_height() + 10), 4)
        pygame.draw.rect(self.screen, (169, 169, 169),
                         (self.text_next1 - 5 + 4, self.text_next2 - 5 + 4, self.next.get_width() + 10 - 6,
                          self.next.get_height() + 10 - 6))
        self.screen.blit(self.next, (self.text_next1, self.text_next2))
        # название первого героя
        geroy = self.heroes[self.count]
        # выбираю полное описание из таблицы Heroes по имени файла
        res = self.cur.execute("""SELECT * FROM Heroes
                                  WHERE Hero = '{}'""".format(geroy)).fetchall()
        # загружаю картинку и изменяю ее размер
        new_im = pygame.image.load(geroy)
        self.new_im = pygame.transform.scale(new_im, (int(self.width * 0.18), int(self.height * 0.45)))
        # устанавливаю шрифты для всех подписей под картинкой героя
        self.font_name = pygame.font.SysFont('comic sans ms', 50)
        self.font_type = pygame.font.SysFont('comic sans ms', 37)
        self.font_descr = pygame.font.SysFont('comic sans ms', 20)
        name = self.font_name.render('Мэг', False, (169, 169, 169))
        # беру тип героя из результата поиска по таблице в бд
        tip = self.font_type.render(str(res[0][1]), False, (169, 169, 169))
        # делю краткое описание героя на несколько предложений
        d = str(res[0][2]).split('. ')
        # беру описание героя из результата поиска по таблице в бд (1 предложение)
        descr1 = self.font_descr.render(str(d[0] + '.'), False, (169, 169, 169))
        # если предложений несколько:
        if len(d) > 1:
            descr2 = self.font_descr.render(str(d[1]), False, (169, 169, 169))
        else:
            descr2 = ''
        # устанавливаю координаты для каждой подписи
        self.coor_im_x = self.width * 0.41
        self.coor_im_y = self.height * 0.3
        self.coor_n_x = self.width // 2 - name.get_width() // 2
        self.coor_n_y = self.height * 0.75
        self.coor_t_x = self.width // 2 - tip.get_width() // 2
        self.coor_t_y = self.height * 0.8
        self.coor_d_x1 = self.width // 2 - descr1.get_width() // 2
        self.coor_d_x2 = self.width // 2 - descr2.get_width() // 2
        self.coor_d_y1 = self.height * 0.85
        self.coor_d_y2 = self.height * 0.87
        # вывожу на экран
        self.screen.blit(self.new_im, (self.coor_im_x, self.coor_im_y))
        self.screen.blit(name, (self.coor_n_x, self.coor_n_y))
        self.screen.blit(tip, (self.coor_t_x, self.coor_t_y))
        self.screen.blit(descr1, (self.coor_d_x1, self.coor_d_y1))
        self.screen.blit(descr2, (self.coor_d_x2, self.coor_d_y2))
        # обновляю экран
        pygame.display.update()
        running = True
        res = True
        menu = WinchesterChoose()
        while running:
            for event in pygame.event.get():
                # если пользователь закрывает программу
                if event.type == pygame.QUIT:
                    return False
                # если нажимает куда-либо
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    # нажатие на кнпоку "следующий"
                    if self.width * 0.7 <= x <= (self.width * 0.7 + self.kn1.get_width()) and self.height * 0.5 <= y <= (self.height * 0.5 + self.kn1.get_height()):
                        self.count += 1
                        # вызов функции, обновляющей героя
                        self.new_hero()
                    # нажатие на кнпоку "предыдущий"
                    elif self.width * 0.3 <= x <= (self.width * 0.3 + self.kn2.get_width()) and self.height * 0.5 <= y <= (self.height * 0.5 + self.kn2.get_height()):
                        self.count -= 1
                        # вызов функции, обновляющей героя
                        self.new_hero()
                    elif self.text_next1 <= x <= (self.text_next1 + self.next.get_width()) and self.text_next2 <= y <= (self.text_next2 + self.next.get_height()):
                        res = menu.draw(self.screen)
                if not res:
                    return False


    def new_hero(self):
        # номер героя в списке
        num = self.count % 5
        # название его файла
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
        # выбор описание героя из таблицы
        res = self.cur.execute("""SELECT * FROM Heroes
                                  WHERE Hero = '{}'""".format(geroy)).fetchall()
        # вывод на экран
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.kn2, (self.width * 0.3, self.height * 0.5))
        self.screen.blit(self.kn1, (self.width * 0.7, self.height * 0.5))
        # оформление заголовка
        pygame.draw.rect(self.screen, (0, 0, 0),
                         (self.text_x - 5, self.text_y - 5, self.text.get_width() + 10, self.text.get_height() + 10), 4)
        pygame.draw.rect(self.screen, (169, 169, 169),
                         (self.text_x - 5 + 4, self.text_y - 5 + 4, self.text.get_width() + 10 - 6,
                          self.text.get_height() + 10 - 6))
        self.screen.blit(self.text, self.coors)
        # почти то же самое, что в начале кода
        new_im = pygame.image.load(geroy)
        self.new_im = pygame.transform.scale(new_im, (int(self.width * 0.2), int(self.height * 0.45)))
        n = name
        name = self.font_name.render(name, False, (169, 169, 169))
        tip = self.font_type.render(str(res[0][1]), False, (169, 169, 169))
        d = str(res[0][2]).split('. ')
        descr1 = self.font_descr.render(str(d[0] + '.'), False, (169, 169, 169))
        if len(d) > 1:
            descr2 = self.font_descr.render(str(d[1]), False, (169, 169, 169))
        else:
            descr2 = ''
        self.coor_n_x = self.width // 2 - name.get_width() // 2
        self.coor_t_x = self.width // 2 - tip.get_width() // 2
        self.coor_d_x1 = self.width // 2 - descr1.get_width() // 2
        self.coor_d_x2 = self.width // 2 - descr2.get_width() // 2
        # для имени "Мэг" опр. координаты, так как оно очень короткое
        if n == 'Мэг':
            self.coor_n_x = self.width * 0.48
        else:
            self.coor_n_x = self.width * 0.45
        pygame.draw.rect(self.screen, (0, 0, 0), (self.text_next1 - 5, self.text_next2 - 5, self.next.get_width() + 10,
                                                  self.next.get_height() + 10), 4)
        pygame.draw.rect(self.screen, (169, 169, 169),
                         (self.text_next1 - 5 + 4, self.text_next2 - 5 + 4, self.next.get_width() + 10 - 6,
                          self.next.get_height() + 10 - 6))
        # вывод на экран
        self.screen.blit(self.next, (self.text_next1, self.text_next2))
        self.screen.blit(self.new_im, (self.coor_im_x, self.coor_im_y))
        self.screen.blit(name, (self.coor_n_x, self.coor_n_y))
        self.screen.blit(tip, (self.coor_t_x, self.coor_t_y))
        self.screen.blit(descr1, (self.coor_d_x1, self.coor_d_y1))
        self.screen.blit(descr2, (self.coor_d_x2, self.coor_d_y2))
        # обновления экрана
        pygame.display.update()


if __name__ == '__main__':
    # создаю экземпляр класса и показываю его
    start = Menu()
