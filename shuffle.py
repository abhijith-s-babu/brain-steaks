import pygame
import sys

pygame.init()
mydis = pygame.display.set_mode((1000,700),pygame.RESIZABLE)
headcolor = (255,0,50)
txtcolor = (255,13,0)
btncolor = (240,240,240)
black = (0, 0, 0)
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
          
def shuffle():
    bg = pygame.image.load("blackbg.jpg")
    bg = pygame.transform.scale(bg, (1000, 700))
    mydis.blit(bg, (0, 0))

    img1 = pygame.image.load("image_part_005.png")
    img1 = pygame.transform.scale(img1, (120, 120))
    mydis.blit(img1, (260, 170))
    img2 = pygame.image.load("image_part_004.png")
    img2 = pygame.transform.scale(img2, (120, 120))
    mydis.blit(img2, (380, 170))
    img3 = pygame.image.load("image_part_003.png")
    img3 = pygame.transform.scale(img3, (120, 120))
    mydis.blit(img3, (500, 170))
    img4 = pygame.image.load("image_part_002.png")
    img4 = pygame.transform.scale(img4, (120, 120))
    mydis.blit(img4, (620, 170))
    img5 = pygame.image.load("image_part_001.png")
    img5 = pygame.transform.scale(img5, (120, 120))
    mydis.blit(img5, (260, 290))
    img6 = pygame.image.load("image_part_006.png")
    img6 = pygame.transform.scale(img6, (120, 120))
    mydis.blit(img6, (380, 290))
    img7 = pygame.image.load("image_part_012.png")
    img7 = pygame.transform.scale(img7, (120, 120))
    mydis.blit(img7, (500, 290))
    img8 = pygame.image.load("image_part_008.png")
    img8 = pygame.transform.scale(img8, (120, 120))
    mydis.blit(img8, (620, 290))
    img9 = pygame.image.load("C:image_part_009.png")
    img9 = pygame.transform.scale(img9, (120, 120))
    mydis.blit(img9, (260, 410))
    img10 = pygame.image.load("image_part_010.png")
    img10 = pygame.transform.scale(img10, (120, 120))
    mydis.blit(img10, (380, 410))
    img11 = pygame.image.load("image_part_015.png")
    img11 = pygame.transform.scale(img11, (120, 120))
    mydis.blit(img11, (500, 410))
    img12 = pygame.image.load("image_part_007.png")
    img12 = pygame.transform.scale(img12, (120, 120))
    mydis.blit(img12, (620, 410))
    img13 = pygame.image.load("image_part_013.png")
    img13 = pygame.transform.scale(img13, (120, 120))
    mydis.blit(img13, (260, 530))
    img14 = pygame.image.load("image_part_014.png")
    img14 = pygame.transform.scale(img14, (120, 120))
    mydis.blit(img14, (380, 530))
    img15 = pygame.image.load("image_part_011.png")
    img15 = pygame.transform.scale(img15, (120, 120))
    mydis.blit(img15, (500, 530))
    img16 = pygame.image.load("image_part_016.png")
    img16 = pygame.transform.scale(img16, (120, 120))
    # mydis.blit(img16,(620,530))
    pygame.draw.rect(mydis, black, (620, 530, 120, 120))
    org = pygame.image.load("shuffle.jpg")
    org = pygame.transform.scale(org, (200, 200))
    mydis.blit(org, (770, 100))

    imglist = [0] * 16
    imglist[0] = img1
    imglist[1] = img2
    imglist[2] = img3
    imglist[3] = img4
    imglist[4] = img5
    imglist[5] = img6
    imglist[6] = img7
    imglist[7] = img8
    imglist[8] = img9
    imglist[9] = img10
    imglist[10] = img11
    imglist[11] = img12
    imglist[12] = img13
    imglist[13] = img14
    imglist[14] = img15

    clicklist = []
    imgpos1 = clickable(260, 170, 120, 120, 1)
    imgpos2 = clickable(380, 170, 120, 120, 2)
    imgpos3 = clickable(500, 170, 120, 120, 3)
    imgpos4 = clickable(620, 170, 120, 120, 4)
    imgpos5 = clickable(260, 290, 120, 120, 5)
    imgpos6 = clickable(380, 290, 120, 120, 6)
    imgpos7 = clickable(500, 290, 120, 120, 7)
    imgpos8 = clickable(620, 290, 120, 120, 8)
    imgpos9 = clickable(260, 410, 120, 120, 9)
    imgpos10 = clickable(380, 410, 120, 120, 10)
    imgpos11 = clickable(500, 410, 120, 120, 11)
    imgpos12 = clickable(620, 410, 120, 120, 12)
    imgpos13 = clickable(260, 530, 120, 120, 13)
    imgpos14 = clickable(380, 530, 120, 120, 14)
    imgpos15 = clickable(500, 530, 120, 120, 15)
    imgpos16 = clickable(620, 530, 120, 120, 16)

    moves = 0

    for i in range(16):
        name = "imgpos" + str(i + 1)
        ob = eval(name)
        clicklist.append(ob)

    while True:
        for event in pygame.event.get():
            mpos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in clicklist:
                    if i.isover(mpos):
                        pos = i.uid
                        if imglist[pos - 1] != 0:
                            top = pos - 4
                            bottom = pos + 4
                            if pos % 4 != 0:
                                right = pos + 1
                            else:
                                right = 18
                            if pos % 4 != 1:
                                left = pos - 1
                            else:
                                left = -1

                            if top > 0:
                                if imglist[top - 1] == 0:
                                    mydis.blit(imglist[pos - 1],
                                               (260 + (120 * ((top - 1) % 4)), 170 + (120 * ((top - 1) // 4))))
                                    imglist[top - 1] = imglist[pos - 1]
                                    imglist[pos - 1] = 0
                                    pygame.draw.rect(mydis, black, (
                                        260 + (120 * ((pos - 1) % 4)), 170 + (120 * ((pos - 1) // 4)), 120, 120))

                            if bottom < 17:
                                if imglist[bottom - 1] == 0:
                                    mydis.blit(imglist[pos - 1],
                                               (260 + (120 * ((bottom - 1) % 4)), 170 + (120 * ((bottom - 1) // 4))))
                                    imglist[bottom - 1] = imglist[pos - 1]
                                    imglist[pos - 1] = 0
                                    pygame.draw.rect(mydis, black, (
                                        260 + (120 * ((pos - 1) % 4)), 170 + (120 * ((pos - 1) // 4)), 120, 120))
                            if left > 0:
                                if imglist[left - 1] == 0:
                                    mydis.blit(imglist[pos - 1],
                                               (260 + (120 * ((left - 1) % 4)), 170 + (120 * ((left - 1) // 4))))
                                    imglist[left - 1] = imglist[pos - 1]
                                    imglist[pos - 1] = 0
                                    pygame.draw.rect(mydis, black, (
                                        260 + (120 * ((pos - 1) % 4)), 170 + (120 * ((pos - 1) // 4)), 120, 120))
                            if right < 17:
                                if imglist[right - 1] == 0:
                                    mydis.blit(imglist[pos - 1],
                                               (260 + (120 * ((right - 1) % 4)), 170 + (120 * ((right - 1) // 4))))
                                    imglist[right - 1] = imglist[pos - 1]
                                    imglist[pos - 1] = 0
                                    pygame.draw.rect(mydis, black, (
                                        260 + (120 * ((pos - 1) % 4)), 170 + (120 * ((pos - 1) // 4)), 120, 120))

        pygame.display.update()



shuffle()
