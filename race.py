import pygame
import random

#setup display
pygame.init()
WIDTH, HEIGHT= 1000,1000
GREEN = (75,139,59)

#creates window
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Who Decides?")
FPS = 60
clock = pygame.time.Clock()

#loads images
images = []
for i in range(2):
    player = pygame.image.load("player"+str(i)+".png")
    player = pygame.transform.scale(player, (200, 200))
    images.append(player)

#creates buttons
startButton = pygame.Rect(500,500,50,50)

#creates finish line
finishlineY = 0
def createFinishLine():
    global win
    global HEIGHT
    white=True
    global finishlineY
    i=0
    for i in range(HEIGHT):
        if white:
            pygame.draw.rect(win, (255,255,255), pygame.Rect(500,finishlineY,50,50))
            white = False
        else:
            pygame.draw.rect(win,(0,0,0),pygame.Rect(500,finishlineY,50,50))
            white = True
        i +=50
        finishlineY +=50


#keeps the game going
run = True
p1y,p2y = 0,200
p1x,p2x = 0,0

while run:
    clock.tick(FPS)
    win.fill(GREEN)
    win.blit(images[0],(p1x,p1y))
    win.blit(images[1],(p2x,p2y))
    pygame.draw.rect(win, (200,0,200),startButton)
    #createFinishLine()

    pygame.display.update()

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            run = False
        if ev.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            #will start race
            if startButton.collidepoint(pos):
                p1x,p2x=0,0
                win.blit(images[0],(p1x,p1y))
                win.blit(images[1],(p2x,p2y))
                while(p1x<500):
                    p1x+=random.randint(0,5)
                    p2x+= random.randint(0,5)
                    win.fill(GREEN)
                    createFinishLine()
                    win.blit(images[0],(p1x,p1y))
                    win.blit(images[1],(p2x,p2y))
                    pygame.display.update()
pygame.quit()