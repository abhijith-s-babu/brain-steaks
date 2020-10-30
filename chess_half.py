import pygame
import sys

pygame.init()
mydis = pygame.display.set_mode((1000,700))
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 242, 242)

active = 0
current = 0
death = 0
curr_img = 0
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
        
def bmove(ps,ac):
    pass

    
def wmove(ps,ac):
    pass

    
def chess2():
    #right shift by 15
    bg1 = pygame.image.load("C:\\Users\\ABHIJITHSBABU\\brain steaks\\blackbg.jpg")
    bg1 = pygame.transform.scale(bg1, (1000, 700))
    mydis.blit(bg1,(0,0))
    bg1 = pygame.image.load("C:\\Users\\ABHIJITHSBABU\\brain steaks\\chessbox.png")
    bg1 = pygame.transform.scale(bg1, (1000, 700))
    mydis.blit(bg1,(0,0))
    
    wpawn = pygame.image.load("C:\\Users\\ABHIJITHSBABU\\brain steaks\\white1.png")
    wpawn = pygame.transform.scale(wpawn, (30, 60))
    mydis.blit(wpawn,(275,510))
    mydis.blit(wpawn,(335,510))
    mydis.blit(wpawn,(395,510))
    mydis.blit(wpawn,(455,510))
    mydis.blit(wpawn,(515,510))
    mydis.blit(wpawn,(575,510))
    mydis.blit(wpawn,(635,510))
    mydis.blit(wpawn,(695,510))
    
    bpawn = pygame.image.load("C:\\Users\\ABHIJITHSBABU\\brain steaks\\black6.png")
    bpawn = pygame.transform.scale(bpawn, (30, 60))
    mydis.blit(bpawn,(275,210))
    mydis.blit(bpawn,(335,210))
    mydis.blit(bpawn,(395,210))
    mydis.blit(bpawn,(455,210))
    mydis.blit(bpawn,(515,210))
    mydis.blit(bpawn,(575,210))
    mydis.blit(bpawn,(635,210))
    mydis.blit(bpawn,(695,210))
    
    brook = pygame.image.load("C:\\Users\\ABHIJITHSBABU\\brain steaks\\black4.png")
    brook = pygame.transform.scale(brook, (30, 60))
    mydis.blit(brook,(275,150))
    mydis.blit(brook,(695,150))
    
    bknight = pygame.image.load("C:\\Users\\ABHIJITHSBABU\\brain steaks\\black5.png")
    bknight = pygame.transform.scale(bknight, (30, 60))
    mydis.blit(bknight,(335,150))
    mydis.blit(bknight,(635,150))
    
    bdiag = pygame.image.load("C:\\Users\\ABHIJITHSBABU\\brain steaks\\black3.png")
    bdiag = pygame.transform.scale(bdiag, (30, 60))
    mydis.blit(bdiag,(395,150))
    mydis.blit(bdiag,(575,150))
    
    
    bqueen = pygame.image.load("C:\\Users\\ABHIJITHSBABU\\brain steaks\\black2.png")
    bqueen = pygame.transform.scale(bqueen, (30, 60))
    mydis.blit(bqueen,(455,150))
    
    bking = pygame.image.load("C:\\Users\\ABHIJITHSBABU\\brain steaks\\black1.png")
    bking = pygame.transform.scale(bking, (30, 60))
    mydis.blit(bking,(515,150))
    
    wrook = pygame.image.load("C:\\Users\\ABHIJITHSBABU\\brain steaks\\white3.png")
    wrook = pygame.transform.scale(wrook, (30, 60))
    mydis.blit(wrook,(275,570))
    mydis.blit(wrook,(695,570))
    
    wknight = pygame.image.load("C:\\Users\\ABHIJITHSBABU\\brain steaks\\white2.png")
    wknight = pygame.transform.scale(wknight, (30, 60))
    mydis.blit(wknight,(335,570))
    mydis.blit(wknight,(635,570))
    
    wdiag = pygame.image.load("C:\\Users\\ABHIJITHSBABU\\brain steaks\\white4.png")
    wdiag = pygame.transform.scale(wdiag, (30, 60))
    mydis.blit(wdiag,(395,570))
    mydis.blit(wdiag,(575,570))
    
    
    wqueen = pygame.image.load("C:\\Users\\ABHIJITHSBABU\\brain steaks\\white5.png")
    wqueen = pygame.transform.scale(wqueen, (30, 60))
    mydis.blit(wqueen,(455,570))
    
    wking = pygame.image.load("C:\\Users\\ABHIJITHSBABU\\brain steaks\\white6.png")
    wking = pygame.transform.scale(wking, (30, 60))
    mydis.blit(wking,(515,570))
    
    glow = pygame.image.load("C:\\Users\\ABHIJITHSBABU\\brain steaks\\glow.png")
    glow = pygame.transform.scale(glow, (60, 60))
    rglow = pygame.image.load("C:\\Users\\ABHIJITHSBABU\\brain steaks\\redglow.png")
    rglow = pygame.transform.scale(rglow, (60, 60))
    
    #cell values
    '''
    black pawns = 0-7
    white pawns = 8-15
    black rooks = 16,17
    black knights = 18,19
    black diagonals = 20,21
    b  king = 22
    b queen = 23
    white rooks = 24,25
    white knights = 26,27
    white diagonals = 28,29
    w  king = 30
    w queen = 31
    
    '''
    
    cell = [0]*32
    for i in range(8):
        cell[i] = i+8
        cell[i+8] = i + 48
    cell[16] = 0
    cell[17] = 7
    cell[18] = 1
    cell[19] = 6
    cell[20] = 2
    cell[21] = 5
    cell[22] = 4
    cell[23] = 3
    cell[24] = 56
    cell[25] = 63
    cell[26] = 57
    cell[27] = 62
    cell[28] = 58
    cell[29] = 61
    cell[30] = 60
    cell[31] = 59
    
    movepawn = []
    
    clicks = []*64
    cid = 0
    for i in range(8):
        for j in range(8):
            clk = clickable(260+(j*60),150+(i*60),60,60,cid)
            cid += 1
            clicks.append(clk)
    chance = 'b'
    
    def col(p):
        colid = (((p//8)%2) + p)%2
        return colid  
    
    def getimage(gid):
        
        nonlocal bpawn
        nonlocal wpawn
        nonlocal brook
        nonlocal bdiag
        nonlocal bknight
        nonlocal bking
        nonlocal bqueen
        nonlocal wrook
        nonlocal wknight
        nonlocal wdiag
        nonlocal wking
        nonlocal wqueen
        
        if gid in range(0,8):
            return bpawn
        elif gid in range(8,16):
            return wpawn
        elif gid in [16,17]:
            return brook
        elif gid in [18,19]:
            return bknight
        elif gid in [20,21]:
            return bdiag
        elif gid == 22:
            return bking
        elif gid == 23:
            return bqueen
        elif gid in [24,25]:
            return wrook
        elif gid in [26,27]:
            return wknight
        elif gid in [28,29]:
            return wdiag
        elif gid == 30:
            return wking
        elif gid == 31:
            return wqueen
        
    
    glowcell = []
    redcell = []
    
    global active
    def bmove(ps):
        for i in range(0,8):
            cl = cell[i]
            if clicks[cl].isover(ps):
                move(i)
        for i in range(16,24):
            cl = cell[i]
            if clicks[cl].isover(ps):
                move(i)
    
                  
    
    
    def wmove(ps):
        for i in range(8,16):
            cl = cell[i]
            if clicks[cl].isover(ps):
                move(i)
        
        for i in range(24,32):
            cl = cell[i]
            if clicks[cl].isover(ps):
                move(i)
        
    
    
    def move(num):
        global active
        global current
        global curr_img
        pos = cell[num]
        
        #moving pawn
        if num < 8:
            if pos+8 not in cell and pos + 8 <64:
                mydis.blit(glow,(((pos%8)*60 + 260),(((pos+8)//8)*60 + 150)))
                glowcell.append(pos+8)
                
                if pos+16 not in cell and num not in movepawn:
                    mydis.blit(glow,(((pos%8)*60 + 260),(((pos+16)//8)*60 + 150)))
                    glowcell.append(pos+16)
                curr_img = bpawn
                active = 1
            for i in range(8,16):
                if pos + 9 == cell[i] and pos%8 != 7:
                   mydis.blit(rglow,((((pos+9)%8)*60 + 260),(((pos+9)//8)*60 + 150))) 
                   redcell.append(pos+9)
                   curr_img = bpawn
                   active = 1
                   death = i
                if pos + 7 == cell[i] and pos%8 != 0:
                   mydis.blit(rglow,((((pos+7)%8)*60 + 260),(((pos+7)//8)*60 + 150))) 
                   redcell.append(pos+7)
                   curr_img = bpawn
                   active = 1
                   death = i
            for i in range(24,32):
                if pos + 9 == cell[i] and pos%8 != 7:
                   mydis.blit(rglow,((((pos+9)%8)*60 + 260),(((pos+9)//8)*60 + 150))) 
                   redcell.append(pos+9)
                   curr_img = bpawn
                   active = 1
                   death = i
                if pos + 7 == cell[i] and pos%8 != 0:
                   mydis.blit(rglow,((((pos+7)%8)*60 + 260),(((pos+7)//8)*60 + 150))) 
                   redcell.append(pos+7)
                   curr_img = bpawn
                   active = 1
                   death = i
            current = num
        elif num < 16:
            pos = cell[num]
            if pos-8 not in cell and pos-8 >= 0:
                mydis.blit(glow,(((pos%8)*60 + 260),(((pos-8)//8)*60 + 150)))
                glowcell.append(pos-8)
                
                if pos-16 not in cell and num not in movepawn:
                    mydis.blit(glow,(((pos%8)*60 + 260),(((pos-16)//8)*60 + 150)))
                    glowcell.append(pos-16)
                curr_img = wpawn
                active = 1
            for i in range(0,8):
                if pos - 9 == cell[i] and pos%8 != 0:
                   mydis.blit(rglow,((((pos-9)%8)*60 + 260),(((pos-9)//8)*60 + 150))) 
                   redcell.append(pos-9)
                   curr_img = wpawn
                   active = 1
                   death = i
                if pos - 7 == cell[i] and pos%8 != 7:
                   mydis.blit(rglow,((((pos-7)%8)*60 + 260),(((pos-7)//8)*60 + 150))) 
                   redcell.append(pos-7)
                   curr_img = wpawn
                   active = 1
                   death = i
            for i in range(16,24):
                if pos - 9 == cell[i] and pos%8 != 0:
                   mydis.blit(rglow,((((pos-9)%8)*60 + 260),(((pos-9)//8)*60 + 150))) 
                   redcell.append(pos-9)
                   curr_img = wpawn
                   active = 1
                   death = i
                if pos - 7 == cell[i] and pos%8 != 7:
                   mydis.blit(rglow,((((pos-7)%8)*60 + 260),(((pos-7)//8)*60 + 150))) 
                   redcell.append(pos-7)
                   curr_img = wpawn
                   active = 1
                   death = i
            current = num
        #moving rooks
        elif num in [16,17,24,25]:
            for i in range(1,8):
                if (pos + 8*i) >=0 and (pos + 8*i) < 64:
                    if pos + 8*i >63:
                        break
                    if pos + 8*i not in cell:
                        mydis.blit(glow,(((pos%8)*60 + 260),(((pos+8*i)//8)*60 + 150)))
                        glowcell.append(pos+8*i)
                        active = 1
                    else:
                        if num in [16,17]:
                            if cell.index(pos + 8*i) in range(24,32):
                                mydis.blit(rglow,((((pos + 8*i)%8)*60 + 260),(((pos + 8*i)//8)*60 + 150))) 
                                redcell.append(pos + 8*i)
                                curr_img = brook
                                active = 1
                                death = cell.index(pos + 8*i)
                            if cell.index(pos + 8*i) in range(8,16):
                                mydis.blit(rglow,((((pos + 8*i)%8)*60 + 260),(((pos + 8*i)//8)*60 + 150))) 
                                redcell.append(pos + 8*i)
                                curr_img = brook
                                active = 1
                                death = cell.index(pos + 8*i)
                        if num in [24,25]:
                            if cell.index(pos + 8*i) in range(0,8):
                                mydis.blit(rglow,((((pos + 8*i)%8)*60 + 260),(((pos + 8*i)//8)*60 + 150))) 
                                redcell.append(pos + 8*i)
                                curr_img = wrook
                                active = 1
                                death = cell.index(pos + 8*i)
                            if cell.index(pos + 8*i) in range(16,24):
                                mydis.blit(rglow,((((pos + 8*i)%8)*60 + 260),(((pos + 8*i)//8)*60 + 150))) 
                                redcell.append(pos + 8*i)
                                curr_img = wrook
                                active = 1
                                death = cell.index(pos + 8*i)
                        break
            for i in range(1,8):
                if (pos - 8*i) >= 0 and (pos - 8*i) < 64:
                    if pos + 8*i < 0:
                        break
                    if pos - 8*i not in cell:
                        mydis.blit(glow,(((pos%8)*60 + 260),(((pos-8*i)//8)*60 + 150)))
                        glowcell.append(pos-8*i)
                        active = 1
                    else:
                        if num in [16,17]:
                            if cell.index(pos - 8*i) in range(24,32):
                                mydis.blit(rglow,((((pos - 8*i)%8)*60 + 260),(((pos - 8*i)//8)*60 + 150))) 
                                redcell.append(pos - 8*i)
                                curr_img = brook
                                active = 1
                                death = cell.index(pos - 8*i)
                            if cell.index(pos - 8*i) in range(8,16):
                                mydis.blit(rglow,((((pos - 8*i)%8)*60 + 260),(((pos - 8*i)//8)*60 + 150))) 
                                redcell.append(pos - 8*i)
                                curr_img = brook
                                active = 1
                                death = cell.index(pos - 8*i)
                        if num in [24,25]:
                            if cell.index(pos - 8*i) in range(0,8):
                                mydis.blit(rglow,((((pos - 8*i)%8)*60 + 260),(((pos - 8*i)//8)*60 + 150))) 
                                redcell.append(pos - 8*i)
                                curr_img = wrook
                                active = 1
                                death = cell.index(pos - 8*i)
                            if cell.index(pos - 8*i) in range(16,24):
                                mydis.blit(rglow,((((pos - 8*i)%8)*60 + 260),(((pos - 8*i)//8)*60 + 150))) 
                                redcell.append(pos - 8*i)
                                curr_img = wrook
                                active = 1
                                death = cell.index(pos - 8*i)
                        break
            for i in range(1,8):
                if (pos - i) >= 0 and (pos - i) < 64:
                    if (pos + 1 - i)%8 == 0:
                        break
                    if pos - i not in cell:
                        mydis.blit(glow,((((pos-i)%8)*60 + 260),(((pos-i)//8)*60 + 150)))
                        glowcell.append(pos-i)
                        active = 1
                    else:
                        if num in [16,17]:
                            if cell.index(pos - i) in range(8,16):
                                mydis.blit(rglow,((((pos - i)%8)*60 + 260),(((pos - i)//8)*60 + 150))) 
                                redcell.append(pos - i)
                                curr_img = brook
                                active = 1
                                death = cell.index(pos - i)
                            if cell.index(pos - i) in range(24,32):
                                mydis.blit(rglow,((((pos - i)%8)*60 + 260),(((pos - i)//8)*60 + 150))) 
                                redcell.append(pos - i)
                                curr_img = brook
                                active = 1
                                death = cell.index(pos - i)
                        if num in [24,25]:
                            if cell.index(pos - i) in range(0,8):
                                mydis.blit(rglow,((((pos - i)%8)*60 + 260),(((pos - i)//8)*60 + 150))) 
                                redcell.append(pos - i)
                                curr_img = wrook
                                active = 1
                                death = cell.index(pos - i)
                            if cell.index(pos - i) in range(16,24):
                                mydis.blit(rglow,((((pos - i)%8)*60 + 260),(((pos - i)//8)*60 + 150))) 
                                redcell.append(pos - i)
                                curr_img = wrook
                                active = 1
                                death = cell.index(pos - i)
                        break
            for i in range(1,8):
                if (pos + i) >= 0 and (pos + i) < 64:
                    if (pos + 1 + i)%8 == 1:
                        break
                    if pos + i not in cell:
                        mydis.blit(glow,((((pos+i)%8)*60 + 260),(((pos+i)//8)*60 + 150)))
                        glowcell.append(pos+i)
                        active = 1
                    else:
                        if num in [16,17]:
                            if cell.index(pos + i) in range(8,16):
                                mydis.blit(rglow,((((pos + i)%8)*60 + 260),(((pos + i)//8)*60 + 150))) 
                                redcell.append(pos + i)
                                curr_img = brook
                                active = 1
                                death = cell.index(pos + i)
                            if cell.index(pos + i) in range(24,32):
                                mydis.blit(rglow,((((pos + i)%8)*60 + 260),(((pos + i)//8)*60 + 150))) 
                                redcell.append(pos + i)
                                curr_img = brook
                                active = 1
                                death = cell.index(pos + i)
                        if num in [24,25]:
                            if cell.index(pos + i) in range(0,8):
                                mydis.blit(rglow,((((pos + i)%8)*60 + 260),(((pos + i)//8)*60 + 150))) 
                                redcell.append(pos + i)
                                curr_img = wrook
                                active = 1
                                death = cell.index(pos + i)
                            if cell.index(pos + i) in range(16,24):
                                mydis.blit(rglow,((((pos + i)%8)*60 + 260),(((pos + i)//8)*60 + 150))) 
                                redcell.append(pos + i)
                                curr_img = wrook
                                active = 1
                                death = cell.index(pos + i)
                        break
            if num<20:
                curr_img = brook
            else:
                curr_img = wrook
                
          
        #moving diagonals
        elif num in [20,21,28,29]:
            for i in range(1,8):
                if (pos + 9*i) >=0 and (pos + 9*i) < 64:
                    if pos + 9*i not in cell:
                        if (pos + 1 + 9*i)%8 == 1:
                            break
                        mydis.blit(glow,((((pos+9*i)%8)*60 + 260),(((pos+9*i)//8)*60 + 150)))
                        glowcell.append(pos+9*i)
                        active = 1
                    else:
                        if num in [20,21]:
                            if cell.index(pos + 9*i) in range(8,16):
                                mydis.blit(rglow,((((pos + 9*i)%8)*60 + 260),(((pos + 9*i)//8)*60 + 150))) 
                                redcell.append(pos + 9*i)
                                curr_img = bdiag
                                active = 1
                                death = cell.index(pos + 9*i)
                            if cell.index(pos + 9*i) in range(24,32):
                                mydis.blit(rglow,((((pos + 9*i)%8)*60 + 260),(((pos + 9*i)//8)*60 + 150))) 
                                redcell.append(pos + 9*i)
                                curr_img = bdiag
                                active = 1
                                death = cell.index(pos + 9*i)
                        if num in [28,29]:
                            if cell.index(pos + 9*i) in range(0,8):
                                mydis.blit(rglow,((((pos + 9*i)%8)*60 + 260),(((pos + 9*i)//8)*60 + 150))) 
                                redcell.append(pos + 9*i)
                                curr_img = wdiag
                                active = 1
                                death = cell.index(pos + 9*i)
                            if cell.index(pos + 9*i) in range(16,24):
                                mydis.blit(rglow,((((pos + 9*i)%8)*60 + 260),(((pos + 9*i)//8)*60 + 150))) 
                                redcell.append(pos + 9*i)
                                curr_img = wdiag
                                active = 1
                                death = cell.index(pos + 9*i)
                        break
            for i in range(1,8):
                if (pos - 9*i) >= 0 and (pos - 9*i) < 64:
                    if pos - 9*i not in cell:
                        if (pos - 9*i + 1)%8 == 0:
                            break
                        mydis.blit(glow,((((pos-9*i)%8)*60 + 260),(((pos-9*i)//8)*60 + 150)))
                        glowcell.append(pos-9*i)
                        active = 1
                    else:
                        if num in [20,21]:
                            if cell.index(pos - 9*i) in range(24,32):
                                mydis.blit(rglow,((((pos - 9*i)%8)*60 + 260),(((pos - 9*i)//8)*60 + 150))) 
                                redcell.append(pos - 9*i)
                                curr_img = bdiag
                                active = 1
                                death = cell.index(pos - 9*i)
                            if cell.index(pos - 8*i) in range(8,16):
                                mydis.blit(rglow,((((pos - 9*i)%8)*60 + 260),(((pos - 9*i)//8)*60 + 150))) 
                                redcell.append(pos - 9*i)
                                curr_img = bdiag
                                active = 1
                                death = cell.index(pos - 9*i)
                        if num in [28,29]:
                            if cell.index(pos - 9*i) in range(0,8):
                                mydis.blit(rglow,((((pos - 9*i)%8)*60 + 260),(((pos - 9*i)//8)*60 + 150))) 
                                redcell.append(pos - 9*i)
                                curr_img = wdiag
                                active = 1
                                death = cell.index(pos - 9*i)
                            if cell.index(pos - 9*i) in range(16,24):
                                mydis.blit(rglow,((((pos - 9*i)%8)*60 + 260),(((pos - 9*i)//8)*60 + 150))) 
                                redcell.append(pos - 9*i)
                                curr_img = wdiag
                                active = 1
                                death = cell.index(pos - 9*i)
                        break
            for i in range(1,8):
                if (pos + 7*i) >=0 and (pos + 7*i) < 64:
                    if pos + 7*i not in cell:
                        if (pos + 1 + 7*i)%8 == 0:
                            break
                        mydis.blit(glow,((((pos+7*i)%8)*60 + 260),(((pos+7*i)//8)*60 + 150)))
                        glowcell.append(pos+7*i)
                        active = 1
                    else:
                        if num in [20,21]:
                            if cell.index(pos + 7*i) in range(8,16):
                                mydis.blit(rglow,((((pos + 7*i)%8)*60 + 260),(((pos + 7*i)//8)*60 + 150))) 
                                redcell.append(pos + 7*i)
                                curr_img = bdiag
                                active = 1
                                death = cell.index(pos + 7*i)
                            if cell.index(pos + 7*i) in range(24,32):
                                mydis.blit(rglow,((((pos + 7*i)%8)*60 + 260),(((pos + 7*i)//8)*60 + 150))) 
                                redcell.append(pos + 7*i)
                                curr_img = bdiag
                                active = 1
                                death = cell.index(pos + 7*i)
                        if num in [28,29]:
                            if cell.index(pos + 7*i) in range(0,8):
                                mydis.blit(rglow,((((pos + 7*i)%8)*60 + 260),(((pos + 7*i)//8)*60 + 150))) 
                                redcell.append(pos + 7*i)
                                curr_img = wdiag
                                active = 1
                                death = cell.index(pos + 7*i)
                            if cell.index(pos + 7*i) in range(16,24):
                                mydis.blit(rglow,((((pos + 7*i)%8)*60 + 260),(((pos + 7*i)//8)*60 + 150))) 
                                redcell.append(pos + 7*i)
                                curr_img = wdiag
                                active = 1
                                death = cell.index(pos + 7*i)
                        break
            for i in range(1,8):
                if (pos - 7*i) >= 0 and (pos - 7*i) < 64:
                    if pos - 7*i not in cell:
                        if (pos - 7*i + 1)%8 == 1:
                            break
                        mydis.blit(glow,((((pos-7*i)%8)*60 + 260),(((pos-7*i)//8)*60 + 150)))
                        glowcell.append(pos-7*i)
                        active = 1
                    else:
                        if num in [20,21]:
                            if cell.index(pos - 7*i) in range(24,32):
                                mydis.blit(rglow,((((pos - 7*i)%8)*60 + 260),(((pos - 7*i)//8)*60 + 150))) 
                                redcell.append(pos - 7*i)
                                curr_img = bdiag
                                active = 1
                                death = cell.index(pos - 7*i)
                            if cell.index(pos - 7*i) in range(8,16):
                                mydis.blit(rglow,((((pos - 7*i)%8)*60 + 260),(((pos - 7*i)//8)*60 + 150))) 
                                redcell.append(pos - 7*i)
                                curr_img = bdiag
                                active = 1
                                death = cell.index(pos - 7*i)
                        if num in [28,29]:
                            if cell.index(pos - 7*i) in range(0,8):
                                mydis.blit(rglow,((((pos - 7*i)%8)*60 + 260),(((pos - 7*i)//8)*60 + 150))) 
                                redcell.append(pos - 7*i)
                                curr_img = wdiag
                                active = 1
                                death = cell.index(pos - 7*i)
                            if cell.index(pos - 7*i) in range(16,24):
                                mydis.blit(rglow,((((pos - 7*i)%8)*60 + 260),(((pos - 7*i)//8)*60 + 150))) 
                                redcell.append(pos - 7*i)
                                curr_img = wdiag
                                active = 1
                                death = cell.index(pos - 7*i)
                        break
            if num<25:
                curr_img = bdiag
            else:
                curr_img = wdiag
                
        #moving queen
        elif num in [23,31]:
            for i in range(1,8):
                if (pos + 8*i) >=0 and (pos + 8*i) < 64:
                    if pos + 8*i >63:
                        break
                    if pos + 8*i not in cell:
                        mydis.blit(glow,(((pos%8)*60 + 260),(((pos+8*i)//8)*60 + 150)))
                        glowcell.append(pos+8*i)
                        active = 1
                    else:
                        break
            for i in range(1,8):
                if (pos - 8*i) >= 0 and (pos - 8*i) < 64:
                    if pos + 8*i < 0:
                        break
                    if pos - 8*i not in cell:
                        mydis.blit(glow,(((pos%8)*60 + 260),(((pos-8*i)//8)*60 + 150)))
                        glowcell.append(pos-8*i)
                        active = 1
                    else:
                        break
            for i in range(1,8):
                if (pos - i) >= 0 and (pos - i) < 64:
                    if (pos + 1 - i)%8 == 0:
                        break
                    if pos - i not in cell:
                        mydis.blit(glow,((((pos-i)%8)*60 + 260),(((pos-i)//8)*60 + 150)))
                        glowcell.append(pos-i)
                        active = 1
                    else:
                        break
            for i in range(1,8):
                if (pos + i) >= 0 and (pos + i) < 64:
                    if (pos + 1 + i)%8 == 1:
                        break
                    if pos + i not in cell:
                        mydis.blit(glow,((((pos+i)%8)*60 + 260),(((pos+i)//8)*60 + 150)))
                        glowcell.append(pos+i)
                        active = 1
                    else:
                        break
            for i in range(1,8):
                if (pos + 9*i) >=0 and (pos + 9*i) < 64:
                    if pos + 9*i not in cell:
                        if (pos + 1 + 9*i)%8 == 1:
                            break
                        mydis.blit(glow,((((pos+9*i)%8)*60 + 260),(((pos+9*i)//8)*60 + 150)))
                        glowcell.append(pos+9*i)
                        active = 1
                    else:
                        break
            for i in range(1,8):
                if (pos - 9*i) >= 0 and (pos - 9*i) < 64:
                    if pos - 9*i not in cell:
                        if (pos - 9*i + 1)%8 == 0:
                            break
                        mydis.blit(glow,((((pos-9*i)%8)*60 + 260),(((pos-9*i)//8)*60 + 150)))
                        glowcell.append(pos-9*i)
                        active = 1
                    else:
                        break
            for i in range(1,8):
                if (pos + 7*i) >=0 and (pos + 7*i) < 64:
                    if pos + 7*i not in cell:
                        if (pos + 1 + 7*i)%8 == 0:
                            break
                        mydis.blit(glow,((((pos+7*i)%8)*60 + 260),(((pos+7*i)//8)*60 + 150)))
                        glowcell.append(pos+7*i)
                        active = 1
                    else:
                        break
            for i in range(1,8):
                if (pos - 7*i) >= 0 and (pos - 7*i) < 64:
                    if pos - 7*i not in cell:
                        if (pos - 7*i + 1)%8 == 1:
                            break
                        mydis.blit(glow,((((pos-7*i)%8)*60 + 260),(((pos-7*i)//8)*60 + 150)))
                        glowcell.append(pos-7*i)
                        active = 1
                    else:
                        break
            if num<25:
                curr_img = bqueen
            else:
                curr_img = wqueen
       
        #moving king
        elif num in [30,22]:
            if pos + 8 not in cell:
                if pos + 8 <64:
                    mydis.blit(glow,(((pos%8)*60 + 260),(((pos+8)//8)*60 + 150)))
                    glowcell.append(pos+8)
                    active = 1
            if pos - 8 not in cell:
                if pos - 8 >= 0:
                    mydis.blit(glow,(((pos%8)*60 + 260),(((pos-8)//8)*60 + 150)))
                    glowcell.append(pos-8)
                    active = 1
            if pos + 1 not in cell:
                if pos + 1 < 64:
                    mydis.blit(glow,((((pos+1)%8)*60 + 260),(((pos+1)//8)*60 + 150)))
                    glowcell.append(pos+1)
                    active = 1
            if pos + 9 not in cell:
                if pos + 9 < 64:
                    mydis.blit(glow,((((pos+9)%8)*60 + 260),(((pos+9)//8)*60 + 150)))
                    glowcell.append(pos+9)
                    active = 1
            if pos + 7 not in cell:
                if pos + 7 < 64:
                    mydis.blit(glow,((((pos+7)%8)*60 + 260),(((pos+7)//8)*60 + 150)))
                    glowcell.append(pos+7)
                    active = 1
            if pos - 1 not in cell:
                if pos - 1 >= 0:
                    mydis.blit(glow,((((pos-1)%8)*60 + 260),(((pos-1)//8)*60 + 150)))
                    glowcell.append(pos-1)
            if pos - 7 not in cell:
                if pos - 7 >= 0:
                    mydis.blit(glow,((((pos-7)%8)*60 + 260),(((pos-7)//8)*60 + 150)))
                    glowcell.append(pos-7)
            if pos - 9 not in cell:
                if pos - 9 >= 0:
                    mydis.blit(glow,((((pos-9)%8)*60 + 260),(((pos-9)//8)*60 + 150)))
                    glowcell.append(pos-9)
                    active = 1
            if num == 22:
                curr_img = bking
            else:
                curr_img = wking
                
        #moving knights
        elif num in [18,19,26,27]:
            if pos%8 == 7:
                for q in [-10,-17,6,15]:
                    np = pos + q
                    if np >=0 and np < 64:
                        if np not in cell:
                            mydis.blit(glow,((np%8)*60 + 260,(np//8)*60 + 150))
                            glowcell.append(np)
                            active = 1
            elif pos%8 == 6:
                for q in [-10,-17,6,15,-15,17]:
                    np = pos + q
                    if np >=0 and np < 64:
                        if np not in cell:
                            mydis.blit(glow,((np%8)*60 + 260,(np//8)*60 + 150))
                            glowcell.append(np)
                            active = 1
        
            elif pos%8 == 0:
                for q in [-15,-6,10,17]:
                    np = pos + q
                    if np >=0 and np < 64:
                        if np not in cell:
                            mydis.blit(glow,((np%8)*60 + 260,(np//8)*60 + 150))
                            glowcell.append(np)
                            active = 1
                
            elif pos%8 == 1:
                for q in [-15,-6,10,17,-17,15]:
                    np = pos + q
                    if np >=0 and np < 64:
                        if np not in cell:
                            mydis.blit(glow,((np%8)*60 + 260,(np//8)*60 + 150))
                            glowcell.append(np)
                            active = 1
            else:
                for q in [-15,-6,10,17,15,6,-10,-17]:
                    np = pos + q
                    if np >=0 and np < 64:
                        if np not in cell:
                            mydis.blit(glow,((np%8)*60 + 260,(np//8)*60 + 150))
                            glowcell.append(np)
                            active = 1
                            
            if num<25:
                curr_img = bknight
            else:
                curr_img = wknight
                
            
        current = num    
        
    
    while True:
        for event in pygame.event.get():
            cpos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if active == 0:
                    if chance == 'b':
                        bmove(cpos)
                    elif chance == 'w':
                        wmove(cpos)
                elif active == 1:
                    for i in glowcell:
                        if clicks[i].isover(cpos):
                            pos = cell[current]
                            cell[current] = i
                            a = col(pos)
                            if a == 0:
                                pygame.draw.rect(mydis,blue,(((pos%8)*60 + 260),((pos//8)*60 + 150),60,60))
                            elif a == 1:
                                pygame.draw.rect(mydis,white,(((pos%8)*60 + 260),((pos//8)*60 + 150),60,60))
                            for gi in glowcell:
                                pos = gi
                                a = col(pos)
                                if a == 0:
                                    pygame.draw.rect(mydis,blue,(((pos%8)*60 + 260),((pos//8)*60 + 150),60,60))
                                elif a == 1:
                                    pygame.draw.rect(mydis,white,(((pos%8)*60 + 260),((pos//8)*60 + 150),60,60))
                            for gi in redcell:
                                pos = gi
                                a = col(pos)
                                if a == 0:
                                    pygame.draw.rect(mydis,blue,(((pos%8)*60 + 260),((pos//8)*60 + 150),60,60))
                                elif a == 1:
                                    pygame.draw.rect(mydis,white,(((pos%8)*60 + 260),((pos//8)*60 + 150),60,60))
                                prt = getimage(cell.index(gi))
                                mydis.blit(prt,(((pos%8)*60 + 275),((pos//8)*60 + 150)))
                            mydis.blit(curr_img,(((i%8)*60 + 275),(((i)//8)*60 + 150)))
                            active = 0
                            movepawn.append(current)
                            glowcell = []
                            redcell = []
                            if chance == "b":
                                chance = "w"
                            else:
                                chance = "b"
                    for i in redcell:
                        if clicks[i].isover(cpos):
                            pos = cell[current]
                            print(cell.index(i))
                            cell[cell.index(i)] = -1
                            cell[current] = i
                            a = col(pos)
                            if a == 0:
                                pygame.draw.rect(mydis,blue,(((pos%8)*60 + 260),((pos//8)*60 + 150),60,60))
                            elif a == 1:
                                pygame.draw.rect(mydis,white,(((pos%8)*60 + 260),((pos//8)*60 + 150),60,60))
                            for gi in redcell:
                                pos = gi
                                a = col(pos)
                                if a == 0:
                                    pygame.draw.rect(mydis,blue,(((pos%8)*60 + 260),((pos//8)*60 + 150),60,60))
                                elif a == 1:
                                    pygame.draw.rect(mydis,white,(((pos%8)*60 + 260),((pos//8)*60 + 150),60,60))
                                prt = getimage(cell.index(gi))
                                mydis.blit(prt,(((pos%8)*60 + 275),((pos//8)*60 + 150)))
                            for gi in glowcell:
                                pos = gi
                                a = col(pos)
                                if a == 0:
                                    pygame.draw.rect(mydis,blue,(((pos%8)*60 + 260),((pos//8)*60 + 150),60,60))
                                elif a == 1:
                                    pygame.draw.rect(mydis,white,(((pos%8)*60 + 260),((pos//8)*60 + 150),60,60))
                            
                            mydis.blit(curr_img,(((i%8)*60 + 275),(((i)//8)*60 + 150)))
                            active = 0
                            movepawn.append(current)
                            redcell = []
                            glowcell = []
                            if chance == "b":
                                chance = "w"
                            else:
                                chance = "b"
        pygame.display.update()


                           
chess2()
                
