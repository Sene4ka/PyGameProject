import pygame
from heroes_menu import Menu
# модуль, позволяющий нам узнать размеры экрана
from screeninfo import get_monitors

# инициализирую pygame
pygame.init()
# заголовок окна
pygame.display.set_caption('Supernatural: Team free will')
BLACK = (0, 0, 0)
# размеры окна с помощью get_monitors
size = width, height = int(str(get_monitors()[0]).split('width=')[1][:4]), \
                       int(str(get_monitors()[0]).split('height=')[1][:4]) - 76
screen = pygame.display.set_mode(size)
# фон (заставка игры)
bg = pygame.image.load("fon.png")
# меняю размеры фона под размеры экрана
fon = pygame.transform.scale(bg, (width, height))
# ззагружаю картинку кнопки
button = pygame.image.load("button_start.png")
# заглушаю в ней черный цвет
button.set_colorkey(BLACK)
button.convert_alpha()
# размещаю по центру экрана
loc = (width * 0.43, height * 0.6)
# помещаю все в окно
screen.fill((0, 0, 0))
screen.blit(fon, (0, 0))
screen.blit(button, loc)
# обновляю экран
pygame.display.update()
running = True
checking1 = True
checking2 = False
# экземпляр класса выбра своего игрока
while running:
    for event in pygame.event.get():
        # если пользователь закрывает программу
        if event.type == pygame.QUIT:
            running = False
        # если нажимает куда-либо
        if event.type == pygame.MOUSEBUTTONDOWN:
            # позиция нажатия мыши
            x, y = event.pos
            # если нажата кнопка
            if width * 0.43 <= x <= width * 0.6 and height * 0.61 <= y <= height * 0.85 and checking1:
                # запускаю выбор героя
                Menu().draw(screen)
                checking1 = False
    pygame.display.flip()
pygame.quit()