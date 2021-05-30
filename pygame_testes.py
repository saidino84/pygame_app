import pygame
pygame.init()

win =pygame.display.set_mode( (200,300))
pygame.display.set_caption("Teste")
# label=
running= True
while running:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        print(event)