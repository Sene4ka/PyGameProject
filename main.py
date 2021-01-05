import pygame
from menu import Menu
from map import Map
from hero import Hero
from enemy import Enemy

pygame.init()
BLACK = (0, 0, 0)
size = 1350, 720
screen = pygame.display.set_mode(size)
bg = pygame.image.load("fon.png")
button = pygame.image.load("button_start.png")
button.set_colorkey(BLACK)
button.convert_alpha()
loc = (540, 410)
screen.fill((0, 0, 0))
screen.blit(bg, (0, 0))
screen.blit(button, loc)
pygame.display.update()
running = True
checking = True
menu = Menu(screen)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 540 <= x <= 720 and 410 <= y <= 690 and checking:
                print(x, y)
                menu.draw()
                checking = False
    pygame.display.flip()
pygame.quit()