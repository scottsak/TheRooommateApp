import pygame
import sys



class Menu(object):
    def __init__(self):
        pygame.init()
        res = (720,720)
        print("hello")
        self.screen = pygame.display.set_mode(res)
        self.height= self.screen.get_height()
        self.width = self.screen.get_width()

    def getMenu(self):
        while True:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    if self.width/2 <= mouse[0] <= self.width/2+140 and self.height/2 <=mouse[1] <= self.height/2+40:
                        pygame.quit()

            self.screen.fill((255,255,255))

            mouse = pygame.mouse.get_pos()
            pygame.display.update()
              
menu = Menu()
menu.getMenu()     
