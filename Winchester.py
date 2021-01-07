import pygame
from screeninfo import get_monitors
print(get_monitors())


class WinchesterChoose:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Supernatural: Team free will')
        size = width, height = int(str(get_monitors()[0]).split('width=')[1][:4]), \
                               int(str(get_monitors()[0]).split('height=')[1][:4]) - 76
        screen = pygame.display.set_mode(size)
        fon = pygame.image.load("fon.jpg")
        screen.blit(fon, (0, 0))
        font = pygame.font.SysFont('comic sans ms', 50)
        txt = font.render('Выберите своего героя', True, (169, 169, 169))
        txt_x = width // 2 - txt.get_width() // 2
        txt_y = int(height * 0.1)
        pygame.draw.rect(screen, (169, 169, 169), (txt_x, txt_y, txt.get_width() + 1, txt.get_height()), 4)
        screen.blit(txt, (txt_x, txt_y))
        pygame.display.flip()

        txt2 = font.render('Дин', True, (169, 169, 169))
        pygame.draw.rect(screen, (0, 0, 0), (int(width * 0.25) - 5, int(height * 0.4) - 5,
                                             txt2.get_width() + 10, txt2.get_height() + 10), 0)
        pygame.draw.rect(screen, (169, 169, 169), (int(width * 0.25) - 5, int(height * 0.4) - 5,
                                                   txt2.get_width() + 10, txt2.get_height() + 10), 3)
        screen.blit(txt2, (int(width * 0.25), int(height * 0.4)))

        txt3 = font.render('Cэм', True, (169, 169, 169))
        pygame.draw.rect(screen, (0, 0, 0), (int(width * 0.75) - 5, int(height * 0.4) - 5,
                                             txt3.get_width() + 10, txt3.get_height() + 10), 0)
        pygame.draw.rect(screen, (169, 169, 169), (int(width * 0.75) - 5, int(height * 0.4) - 5,
                                             txt3.get_width() + 10, txt3.get_height() + 10), 3)
        screen.blit(txt3, (int(width * 0.75), int(height * 0.4)))

        sam_dean = pygame.image.load("Sam and Dean.png")
        x, y = sam_dean.get_size()
        sam_dean_x = int(width * 0.5) - x // 2
        sam_dean_y = int(height * 0.5) - y // 2
        screen.blit(sam_dean, (sam_dean_x, sam_dean_y))
        pygame.display.update()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if 270 <= x <= 365 and 340 <= y <= 400:
                        hero = Game('Dean')
                        hero.show()
                    elif 890 <= x <= 980 and 340 <= y <= 400:
                        hero = Game('Sam')
                        hero.show()
        pygame.display.update()


if __name__ == '__main__':
    q = WinchesterChoose()
    q.show()
    pygame.quit()
