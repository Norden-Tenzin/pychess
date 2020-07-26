
import pygame
pygame.init()

## board color 
white, black = (255, 255, 255), (0, 0, 0)

## making a screen resolution
screen = pygame.display.set_mode([400, 400])
## setting screen color
screen.fill((255, 255, 255))

## size of each cell
cellSize = 50
board = pygame.Surface((cellSize * 8, cellSize * 8))
board.fill((white))

for y in range(0, 8, 2):
    print("y: ---->", y)
    for fb in range(0, 8, 2):
        print("fb: ", fb)
        pygame.draw.rect(board, black, (y*cellSize, fb*cellSize, cellSize, cellSize))

    for fw in range(1, 9, 2):
        print("fw: -->", fw)
        pygame.draw.rect(board, black, ((y+1)*cellSize, fw*cellSize, cellSize, cellSize))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(board, board.get_rect())
    pygame.display.flip()
pygame.quit()
