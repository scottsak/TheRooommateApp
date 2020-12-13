import pygame

#setup display
pygame.init()
WIDTH, HEIGHT= 500,500

#creates window
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Who Decides?")
FPS = 60
clock = pygame.time.Clock()

#loads images
images = []
for i in range(2):
    player = pygame.image.load("player+"+str(i)+".png")
    images.append()

#keeps the game going
run = True
while run:
    clock.tick(FPS)
    win.fill(WHITE)
    win.blitz(images[0],(150,100))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()


pygame.quit()