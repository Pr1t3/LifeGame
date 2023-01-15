import pygame
from gameLife import game
def drawGrid(l):
    for row in range(0, h, blockSize):
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
h = blockSize*sizeH

pygame.init()
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

isGameStarted = False
isRunning = True
while isRunning:
    screen.fill((0,0,0))
    if(isGameStarted):
        l = game(l)
    drawGrid(l)
    clock.tick(5)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mousePos = event.pos
            for row in range(0, h, blockSize):
                for col in range(0, w, blockSize):
                    mouseCol, mouseRow = mousePos
                    if(row < mouseRow < row+blockSize):
                        if(col < mouseCol < col+blockSize):
                            l[row//blockSize][col//blockSize] = '1'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DELETE:
            isGameStarted = True
        if event.type == pygame.QUIT:
            isRunning = False
    
    pygame.display.update()
pygame.quit()