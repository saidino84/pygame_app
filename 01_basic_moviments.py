import pygame

pygame.init()

win=pygame.display.set_mode( (500,500))
pygame.display.set_caption("First Game")

x=50
y=50
w=40
h=60
vel =5 
run =True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x-=vel
    if keys[pygame.K_RIGHT]:
        x +=vel
    if keys[pygame.K_DOWN]:
        y +=vel
    if keys[pygame.K_UP]:
        y -=vel
    # cor do fundo
    win.fill((45,12,34))
    # desnhar um rectang( precisamos de tres parametros(1-ctx, 2(cor-rgb) 3=[medidas do rectangulo])
    # drawing a rect angle( surface:{where you want to draw[in this case is in the displa]}, color, rect_[x,y,w,h]
    pygame.draw.rect(win,(255,0,0),(x,y,w,h))
    # to display the designs we need to update de display
    pygame.display.update()
pygame.quit()
