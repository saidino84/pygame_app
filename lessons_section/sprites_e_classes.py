import pygame,os,sys
from PIL import Image


# img=Image.open('lessons_section/sprites/bg.png')
img=""
if os.path.exists('lessons_section/sprites/bg.png'):
    img='lessons_section/sprites/bg.png'
else:
    img='sprites/bg.png'
# print(img.size)
# img.show()

pygame.init()
g_width=540
g_height=600
surface=pygame.display.set_mode((g_width,g_height))
title=pygame.display.set_caption("Sprites vs Classes")
bg=pygame.image.load(img).convert()
clock=pygame.time.Clock()

def game_loop():
    run=True
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                pygame.quit()
                quit()
        surface.blit(bg,(0,0))
        pygame.display.flip()
        clock.tick(60)

                


game_loop()