import pygame
import sys

class Race(object):
    def __init__(self):
        pygame.init()
        res = (720,720)
        self.screen = pygame.display.set_mode(res)
        self.height= self.screen.get_height()
        self.width = self.screen.get_width()
        self.players = []
   
    def startRace():
        while True:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    if self.width/2 <= mouse[0] <= self.width/2+140 and self.height/2 <=mouse[1] <= self.height/2+40:
                        pygame.quit()

            self.screen.fill((255,255,255))

            mouse = pygame.mouse.get_pos()
            # if mouse is hovered on a button it 
            # changes to lighter shade  
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
                pygame.draw.rect(screen,color_light,[width/2,height/2,140,40]) 
                
            else: 
                pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40]) 
            
            # superimposing the text onto our button 
            screen.blit(text , (width/2+50,height/2)) 
            pygame.display.update()

    #creates players
    def createPlayer(self,player):
        self.players.add(player)

    

race = Race()
race.startRace
