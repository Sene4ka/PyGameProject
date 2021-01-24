import pygame
from screeninfo import get_monitors


class Death:
    def __init__(self):
        pygame.init()
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load('o_death.mp3')
        pygame.mixer.music.play(-1)
    def draw(self):
        pygame.display.set_caption('Supernatural: Team free will')
        size = width, height = int(str(get_monitors()[0]).split('width=')[1][:4]), \
                               int(str(get_monitors()[0]).split('height=')[1][:4]) - 76
        screen = pygame.display.set_mode(size)
        img = pygame.image.load("fon7.jpg")
        fon = pygame.transform.scale(img, (width, height))
        screen.blit(fon, (0, 0))
        font = pygame.font.SysFont('comic sans ms', 50)

        txt = font.render('Упс!', True, (255, 255, 255))
        txt2 = font.render('К сожалению, ты проиграл...', True, (255, 255, 255))
        txt3 = font.render('Хочешь сыграть еще раз?', True, (255, 255, 255))
        txt4 = font.render('Да', True, (0, 0, 0))

        txt_x = width // 2 - txt.get_width() // 2
        txt_x2 = width // 2 - txt2.get_width() // 2
        txt_x3 = width // 2 - txt3.get_width() // 2
        txt_x4 = width // 2 - txt4.get_width() // 2

        pygame.draw.rect(screen, (255, 255, 255), (txt_x4 - 10, int(height * 0.6), txt4.get_width() + 20,
                                             txt4.get_height()), 0)
        pygame.draw.rect(screen, (128, 128, 128), (txt_x4 - 10, int(height * 0.6),
                                                   txt4.get_width() + 20, txt4.get_height()), 4)

        screen.blit(txt, (txt_x, int(height * 0.1)))
        screen.blit(txt2, (txt_x2, int(height * 0.25)))
        screen.blit(txt3, (txt_x3, int(height * 0.5)))
        screen.blit(txt4, (txt_x4, int(height * 0.6)))

        pygame.display.flip()
        pygame.display.update()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos                
                    # Координваты границ кнопки
                    a = txt_x4 + txt4.get_width() + 10
                    b = int(height * 0.6) + txt4.get_height()
                    if int(width * 0.25) - 5 <= x <= a and int(height * 0.4) - 5 <= y <= b:
                        return "restart"


if __name__ == '__main__':
    pg = Death()
