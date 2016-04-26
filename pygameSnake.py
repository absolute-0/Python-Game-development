import pygame
import time
import random
pygame.init()

#colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green =(0,255,0)
blue = (0,0,255)

#variables
window_width = 600
window_height = 500
canvas = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('lazy snake')

clock = pygame.time.Clock()
font = pygame.font.SysFont(None,25)

def snake(snakeList,blockSize):
    for block in snakeList:
        pygame.draw.rect(canvas, red, [block[0],block[1],blockSize,blockSize])
    
def textObject(msg,color):
    textScr = font.render(msg, True, color)
    return textScr, textScr.get_rect()

def message(msg, color):
    textScr,textRect = textObject(msg, color)
    textRect.center = (window_width/2),(window_height/2)
    canvas.blit(textScr,textRect)

def gameStart():
    posx = window_width/2
    posy = window_height/2
    blockSize=10
    vel = 10
    svelx = 0
    svely = 0
    gameExit = False
    gameOver = False
    appleThickness = 20
    applePosx = random.randrange(0,window_width-9,blockSize+appleThickness)
    applePosy = random.randrange(0,window_height-9,blockSize+appleThickness)
    snakeList=[[posx,posy]]
    while not gameExit:
                        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if svelx==0:                        
                        svelx = vel
                        svely = 0
                elif event.key == pygame.K_LEFT:
                    if svelx==0:
                        svelx = -vel
                        svely = 0
                elif event.key == pygame.K_UP:
                    if svely==0:                        
                        svely = -vel
                        svelx = 0
                elif event.key == pygame.K_DOWN:
                    if svely==0:
                        svely = vel
                        svelx = 0
                        
        posx += svelx
        posy += svely
        
        if posx>window_width or posx<0 or posy>window_height or posy<0:
            gameOver = True

        snakeList.append([posx,posy])
        
        if posx >= applePosx and posx <= applePosx + appleThickness and posy >= applePosy and posy <= applePosy + appleThickness:
            applePosx = random.randrange(0,window_width-9,blockSize+appleThickness)
            applePosy = random.randrange(0,window_height-9,blockSize+appleThickness)

        else:
            snakeList.pop(0)
            
        if snakeList[-1] in snakeList[0:-1]:
            gameOver = True

        if not gameOver:
            canvas.fill(black)
            pygame.draw.rect(canvas, green, [applePosx, applePosy,blockSize+20,blockSize+20])
            snake(snakeList,blockSize)
            pygame.display.update()
                

        while gameOver:
            canvas.fill(white)
            message("Press P to Play again, or q to quit",red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        gameStart()
                    elif event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                        return None
                        
        clock.tick(20)
gameStart()
pygame.quit()


#things to remember

##        if posx>=window_width or posx<=0 or posy>=window_height or posy<=0:
##            gameOver = True
##            canvas.fill(white)
##            message("Press P to Play again, or q to quit",red)
##            pygame.display.update()
##            for event in pygame.event.get():
##                if event.type == pygame.KEYDOWN:
##                    if event.key == pygame.K_p:
##                        gameStart()
##                    elif event.key == pygame.K_q:
##                        gameExit = True

##        pygame.draw.circle(canvas, red, (500,500), 50, 1)

