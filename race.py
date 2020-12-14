import pygame

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
startButton = pygame.Rect(100,100,50,50)


#starts race
def startRace():
    global p1x
    while (p1x<100):
        p1x+=1
        win.blit(images[0],(p1x,p2y))
        pygame.display.flip()

#keeps the game going
run = True
p1x, p2y =  0,0
while run:
    clock.tick(FPS)
    win.fill(GREEN)
    win.blit(images[0],(p1x,p2y))
    pygame.draw.rect(win, (200,0,0),startButton)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            #will start race
            if startButton.collidepoint(pos):
                startRace()


pygame.quit()