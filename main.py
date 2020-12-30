import pygame
from menu import Menu
from map import Map
from hero import Hero
from enemy import Enemy

pygame.init()
size = width, height = 800, 800
screen = pygame.display.set_mode(size)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()