import pygame
from LogicOfLifeGame import game
def drawGrid(l, blockSize, screen, h, w):
    for row in range(0, h-40, blockSize):
        for col in range(0, w, blockSize):
            rect = pygame.Rect(col, row, blockSize, blockSize)
            color = (100,100,100)
            if(l[row//blockSize][col//blockSize] == '1'):
                screen.fill((0, 255, 0), rect) 
            pygame.draw.rect(screen, color, rect, 1)

def main():
    l = [['0' for _ in range(45)] for __ in range(30)]
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
    prevMousePos = (0, 0)
    isPainting = False
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
            clock.tick(60)
        drawGrid(l, blockSize, screen, h, w)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                isPainting = True
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                isPainting = False
            if(isPainting == True):
                try:
                    mousePos = event.pos
                    mouseCol, mouseRow = mousePos
                    for row in range(0, h-40, blockSize):
                        for col in range(0, w, blockSize):                    
                            if(row < mouseRow < row+blockSize):
                                if(col < mouseCol < col+blockSize):
                                    if(prevMousePos != (col, row)):
                                        if(l[row//blockSize][col//blockSize] == '1'):
                                            l[row//blockSize][col//blockSize] = '0'
                                        elif(l[row//blockSize][col//blockSize] == '0'):
                                            l[row//blockSize][col//blockSize] = '1' 
                                        prevMousePos = (col, row)
                    if(h-33 < mouseRow < h-33+25):
                        if(w/2-28 < mouseCol < w/2-28+55):
                            isGameStarted = True
                            screen = pygame.display.set_mode((w, h-40))
                except:
                    isPainting = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                main()
            if event.type == pygame.QUIT:
                isRunning = False
        pygame.display.update()
    pygame.quit()
if(__name__ == '__main__'):
    main()
