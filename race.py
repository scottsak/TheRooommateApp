import pygame
import random

#setup display
pygame.init()
WIDTH, HEIGHT= 1000,1000
GREEN = (75,139,59)
WHITE = (255,255,255)

#creates window
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Who Decides?")
FPS = 30
clock = pygame.time.Clock()

#loads images
images = []
for i in range(2):
    player = pygame.image.load("player"+str(i)+".png")
    player = pygame.transform.scale(player, (200, 200))
    images.append(player)

#creates finish line
finishline = pygame.image.load("finishline.png")
finishline = pygame.transform.rotate(finishline,270)
finishline = pygame.transform.scale(finishline,(200,1000))

#creates buttons
startButton = pygame.Rect(100,800,300,50)
    

#creates background
def createBackground():
    global p1x, p2x
    win.fill(GREEN)
    win.blit(images[0],(p1x,p1y))
    win.blit(images[1],(p2x,p2y))
    win.blit(finishline,(800,0))
    bfont = pygame.font.Font("freesansbold.ttf",50)
    text = bfont.render('Start',True,WHITE)
    #textSurf,button = text_objects("GO!", bfont)
    #win.blit(textSurf, button)
    pygame.draw.rect(win, (200,0,200),startButton)
    win.blit(text,(192,803))
    pygame.display.flip()


#keeps the game going
run = True
racing = False
p1y,p2y = 0,200
p1x,p2x = 0,0

while run:
    clock.tick(FPS)
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            run = False
        if ev.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)

            #will start race
            if startButton.collidepoint(pos):
                racing = True
                p1x,p2x = 0,0

    if racing == True:
        if(p1x < 800 and p2x < 800):
            p1x+=random.randint(0,1)
            p2x+= random.randint(0,10)
        else:
            racing=False

    createBackground()

pygame.quit()