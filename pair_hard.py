import pygame
import sys
import random


pygame.init()
mydis = pygame.display.set_mode((1000,700))
black = (0, 0, 0)
white = (255, 255, 255)
erase = (200, 0, 255)
fontObj1 = pygame.font.Font('freesansbold.ttf', 70)
fontObj2 = pygame.font.Font('freesansbold.ttf', 50)
fontObj3 = pygame.font.Font('freesansbold.ttf', 40)
pygame.display.set_caption("Brain Steaks")

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
        
def pair_medium():
    img = pygame.image.load("C:\\Users\\ABHIJITHSBABU\\brain steaks\\blackbg.jpg")
    bgo = pygame.transform.scale(img, (1000, 700))
    mydis.blit(bgo,(0,0))
    img = pygame.image.load("C:\\Users\\ABHIJITHSBABU\\brain steaks\\pairbg.png")
    bg = pygame.transform.scale(img, (1000, 700))
    mydis.blit(bg,(0,0))
    
    cback = pygame.image.load("C:\\Users\\ABHIJITHSBABU\\brain steaks\\cardback.png")
    cback = pygame.transform.scale(cback, (85, 100))
    
    img = pygame.image.load("C:\\Users\\ABHIJITHSBABU\\brain steaks\\paircut.png")
    cut = pygame.transform.scale(img, (1000, 700))
    
    img = pygame.image.load("C:\\Users\\ABHIJITHSBABU\\brain steaks\\dim.png")
    dim = pygame.transform.scale(img, (1000, 700))
    
    img = pygame.image.load("C:\\Users\\ABHIJITHSBABU\\brain steaks\\dialog.png")
    dial = pygame.transform.scale(img, (1000, 700))
    
    textSurfaceObj = fontObj2.render("LIVES", True, black )
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (835,130)
    mydis.blit(textSurfaceObj,textRectObj)
    
    textSurfaceObj = fontObj2.render("30", True, black )
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (835,245)
    mydis.blit(textSurfaceObj,textRectObj)
    
    textSurfaceObj = fontObj1.render("BACK", True, black )
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (835,470)
    mydis.blit(textSurfaceObj,textRectObj)
    
    textSurfaceObj = fontObj1.render("RESET", True, black )
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (835,610)
    mydis.blit(textSurfaceObj,textRectObj)
    
    back_b = clickable(705, 420, 260, 100, 50)
    reset_b = clickable(705, 560, 260, 100, 50)
    rest_b = clickable(280, 420, 190, 50, 20)
    bck_b = clickable(530, 420, 190, 50, 20)
    
    active = 0
    c_left = 30
    diag = 0
    
    cards = []
    selected = []
    
    for i in range(5):
        for j in range(6):
            x = 45 + j*103
            y = 105 + i*112
            mydis.blit(cback,(x,y))
            c = clickable(x,y,85,100,6*i + j)
            cards.append(c)
            
    randlist = []
    def randomise():
        nonlocal randlist
        k = random.randint(1, 23)
        l = random.randint(3, 5)
        l = l*2 + 1
        
        randlist = []
        for i in range(30):
            k = k+l
            if k > 30:
                k = k - 30
            while k in randlist:
                k += 5
                if k > 30:
                    k = k - 30
            randlist.append(k)
    randomise()
    
    curr_img = None
    curr_num = None
    
    img = pygame.image.load("C:\\Users\\ABHIJITHSBABU\\brain steaks\\pair1.png")
    img1 = pygame.transform.scale(img, (85, 100))
    
    img = pygame.image.load("C:\\Users\\ABHIJITHSBABU\\brain steaks\\pair2.png")
    img2 = pygame.transform.scale(img, (85, 100))
    
    img = pygame.image.load("C:\\Users\\ABHIJITHSBABU\\brain steaks\\pair3.jpg")
    img3 = pygame.transform.scale(img, (85, 100))
    
    img = pygame.image.load("C:\\Users\\ABHIJITHSBABU\\brain steaks\\pair4.jpg")
    img4 = pygame.transform.scale(img, (85, 100))
    
    img = pygame.image.load("C:\\Users\\ABHIJITHSBABU\\brain steaks\\pair5.png")
    img5 = pygame.transform.scale(img, (85, 100))
    
    img = pygame.image.load("C:\\Users\\ABHIJITHSBABU\\brain steaks\\pair6.jpg")
    img6 = pygame.transform.scale(img, (85, 100))
    
    img = pygame.image.load("C:\\Users\\ABHIJITHSBABU\\brain steaks\\pair7.png")
    img7 = pygame.transform.scale(img, (85, 100))
    
    img = pygame.image.load("C:\\Users\\ABHIJITHSBABU\\brain steaks\\pair8.png")
    img8 = pygame.transform.scale(img, (85, 100))
    
    img = pygame.image.load("C:\\Users\\ABHIJITHSBABU\\brain steaks\\pair9.png")
    img9 = pygame.transform.scale(img, (85, 100))
    
    img = pygame.image.load("C:\\Users\\ABHIJITHSBABU\\brain steaks\\pair10.png")
    img10 = pygame.transform.scale(img, (85, 100))
    
    img = pygame.image.load("C:\\Users\\ABHIJITHSBABU\\brain steaks\\pair11.jpg")
    img11 = pygame.transform.scale(img, (85, 100))
    
    img = pygame.image.load("C:\\Users\\ABHIJITHSBABU\\brain steaks\\pair12.jpg")
    img12 = pygame.transform.scale(img, (85, 100))
    
    img = pygame.image.load("C:\\Users\\ABHIJITHSBABU\\brain steaks\\pair13.png")
    img13 = pygame.transform.scale(img, (85, 100))
    
    img = pygame.image.load("C:\\Users\\ABHIJITHSBABU\\brain steaks\\pair14.png")
    img14 = pygame.transform.scale(img, (85, 100))
    
    img = pygame.image.load("C:\\Users\\ABHIJITHSBABU\\brain steaks\\pair15.png")
    img15 = pygame.transform.scale(img, (85, 100))
    
    def flip(n):
        nonlocal active
        nonlocal img1
        nonlocal img2
        nonlocal img3
        nonlocal img4
        nonlocal img5
        nonlocal img6
        nonlocal img7
        nonlocal img8
        nonlocal img9
        nonlocal img10
        nonlocal img11
        nonlocal img12
        nonlocal img13
        nonlocal img14
        nonlocal img15
        nonlocal curr_img
        nonlocal curr_num
        x = n%6
        y = n//6
        x = 45 + x*103
        y = 105 + y*112
        img_id = (randlist[n]+1)//2
        im = "img" + str(img_id)
        im = eval(im)
        mydis.blit(im,(x,y))
        if active == 1:
            pygame.display.update()
            pygame.time.wait(500)
            check(im,n)
        else:
            curr_img = im
            curr_num = n 
            selected.append(n)
            active = 1
            
    def reset():
        nonlocal c_left
        nonlocal selected
        nonlocal active
        mydis.blit(bgo,(0,0))
        mydis.blit(bg,(0,0))
        c_left = 30
        selected = []
        randomise()
        for i in range(5):
            for j in range(6):
                x = 45 + j*103
                y = 105 + i*112
                mydis.blit(cback,(x,y))
    
        textSurfaceObj = fontObj2.render("LIVES", True, black )
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (835,130)
        mydis.blit(textSurfaceObj,textRectObj)
        
        textSurfaceObj = fontObj2.render("30", True, black )
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (835,245)
        mydis.blit(textSurfaceObj,textRectObj)
        
        textSurfaceObj = fontObj1.render("BACK", True, black )
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (835,470)
        mydis.blit(textSurfaceObj,textRectObj)
        
        textSurfaceObj = fontObj1.render("RESET", True, black )
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (835,610)
        mydis.blit(textSurfaceObj,textRectObj)
        active = 0
        
    
    def show_win():
        nonlocal diag
        mydis.blit(dim,(0,0))
        mydis.blit(dial,(0,0))  
        textSurfaceObj = fontObj2.render("LEVEL COMPLETE", True, black )
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (500,300)
        mydis.blit(textSurfaceObj,textRectObj)
        textSurfaceObj = fontObj3.render("RESTART", True, black )
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (375,445)
        mydis.blit(textSurfaceObj,textRectObj)
        textSurfaceObj = fontObj3.render("BACK", True, black )
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (625,445)
        mydis.blit(textSurfaceObj,textRectObj)
        pygame.display.update()
        diag = 1
                
    
    def show_loss():
        nonlocal diag  
        mydis.blit(dim,(0,0))
        mydis.blit(dial,(0,0))
        textSurfaceObj = fontObj2.render("GAME OVER", True, black )
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (500,300)
        mydis.blit(textSurfaceObj,textRectObj)
        textSurfaceObj = fontObj3.render("RETRY", True, black )
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (375,445)
        mydis.blit(textSurfaceObj,textRectObj)
        textSurfaceObj = fontObj3.render("BACK", True, black )
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (625,445)
        mydis.blit(textSurfaceObj,textRectObj)
        pygame.display.update()
        diag = 1
    
    def check(ob,m):
        nonlocal curr_img
        nonlocal curr_num
        nonlocal cback
        nonlocal active
        nonlocal c_left
        if ob == curr_img:
            selected.append(m)
            if len(selected) == 30:
                show_win()
        else:
            x = m%6
            y = m//6
            x = 45 + x*103
            y = 105 + y*112
            mydis.blit(cback,(x,y))
            x = curr_num%6
            y = curr_num//6
            x = 45 + x*103
            y = 105 + y*112
            mydis.blit(cback,(x,y))
            selected.pop()
            
            c_left -= 1
            mydis.blit(cut,(0,0))
            
            textSurfaceObj = fontObj2.render(str(c_left), True, black )
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (835,245)
            mydis.blit(textSurfaceObj,textRectObj)
            
            if c_left == 0:
                show_loss()
                
            
            
            
        active = 0
            
            
    
    while True:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in cards:
                    if i.isover(pos) and i.uid not in selected:
                        flip(i.uid)
                        
                if back_b.isover(pos):
                    print("go back")
                if reset_b.isover(pos):
                    reset()
                if diag == 1:
                    if rest_b.isover(pos):
                        reset()
                        diag = 0
                    if bck_b.isover(pos):
                        print("go back")
                        diag = 0
                        
                
        pygame.display.update()
pair_medium()

        
