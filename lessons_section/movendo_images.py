import os, pygame
os.chdir(os.path.dirname(__file__))

pygame.init()


screen=pygame.display.set_mode((600,400))
pygame.display.set_caption("moving sprites")
bg=pygame.image.load("1-color-spectrum.png")
img=pygame.image.load("bug.png")





def main():
    clock=pygame.time.Clock()
    run=True

    while run:
        screen.blit(bg,[0,0])
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()