import pygame
from Winchester import WinchesterChoose
from screeninfo import get_monitors

pygame.init()
pygame.display.set_caption('Supernatural: Team free will')
BLACK = (0, 0, 0)
size = width, height = int(str(get_monitors()[0]).split('width=')[1][:4]), \
                    int(str(get_monitors()[0]).split('height=')[1][:4]) - 76
screen = pygame.display.set_mode(size)
bg = pygame.image.load("fon.png")
fon = pygame.transform.scale(bg, (width, height))
button = pygame.image.load("button_start.png")
button.set_colorkey(BLACK)
button.convert_alpha()
loc = (width * 0.43, height * 0.6)
screen.fill((0, 0, 0))
screen.blit(fon, (0, 0))
screen.blit(button, loc)
pygame.display.update()
running = True
checking1 = True
checking2 = False
menu = WinchesterChoose()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if width * 0.43 <= x <= width * 0.6 and height * 0.61 <= y <= height * 0.85 and checking1:
                menu.draw(screen)
                checking1 = False
    pygame.display.flip()
pygame.quit()
