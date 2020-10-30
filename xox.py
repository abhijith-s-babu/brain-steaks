import pygame
import sys


pygame.init()
mydis = pygame.display.set_mode((1000,700))
black = (0, 0, 0)
white = (255, 255, 255)
erase = (200, 0, 255)
fontObj = pygame.font.Font('freesansbold.ttf', 90)
fontObj2 = pygame.font.Font('freesansbold.ttf', 50)
pygame.display.set_caption("Brain Steaks")
xscore = 0
oscore = 0
fc = "X"

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
        
def xox():
    
    def initpage():
        nonlocal chance
        img = pygame.image.load("C:\\Users\\ABHIJITHSBABU\\brain steaks\\blackbg.jpg")
        bg = pygame.transform.scale(img, (1000, 700))
        mydis.blit(bg,(0,0))
        img = pygame.image.load("C:\\Users\\ABHIJITHSBABU\\brain steaks\\xox.png")
        bg = pygame.transform.scale(img, (1000, 700))
        mydis.blit(bg,(0,0))
        img = pygame.image.load("C:\\Users\\ABHIJITHSBABU\\brain steaks\\xoxglow.png")
        glw = pygame.transform.scale(img, (300, 100))
        
        
        textSurfaceObj = fontObj2.render("Player X:", True, black )
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (755,150)
        mydis.blit(textSurfaceObj,textRectObj)
        
        textSurfaceObj = fontObj2.render("Player O:", True, black )
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (755,290)
        mydis.blit(textSurfaceObj,textRectObj)
        
        textSurfaceObj = fontObj2.render("RESET", True, black )
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (810,470)
        mydis.blit(textSurfaceObj,textRectObj)
        
        textSurfaceObj = fontObj2.render("BACK", True, black )
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (810,610)
        mydis.blit(textSurfaceObj,textRectObj)
        
    
        textSurfaceObj = fontObj2.render(str(xscore), True, black )
        textRectObjx = textSurfaceObj.get_rect()
        textRectObjx.center = (910,150)
        mydis.blit(textSurfaceObj,textRectObjx)
        
        textSurfaceObj = fontObj2.render(str(oscore), True, black )
        textRectObjx = textSurfaceObj.get_rect()
        textRectObjx.center = (910,290)
        mydis.blit(textSurfaceObj,textRectObjx)
        
        chance = fc
    reset_b = clickable(660,420,300,100,10)
    back_b = clickable(660,560,300,100,10)
    initpage()
    boxes = [[0 for i in range(3)] for i in range(3)]
    taken = []*9
    
    for i in range(3):
        for j in range(3):
            boxes[i][j] = clickable(20 + i*200, 80 + j*200, 200, 200, 3*i + j)
    print(boxes[0][2].startx)
    filled = [[0 for i in range(3)] for i in range(3)]
    
    def xwin(): 
        global xscore
        nonlocal filled
        nonlocal taken
        global fc
        img = pygame.image.load("C:\\Users\\ABHIJITHSBABU\\brain steaks\\xoxglow.png")
        glw = pygame.transform.scale(img, (340, 140))
        mydis.blit(glw,(640,80))
        pygame.display.update()
        pygame.time.wait(1000)
        xscore = xscore + 1
    
        textSurfaceObj = fontObj2.render(str(xscore), True, black )
        textRectObjx = textSurfaceObj.get_rect()
        textRectObjx.center = (910,150)
        mydis.blit(textSurfaceObj,textRectObjx)
        
        if xscore == 5:       
            textSurfaceObj = fontObj2.render("X won", True, white )
            textRectObjx = textSurfaceObj.get_rect()
            textRectObjx.center = (500,40)
            mydis.blit(textSurfaceObj,textRectObjx)
            pygame.display.update()
            pygame.time.wait(2000)
            
            reset_game()
            
        else:
    
            textSurfaceObj = fontObj2.render(str(xscore), True, black )
            textRectObjx = textSurfaceObj.get_rect()
            textRectObjx.center = (910,150)
            mydis.blit(textSurfaceObj,textRectObjx)
        
            initpage()
        
            taken = []
            filled = [[0 for i in range(3)] for i in range(3)]
            
            if fc == "X":
                fc = "O"
            else:
                fc = "X"
            
    def owin(): 
        global oscore
        nonlocal taken
        nonlocal filled
        global fc
        img = pygame.image.load("C:\\Users\\ABHIJITHSBABU\\brain steaks\\xoxglow.png")
        glw = pygame.transform.scale(img, (340, 140))
        mydis.blit(glw,(640,220))
        pygame.display.update()
        pygame.time.wait(1000)
        
        oscore = oscore + 1
        
        if oscore == 5:       
            textSurfaceObj = fontObj2.render("O won", True, white )
            textRectObjx = textSurfaceObj.get_rect()
            textRectObjx.center = (500,40)
            mydis.blit(textSurfaceObj,textRectObjx)
            pygame.display.update()
            pygame.time.wait(2000)
            reset_game()
            
        else:
    
            textSurfaceObj = fontObj2.render(str(oscore), True, black )
            textRectObjx = textSurfaceObj.get_rect()
            textRectObjx.center = (910,290)
            mydis.blit(textSurfaceObj,textRectObjx)
            
            initpage()
        
            taken = []
            filled = [[0 for i in range(3)] for i in range(3)]
            
            if fc == "X":
                fc = "O"
            else:
                fc = "X"
    
    def draw():
        nonlocal taken
        nonlocal filled
        global fc
        pygame.time.wait(1000)
        initpage()
        taken = []
        filled = [[0 for i in range(3)] for i in range(3)]
        
        if fc == "X":
            fc = "O"
        else:
            fc = "X"
        
    def reset_game():
        nonlocal taken
        nonlocal filled
        global oscore
        global xscore
        taken = []
        filled = [[0 for i in range(3)] for i in range(3)]
        oscore = 0
        xscore = 0
        initpage()
        
        
    def check():
        for i in range(3):
            for j in range(3):
                if filled[i][0] == filled[i][1] and filled[i][2] == filled[i][1]:
                    if filled[i][0] == "X":
                        xwin()
                    elif filled[i][0] == "O":
                        owin()
                elif filled[0][i] == filled[1][i] and filled[2][i] == filled[1][i]:
                    if filled[0][i] == "X":
                        xwin()
                    elif filled[1][i] == "O":
                        owin()
            if filled[0][0] == filled[1][1] and filled[1][1] == filled[2][2]:
                    if filled[0][0] == "X":
                        xwin()
                    elif filled[0][0] == "O":
                        owin()
            elif filled[0][2] == filled[1][1] and filled[1][1] == filled[2][0]:
                    if filled[0][2] == "X":
                        xwin()
                    elif filled[2][0] == "O":
                        owin()
            if len(taken) == 9:
                draw()
                    
    
    while True:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(3):
                    for j in range(3):
                        if boxes[i][j].isover(pos) and boxes[i][j] not in taken:
                            textSurfaceObj = fontObj.render(chance, True, black )
                            textRectObj = textSurfaceObj.get_rect()
                            textRectObj.center = (120 + 200*i , 180 + 200*j)
                            mydis.blit(textSurfaceObj,textRectObj)
                            filled[i][j] = chance
                            taken.append(boxes[i][j])
                            pygame.display.update()
                            check()
                            if chance == "X":
                                chance = "O"
                            else:
                                chance = "X"
                if reset_b.isover(pos):
                    reset_game()
                if back_b.isover(pos):
                    print("return to previous page")
        pygame.display.update()

xox()
