import pygame
from LogicOfLifeGame import game
def drawGrid(l):
    for row in range(0, h-40, blockSize):
        for col in range(0, w, blockSize):
            rect = pygame.Rect(col, row, blockSize, blockSize)
            color = (100,100,100)
            if(l[row//blockSize][col//blockSize] == '1'):
                screen.fill((0, 255, 0), rect) 
            pygame.draw.rect(screen, color, rect, 1)

l = [['0' for _ in range(15)] for __ in range(15)]

blockSize = 20
sizeH = len(l)
sizeW = len(l[0])
w = blockSize*sizeW
h = blockSize*sizeH + 40


pygame.init()
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()
startButton = pygame.Rect(w/2-27.5, h-30, 55, 25)
font = pygame.font.SysFont('Comic Sans MS', 20)
text = font.render('Start', False, (255,255,255))

isGameStarted = False
isRunning = True
while isRunning:
    screen.fill((0,0,0))
    if(isGameStarted == True):
        l = game(l)
        clock.tick(4)
    if(isGameStarted == False):
        pygame.draw.rect(screen, (0, 155, 0), startButton)
        screen.blit(text, (w/2-27, h-33))
        clock.tick(10)
    drawGrid(l)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mousePos = event.pos
            mouseCol, mouseRow = mousePos
            for row in range(0, h-40, blockSize):
                for col in range(0, w, blockSize):                    
                    if(row < mouseRow < row+blockSize):
                        if(col < mouseCol < col+blockSize):
                            if(l[row//blockSize][col//blockSize] == '1'):
                                l[row//blockSize][col//blockSize] = '0'
                            elif(l[row//blockSize][col//blockSize] == '0'):
                                l[row//blockSize][col//blockSize] = '1'    
            if(310 < mouseRow < 335):
                if(125 < mouseCol < 175):
                    isGameStarted = True
                    screen = pygame.display.set_mode((w, h-40))
        if event.type == pygame.QUIT:
            isRunning = False

    pygame.display.update()
pygame.quit()
