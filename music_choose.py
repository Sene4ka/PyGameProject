import pygame
from screeninfo import get_monitors
from map2 import Map


class MusicChoose:
    def __init__(self, screen, hero):
        self.hero = hero
        # инициализирую pygame
        self.screen = screen
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()
        # заголовок окна
        pygame.display.set_caption('Supernatural: Team free will')
        # узнаю рамеру экрана пользователя с помощью get_monitors()
        size = width, height = int(str(get_monitors()[0]).split('width=')[1][:4]), \
                               int(str(get_monitors()[0]).split('height=')[1][:4]) - 76
        screen = pygame.display.set_mode(size)
        # фон
        bg = pygame.image.load("fon.jpg")
        screen.blit(bg, (0, 0))
        # устанавливаю шрифт для надписей
        font = pygame.font.SysFont('comic sans ms', 30)
        # устанавливаю шрифт для заголовка
        f = pygame.font.SysFont('comic sans ms', 50)
        text = f.render("Выбери свою любимую песню!", False, (0, 0, 0))
        # координаты заголовка
        text_x = width // 2 - text.get_width() // 2
        text_y = int(height * 0.1)
        # рамка и фон для заголовка
        pygame.draw.rect(screen, (0, 0, 0), (text_x - 5, text_y - 5, text.get_width() + 10, text.get_height() + 10), 4)
        pygame.draw.rect(screen, (169, 169, 169),
                         (text_x - 5 + 4, text_y - 5 + 4, text.get_width() + 10 - 6, text.get_height() + 10 - 6))
        screen.blit(text, (text_x, text_y))

        # кнопка для первой песни
        # название и исполнитель
        text1 = font.render("Heat Of The Moment", False, (169, 169, 169))
        text10 = font.render("Asia", False, (169, 169, 169))
        # координаты
        text1_x = int(width * 0.25)
        text1_y = int(height * 0.33)
        text10_x = int(width * 0.25) + text1.get_width() // 3
        text10_y = int(height * 0.33) + text1.get_height()
        # рамка и фон для "кнопки"
        pygame.draw.rect(screen, (169, 169, 169),
                         (text1_x - 5, text1_y - 5, text1.get_width() + 10,
                          text1.get_height() + text10.get_height() + 10), 4)
        pygame.draw.rect(screen, (0, 0, 0),
                         (text1_x - 5 + 3, text1_y - 5 + 3, text1.get_width() + 10 - 4,
                          text1.get_height() + text10.get_height() + 10 - 4))
        # вывожу на экран
        screen.blit(text1, (text1_x, text1_y))
        screen.blit(text10, (text10_x, text10_y))

        # кнопка для второй песни
        # название и исполнитель
        text2 = font.render("Fell On Black Days", False, (169, 169, 169))
        text20 = font.render("Soundgarden", False, (169, 169, 169))
        # координаты
        text2_x = text1_x + width * 0.05 + text1.get_width() + 1
        text2_y = int(height * 0.33)
        text20_x = text1_x + width * 0.05 + text2.get_width() // 5 + text1.get_width() + 1
        text20_y = int(height * 0.33) + text2.get_height()
        # рамка и фон для "кнопки"
        pygame.draw.rect(screen, (169, 169, 169),
                         (text2_x - 5, text2_y - 5, text2.get_width() + 10,
                          text2.get_height() + text20.get_height() + 10), 4)
        pygame.draw.rect(screen, (0, 0, 0),
                         (text2_x - 5 + 3, text2_y - 5 + 3, text2.get_width() + 10 - 4,
                          text2.get_height() + text20.get_height() + 10 - 4))
        # вывожу на экран
        screen.blit(text2, (text2_x, text2_y))
        screen.blit(text20, (text20_x, text20_y))

        # кнопка для третьей песни
        # название и исполнитель
        text3 = font.render("Highway To Hell", False, (169, 169, 169))
        text30 = font.render("AC/DC", False, (169, 169, 169))
        # координаты
        text3_x = text2_x + width * 0.05 + text2.get_width() + 1
        text3_y = int(height * 0.33)
        text30_x = text2_x + width * 0.05 + text3.get_width() // 3 + text2.get_width() + 1
        text30_y = int(height * 0.33) + text3.get_height()
        # рамка и фон для "кнопки"
        pygame.draw.rect(screen, (169, 169, 169),
                         (text3_x - 5, text3_y - 5, text3.get_width() + 10,
                          text3.get_height() + text30.get_height() + 10), 4)
        pygame.draw.rect(screen, (0, 0, 0),
                         (text3_x - 5 + 3, text3_y - 5 + 3, text3.get_width() + 10 - 4,
                          text3.get_height() + text30.get_height() + 10 - 4))
        # вывожу на экран
        screen.blit(text3, (text3_x, text3_y))
        screen.blit(text30, (text30_x, text30_y))

        # кнопка для четвёртой песни
        # название и исполнитель
        text4 = font.render("O, Death", False, (169, 169, 169))
        text40 = font.render("Len Titus", False, (169, 169, 169))
        # координаты
        text4_x = int(width * 0.25)
        text4_y = int(height * 0.5)
        text40_x = int(width * 0.25)
        text40_y = int(height * 0.5) + text4.get_height()
        # рамка и фон для "кнопки"
        pygame.draw.rect(screen, (169, 169, 169),
                         (text4_x - 5, text4_y - 5, text40.get_width() + 10,
                          text4.get_height() + text40.get_height() + 10), 4)
        pygame.draw.rect(screen, (0, 0, 0),
                         (text4_x - 5 + 3, text4_y - 5 + 3, text40.get_width() + 10 - 4,
                          text4.get_height() + text40.get_height() + 10 - 4))
        # вывожу на экран
        screen.blit(text4, (text4_x, text4_y))
        screen.blit(text40, (text40_x, text40_y))

        # кнопка для пятой песни
        # название и исполнитель
        text5 = font.render("God was Never On Your Side", False, (169, 169, 169))
        text50 = font.render("Motorhead", False, (169, 169, 169))
        # координаты
        text5_x = text4_x + width * 0.05 + text4.get_width() + 1
        text5_y = int(height * 0.5)
        text50_x = text4_x + width * 0.05 + text5.get_width() // 3.3 + text4.get_width() + 1
        text50_y = int(height * 0.5) + text4.get_height()
        # рамка и фон для "кнопки"
        pygame.draw.rect(screen, (169, 169, 169),
                         (text5_x - 5, text5_y - 5, text5.get_width() + 10,
                          text5.get_height() + text50.get_height() + 10), 4)
        pygame.draw.rect(screen, (0, 0, 0),
                         (text5_x - 5 + 3, text5_y - 2, text5.get_width() + 10 - 4,
                          text5.get_height() + text50.get_height() + 10 - 4))
        # вывожу на экран
        screen.blit(text5, (text5_x, text5_y))
        screen.blit(text50, (text50_x, text50_y))

        # кнопка для шестой песни
        # название и исполнитель
        text6 = font.render("Little Black Submarines", False, (169, 169, 169))
        text60 = font.render("The Black Keys", False, (169, 169, 169))
        # координаты
        text6_x = text5_x + width * 0.05 + text5.get_width() + 1
        text6_y = int(height * 0.5)
        text60_x = text5_x + width * 0.05 + text6.get_width() // 5 + text5.get_width() + 1
        text60_y = int(height * 0.5) + text4.get_height()
        # рамка и фон для "кнопки"
        pygame.draw.rect(screen, (169, 169, 169),
                         (text6_x - 5, text6_y - 5, text6.get_width() + 10,
                          text6.get_height() + text60.get_height() + 10), 4)
        pygame.draw.rect(screen, (0, 0, 0),
                         (text6_x - 2, text6_y - 2, text6.get_width() + 10 - 4,
                          text6.get_height() + text60.get_height() + 10 - 4))
        # вывожу на экран
        screen.blit(text6, (text6_x, text6_y))
        screen.blit(text60, (text60_x, text60_y))
        # обновляю экран
        pygame.display.update()
        running = True
        while running:
            for event in pygame.event.get():
                # если пользователь закрывает программу
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                # если нажимает куда-либо
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # позиция мышки
                    x, y = event.pos
                    # определение, попал ли пользователь на каую-либо кнопку и установка песни
                    if (text1_x - 5) <= x <= (text1_x - 5 + text1.get_width() + 1) \
                            and (text1_y - 5) <= y <= (text1_y - 5 + text1.get_height() + text10.get_height() + 10):
                        self.song = "heat_of_the_moment.mp3"
                        self.play_song()
                    elif (text2_x - 5) <= x <= (text2_x - 5 + text2.get_width() + 1) \
                            and (text2_y - 5) <= y <= (text2_y - 5 + text2.get_height() + text20.get_height() + 10):
                        self.song = "fell_on_black_days.mp3"
                        self.play_song()
                    elif (text3_x - 5) <= x <= (text3_x - 5 + text3.get_width() + 1) \
                            and (text3_y - 5) <= y <= (text3_y - 5 + text3.get_height() + text30.get_height() + 10):
                        self.song = "highway_to_hell.mp3"
                        self.play_song()
                    elif (text4_x - 5) <= x <= (text4_x - 5 + text4.get_width() + 1) \
                            and (text4_y - 5) <= y <= (text4_y - 5 + text4.get_height() + text40.get_height() + 10):
                        self.song = "o_death.mp3"
                        self.play_song()
                    elif (text5_x - 5) <= x <= (text5_x - 5 + text5.get_width() + 1) \
                            and (text5_y - 5) <= y <= (text5_y - 5 + text5.get_height() + text50.get_height() + 10):
                        self.song = "god_was_never.mp3"
                        self.play_song()
                    elif (text6_x - 5) <= x <= (text6_x - 5 + text6.get_width() + 1) \
                            and (text6_y - 5) <= y <= (text6_y - 5 + text6.get_height() + text60.get_height() + 10):
                        self.song = "little_black_submarines.mp3"
                        self.play_song()

    def play_song(self):
        points = 20
        map = Map()
        res = map.draw(self.screen, self.hero, self.song, points)
        pygame.display.update()


if __name__ == '__main__':
    # создаю экземпляр класса и показываю его
    start = MusicChoose()