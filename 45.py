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
            
l = []
with open('45.txt','r+') as file:
    l1 = file.read().split()
    for x in range(len(l1)):
        l.append(list(l1[x]))

blockSize = 20
sizeH = len(l)
sizeW = len(l[0])
w = blockSize*sizeW
h = blockSize*sizeH

pygame.init()
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

isGameRun = True
while isGameRun:
    screen.fill((0,0,0))
    l = game(l)
    drawGrid(l)
    clock.tick(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isGameRun = False
    pygame.display.update()
pygame.quit()