import pygame
from screeninfo import get_monitors

class MusicChoose:
    def __init__(self):

        pygame.init()
        pygame.font.init()
        pygame.display.set_caption('Supernatural: Team free will')
        size = width, height = int(str(get_monitors()[0]).split('width=')[1][:4]), \
                               int(str(get_monitors()[0]).split('height=')[1][:4]) - 76
        screen = pygame.display.set_mode(size)
        bg = pygame.image.load("fon.jpg")
        screen.blit(bg, (0, 0))
        font = pygame.font.SysFont('comic sans ms', 30)
        f = pygame.font.SysFont('comic sans ms', 50)
        text = f.render("Выбери свою любимую песню!", False, (0, 0, 0))
        text_x = width // 2 - text.get_width() // 2
        text_y = int(height * 0.1)
        pygame.draw.rect(screen, (0, 0, 0), (text_x - 5, text_y - 5, text.get_width() + 10, text.get_height() + 10), 4)
        pygame.draw.rect(screen, (169, 169, 169), (text_x - 5 + 4, text_y - 5 + 4, text.get_width() + 10 - 6, text.get_height() + 10 - 6))
        screen.blit(text, (text_x, text_y))

        text1 = font.render("Heat Of The Moment", False, (169, 169, 169))
        text10 = font.render("Asia", False, (169, 169, 169))
        text1_x = int(width * 0.25)
        text1_y = int(height * 0.33)
        text10_x = int(width * 0.25) + text1.get_width() // 3
        text10_y = int(height * 0.33) + text1.get_height()
        pygame.draw.rect(screen, (169, 169, 169),
                         (text1_x - 5, text1_y - 5, text1.get_width() + 10, text1.get_height() + text10.get_height() + 10), 4)
        pygame.draw.rect(screen, (0, 0, 0),
                         (text1_x - 5 + 3, text1_y - 5 + 3, text1.get_width() + 10 - 4, text1.get_height() + text10.get_height() + 10 - 4))
        screen.blit(text1, (text1_x, text1_y))
        screen.blit(text10, (text10_x, text10_y))

        text2 = font.render("Fell On Black Days", False, (169, 169, 169))
        text20 = font.render("Soundgarden", False, (169, 169, 169))
        text2_x = text1_x + width * 0.05 + text1.get_width() + 1
        text2_y = int(height * 0.33)
        text20_x = text1_x + width * 0.05 + text2.get_width() // 5 + text1.get_width() + 1
        text20_y = int(height * 0.33) + text2.get_height()
        pygame.draw.rect(screen, (169, 169, 169),
                         (text2_x - 5, text2_y - 5, text2.get_width() + 10, text2.get_height() + text20.get_height() + 10), 4)
        pygame.draw.rect(screen, (0, 0, 0),
                         (text2_x - 5 + 3, text2_y - 5 + 3, text2.get_width() + 10 - 4, text2.get_height() + text20.get_height() + 10 - 4))
        screen.blit(text2, (text2_x, text2_y))
        screen.blit(text20, (text20_x, text20_y))

        text3 = font.render("Highway To Hell", False, (169, 169, 169))
        text30 = font.render("AC/DC", False, (169, 169, 169))
        text3_x = text2_x + width * 0.05 + text2.get_width() + 1
        text3_y = int(height * 0.33)
        text30_x = text2_x + width * 0.05 + text3.get_width() // 3 + text2.get_width() + 1
        text30_y = int(height * 0.33) + text3.get_height()
        pygame.draw.rect(screen, (169, 169, 169),
                         (text3_x - 5, text3_y - 5, text3.get_width() + 10, text3.get_height() + text30.get_height() + 10), 4)
        pygame.draw.rect(screen, (0, 0, 0),
                         (text3_x - 5 + 3, text3_y - 5 + 3, text3.get_width() + 10 - 4, text3.get_height() + text30.get_height() + 10 - 4))
        screen.blit(text3, (text3_x, text3_y))
        screen.blit(text30, (text30_x, text30_y))

        text4 = font.render("O, Death", False, (169, 169, 169))
        text40 = font.render("Len Titus", False, (169, 169, 169))
        text4_x = int(width * 0.25)
        text4_y = int(height * 0.5)
        text40_x = int(width * 0.25)
        text40_y = int(height * 0.5) + text4.get_height()
        pygame.draw.rect(screen, (169, 169, 169),
                         (text4_x - 5, text4_y - 5, text40.get_width() + 10, text4.get_height() + text40.get_height() + 10), 4)
        pygame.draw.rect(screen, (0, 0, 0),
                         (text4_x - 5 + 3, text4_y - 5 + 3, text40.get_width() + 10 - 4, text4.get_height() + text40.get_height() + 10 - 4))
        screen.blit(text4, (text4_x, text4_y))
        screen.blit(text40, (text40_x, text40_y))

        text5 = font.render("God was Never On Your Side", False, (169, 169, 169))
        text50 = font.render("Motorhead", False, (169, 169, 169))
        text5_x = text4_x + width * 0.05 + text4.get_width() + 1
        text5_y = int(height * 0.5)
        text50_x = text4_x + width * 0.05 + text5.get_width() // 3.3 + text4.get_width() + 1
        text50_y = int(height * 0.5) + text4.get_height()
        pygame.draw.rect(screen, (169, 169, 169),
                         (text5_x - 5, text5_y - 5, text5.get_width() + 10, text5.get_height() + text50.get_height() + 10), 4)
        pygame.draw.rect(screen, (0, 0, 0),
                         (text5_x - 5 + 3, text5_y - 2, text5.get_width() + 10 - 4, text5.get_height() + text50.get_height() + 10 - 4))
        screen.blit(text5, (text5_x, text5_y))
        screen.blit(text50, (text50_x, text50_y))

        text6 = font.render("Little Black Submarines", False, (169, 169, 169))
        text60 = font.render("The Black Keys", False, (169, 169, 169))
        text6_x = text5_x + width * 0.05 + text5.get_width() + 1
        text6_y = int(height * 0.5)
        text60_x = text5_x + width * 0.05 + text6.get_width() // 3.3 + text5.get_width() + 1
        text60_y = int(height * 0.5) + text4.get_height()
        pygame.draw.rect(screen, (169, 169, 169),
                         (text6_x - 5, text6_y - 5, text6.get_width() + 10, text6.get_height() + text60.get_height() + 10), 4)
        pygame.draw.rect(screen, (0, 0, 0),
                         (text6_x - 2, text6_y - 2, text6.get_width() + 10 - 4, text6.get_height() + text60.get_height() + 10 - 4))
        screen.blit(text6, (text6_x, text6_y))
        screen.blit(text60, (text60_x, text60_y))

        pygame.display.update()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if (text1_x - 5) <= x <= (text1_x - 5 + text1.get_width() + 1) \
                            and (text1_y - 5) <= y <= (text1_y - 5 + text1.get_height() + text10.get_height() + 10):
                        self.song = "heat_of_the_moment.mp3"
                    elif (text2_x - 5) <= x <= (text2_x - 5 + text2.get_width() + 1) \
                            and (text2_y - 5) <= y <= (text2_y - 5 + text2.get_height() + text20.get_height() + 10):
                        self.song = "fell_on_black_days.mp3"
                    elif (text3_x - 5) <= x <= (text3_x - 5 + text3.get_width() + 1) \
                            and (text3_y - 5) <= y <= (text3_y - 5 + text3.get_height() + text30.get_height() + 10):
                        self.song = "highway_to_hell.mp3"
                    elif (text4_x - 5) <= x <= (text4_x - 5 + text4.get_width() + 1) \
                            and (text4_y - 5) <= y <= (text4_y - 5 + text4.get_height() + text40.get_height() + 10):
                        self.song = "o_death.mp3"
                    elif (text5_x - 5) <= x <= (text5_x - 5 + text5.get_width() + 1) \
                            and (text5_y - 5) <= y <= (text5_y - 5 + text5.get_height() + text50.get_height() + 10):
                        self.song = "god_was_never.mp3"
                    elif (text6_x - 5) <= x <= (text6_x - 5 + text6.get_width() + 1) \
                            and (text6_y - 5) <= y <= (text6_y - 5 + text6.get_height() + text60.get_height() + 10):
                        self.song = "little_black_submarines.mp3"
        pygame.quit()
if __name__ == '__main__':
    start = MusicChoose()
