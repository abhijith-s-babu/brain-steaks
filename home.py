import pygame
import sys
import untitled2

pygame.init()
mydis = pygame.display.set_mode((1000,700),pygame.RESIZABLE)
headcolor = (255,0,50)
txtcolor = (255,13,0)
btncolor = (240,240,240)
black = (0, 0, 0)


class clickable:
    def __init__(self,startx,starty,w,h,uid):
        self.startx = startx
        self.starty = starty
        self.w = w
        self.h = h
        self.uid = uid
    
    def isover(self,pos):
        if pos[0]>self.startx and pos[0]< self.startx + self.w:
            if pos[1]>self.starty and pos[1]< self.starty + self.h:
                return True
            else:
                return False
        else:
            return False
            
def intro():
    bg1 = pygame.image.load("C:\\Users\\ABHIJITHSBABU\\brain steaks\introbg.jpg")
    #bg = pygame.image.load("C:\\Users\\ABHIJITHSBABU\\brain steaks\mainbg3.jpg")
    bg1 = pygame.transform.scale(bg1, (1000, 700))
    mydis.blit(bg1,(0,0))
    
    
    while True:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
                
        pygame.display.update()    
def mainpage():
    bg = pygame.image.load("C:\\Users\\ABHIJITHSBABU\\brain steaks\mainbg2.png")
    #bg = pygame.image.load("C:\\Users\\ABHIJITHSBABU\\brain steaks\mainbg3.jpg")
    bg = pygame.transform.scale(bg, (1000, 700))
    mydis.blit(bg,(0,0))
    '''
    pygame.draw.rect(mydis,btncolor,(430,240,140,120));
    pygame.draw.rect(mydis,btncolor,(430,520,140,120));
    pygame.draw.rect(mydis,btncolor,(590,240,140,120));
    pygame.draw.rect(mydis,btncolor,(590,380,140,120));
    pygame.draw.rect(mydis,btncolor,(270,380,140,120));
    pygame.draw.rect(mydis,btncolor,(270,520,140,120));
    pygame.draw.rect(mydis,btncolor,(340,100,320,70));
    pygame.draw.rect(mydis,btncolor,(750,600,200,70));
    '''
    sudoku_b = clickable(430,240,140,120,0)
    xox_b = clickable(430, 520, 140, 120,0)
    shuffle_b = clickable(590, 240, 140, 120,0)
    chess_b = clickable(590, 380, 140, 120,0)
    pair_b = clickable(270, 380, 140, 120,0)
    snake_b = clickable(270, 520, 140, 120,0)
    about = clickable(750, 600, 200, 70,0)
    
    font1 = pygame.font.Font("freesansbold.ttf",50)
    paper = font1.render("Brain Steaks",True,headcolor)
    textrect = paper.get_rect()
    textrect.center = (500,140)
    mydis.blit(paper,textrect)
    
    font2 = pygame.font.Font("freesansbold.ttf",30)
    gtext1 = font2.render("sudoku",True,txtcolor)
    textrect = gtext1.get_rect()
    textrect.center = (500,300)
    mydis.blit(gtext1,textrect)
    
    gtext1 = font2.render("shuffle",True,txtcolor)
    textrect = gtext1.get_rect()
    textrect.center = (660,300)
    mydis.blit(gtext1,textrect)
    
    gtext1 = font2.render("pair",True,txtcolor)
    textrect = gtext1.get_rect()
    textrect.center = (340,440)
    mydis.blit(gtext1,textrect)
    
    gtext1 = font2.render("chess",True,txtcolor)
    textrect = gtext1.get_rect()
    textrect.center = (660,440)
    mydis.blit(gtext1,textrect)
    
    gtext1 = font2.render("S&L",True,txtcolor)
    textrect = gtext1.get_rect()
    textrect.center = (340,580)
    mydis.blit(gtext1,textrect)
    
    gtext1 = font2.render("XOX",True,txtcolor)
    textrect = gtext1.get_rect()
    textrect.center = (500,580)
    mydis.blit(gtext1,textrect)
    
    gtext1 = font2.render("about",True,txtcolor)
    textrect = gtext1.get_rect()
    textrect.center = (850,635)
    mydis.blit(gtext1,textrect)

    
    while True:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if sudoku_b.isover(pos):
                    print("game 1")
                if xox_b.isover(pos):
                    print("game 2")
                if shuffle_b.isover(pos):
                    print("game 3")
                if chess_b.isover(pos):
                    print("game 4")
                if pair_b.isover(pos):
                    print("game 5")
                if snake_b.isover(pos):
                    print("game 6")
                if about.isover(pos):
                    print("about")
                
                
        pygame.display.update()
 
#intro()
mainpage()
#shuffle()
