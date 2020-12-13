import pygame

#setup display
pygame.init()
WIDTH, HEIGHT= 1000,1000

#creates window
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Who Decides?")
FPS = 60
clock = pygame.time.Clock()

#loads images
images = []
for i in range(2):
    player = pygame.image.load("player"+str(i)+".png")
    player = pygame.transform.rotozoom(player, 0, 5)
    images.append(player)

#keeps the game going
run = True
while run:
    clock.tick(FPS)
    win.fill((255,255,255))
    win.blit(images[0],(1,1))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)


pygame.quit()