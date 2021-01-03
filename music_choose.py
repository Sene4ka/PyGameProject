import pygame

class MusicChoose:
    def __init__(self):

        pygame.init()
        pygame.font.init()
        print(pygame.font.get_fonts())
        size = 1350, 720
        screen = pygame.display.set_mode(size)
        bg = pygame.image.load("fon3.jpg")
        screen.blit(bg, (0, 0))
        font = pygame.font.Font('C:\Windows\Fonts\Georgia.ttf', 15)
        f = pygame.font.Font('C:\Windows\Fonts\Georgia.ttf', 37)
        pygame.draw.rect(screen, (240, 255, 240), (405, 150, 500, 70))
        text = f.render("Choose Your Favourite Song", False, (0, 0, 0))
        coors = (420, 170)
        screen.blit(text, coors)

        pygame.draw.rect(screen, (240, 255, 240), (300, 300, 210, 100))
        text1 = font.render("Heat Of The Moment", False, (0, 0, 0))
        text10 = font.render("Asia", False, (0, 0, 0))
        coors1 = (335, 330)
        coors10 = (390, 360)
        screen.blit(text1, coors1)
        screen.blit(text10, coors10)

        pygame.draw.rect(screen, (240, 255, 240), (550, 300, 210, 100))
        text2 = font.render("Fell On Black Days", False, (0, 0, 0))
        text20 = font.render("Soundgarden", False, (0, 0, 0))
        coors2 = (590, 330)
        coors20 = (610, 360)
        screen.blit(text2, coors2)
        screen.blit(text20, coors20)

        pygame.draw.rect(screen, (240, 255, 240), (800, 300, 210, 100))
        text3 = font.render("Highway To Hell", False, (0, 0, 0))
        text30 = font.render("AC/DC", False, (0, 0, 0))
        coors3 = (845, 330)
        coors30 = (885, 360)
        screen.blit(text3, coors3)
        screen.blit(text30, coors30)

        pygame.draw.rect(screen, (240, 255, 240), (300, 450, 210, 100))
        text4 = font.render("O, Death", False, (0, 0, 0))
        text40 = font.render("Len Titus", False, (0, 0, 0))
        coors4 = (370, 480)
        coors40 = (375, 510)
        screen.blit(text4, coors4)
        screen.blit(text40, coors40)

        pygame.draw.rect(screen, (240, 255, 240), (550, 450, 210, 100))
        text5 = font.render("God was Never On Your Side", False, (0, 0, 0))
        text50 = font.render("Soundgarden", False, (0, 0, 0))
        coors5 = (563, 480)
        coors50 = (610, 510)
        screen.blit(text5, coors5)
        screen.blit(text50, coors50)

        pygame.draw.rect(screen, (240, 255, 240), (800, 450, 210, 100))
        text6 = font.render("Little Black Submarines", False, (0, 0, 0))
        text60 = font.render("The Black Keys", False, (0, 0, 0))
        coors6 = (835, 480)
        coors60 = (865, 510)
        screen.blit(text6, coors6)
        screen.blit(text60, coors60)

        pygame.display.update()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if 400 <= x <= 500 and 300 <= y <= 400:
                        clas = HeatOfTheMoment()
                        clas.show()
                    elif 600 <= x <= 700 and 300 <= y <= 400:
                        clas = FellOnBlackDays()
                        clas.show()
                    elif 800 <= x <= 900 and 300 <= y <= 400:
                        clas = HighwayToHell()
                        clas.show()
                    elif 400 <= x <= 500 and 450 <= y <= 550:
                        clas = ODeath()
                        clas.show()
                    elif 600 <= x <= 700 and 450 <= y <= 550:
                        clas = GodWasNever()
                        clas.show()
                    elif 800 <= x <= 900 and 450 <= y <= 550:
                        clas = BlackSubmarines()
                        clas.show()
        pygame.quit()
if __name__ == '__main__':
    start = MusicChoose()
    start.show()
