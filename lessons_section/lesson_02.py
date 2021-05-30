from typing import List
import pygame,os
from pprint import pprint
from PIL import Image
from time import sleep
from random import randint
# os.chdir=os.path.abspath(__file__)
print(os.listdir('.'))

class Bola:
    def __init__(self,x,y,w,h,color) -> None:
        self._x=x
        self._y=y
        self.w=w
        self.h=h
        self.color=color
        self.__velx=3
        self.__vely=7
        self.rect=(self._x,self._y,self.w,self.h)
    def draw(self,surface):
        pygame.draw.ellipse(surface,self.color,self.rect)
        return self
    
    def update(self,gm_width,gm_heght):
        
        self._x+=self.__velx
        self._y+=self.__vely
        
        if self._x>gm_width or  self._x<0:
            self.__velx*=-1
        if self._y>gm_heght or self._y<0:
            self.__vely *=-1
        self.rect=(self._x,self._y,self.w,self.h)
        
        return self
class Bolinhas:
    def __init__(self,radius,color) -> None:
        self.cor=color
        self.radius=radius
        self._coords=[]
     
    def cordenadas(self)->List:
        for i in range(160):
            x=randint(0,800)
            y=randint(0,500)
            self._coords.append([x,y])
        return self._coords

    # def draw(self,surface):
    #     for coords in self.cordenadas():
    #         x=coords[0]
    #         y=coords[1]
    #         pygame.draw.circle(surface,self.cor,(x,y),self.radius)
class Lines:
    def __init__(self,x,y) -> None:
        self.x=x
        self.y=y
        self.rect=(self.x,self.y,50,20)
    def draw(self,display):
        pygame.draw.rect(display,(255,255,255),self.rect)
        return self
    
    
    def update(self,display):
        self.x+=1
    
        print('[self.x [lines] ',self.x, ' [rect]', self.rect)
        if self.x>500:
            print(' [x ] esgotou ', self.x )
            self.x=0
        self.rect=(self.x,self.y,50,20)
        self.draw(display)
        
            
            
                
        
def draw_road_lines(c:int):
    # while True:
    for i in range(0,width+130,130):
        cord=i+c
        pygame.draw.rect(display,(255,255,255),(cord,370,50,20))
        
 

pygame.init()
width = 1300
heigh = 600
carro = "lessons_section/ecto.png"
img=Image.open(carro)
img.save('new.png')
print('[img size] ',img.size)
print('[V]' if os.path.exists(carro) else '[x]')
carImage = pygame.image.load(carro)
display = pygame.display.set_mode((width, heigh))
pygame.display.set_caption("A bit Racy")



# display.fill((255/2,23,212),(0,0,300,300))
def construir_estrada():
    display.fill((255 / 2, 23, 212, .31), (0, 0, width, 300))
    display.fill((255 / 2, 123, 212, .31), (0, 400, width, 530))
    display.fill((2,0,0), (0,300,width,150))
    # display.fill((255, 255, 255), (0, 330, width, 40))
    # draw_road_lines()
    
        
    

def draw_car(x:int, y:int):
    display.blit(carImage, (x, y))

def mostrar_message_de_crash(title:str,msg:str):
    myfont=pygame.font.Font('lessons_section/myfonts/font2.ttf',150)
    myfn3=pygame.font.Font('lessons_section/myfonts/net_font.ttf',45)
    
    posicao1=myfont.render(msg, 1,(255,0,0))
    posicao2=myfn3.render(title,1,(255,255,255))
    
    display.blit(posicao2,(200,188))
    display.blit(posicao1,(200,200))


def mostrar_output(pos_x :int, pos_y:int):
    myfont = pygame.font.SysFont("DejaVuSans", 24)
    lbl_x = myfont.render('pos x:' + str(pos_x), 1, (255, 255, 255))
    lbl_y = myfont.render('pos y:' + str(pos_y), 1, (25, 255, 255))
    display.blit(lbl_x, (30, 0))  # para desenhar os resultados
    display.blit(lbl_y, (640, 0))
    
def gama_loop():
    c=0
    x = 0
    y = 0
    clock = pygame.time.Clock()
    crashed = False
    car_x = 0
    car_y = 0
    b=Bola(12,89,60,60,(100,12,1))
    bolinhas=Bolinhas(3,(234,17,99))
    
    # as bolinhas que se mo vem [crio uma lista com 160 cordenadas de bolinhas ]
    coords_list=[]
    for i in range(160):
        x=randint(0,1400)
        y=randint(0,800)
        coords_list.append([x,y])
    #print(coords_list) # [[868, 155], [917, 340], [560, 229] ,.........]
    
    while not crashed:
        c+=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    car_x = -5
                if event.key == pygame.K_RIGHT:
                    car_x = +5
                if event.key == pygame.K_UP:
                    car_y -= 5
                if event.key == pygame.K_DOWN:
                    car_y += 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    car_x = 0
                    car_y = 0
        if c>110:
            c *=-1
        x += car_x
        y += car_y
        construir_estrada()
        draw_road_lines(c)
        draw_car(x, y)
        
#>>>>>  b.draw(display).update(width,heigh)  [PARA FAZER QUICAR ABOLA]
        # draw_road_lines() 
        # implementacao de bolinhas
        
        # aqui vou varer todas posioes geradas e desenhar cada lista de coordenada
        for coords in coords_list:
            bx=coords[0]
            by=coords[1]
            pygame.draw.circle(display,(76,66,5),(bx,by),4)
            
            coords[1]+=1
            if coords[1]>500:
                coords[1]=0
             
                                   
        # =======================
        if x>width or x<0:
            print('Game Over you crashed')
            mostrar_message_de_crash('PERDESTE O JOGO CARA',"You Crashed")
        mostrar_output(x, f' y={y} c={c}')
        # pygame.display.update()
        pygame.display.flip()

        clock.tick(60)
gama_loop()
print('Game Crashed')
pygame.quit()

quit(6)
print('was quit with  code =0 this wil not be exceuted')

