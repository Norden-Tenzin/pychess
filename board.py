
import pygame

white, black = (255, 255, 255), (0, 0, 0)

def main():
    pygame.init()
    screen = pygame.display.set_mode([400, 400])
    screen.fill((255, 255, 255))

    running = True
    board = drawBoard()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(board, board.get_rect())
        pygame.display.flip()

    pygame.quit()

def drawBoard():
    cellSize = 50
    board = pygame.Surface((cellSize * 8, cellSize * 8))
    board.fill((white))

    for y in range(0, 8, 2):
        for fb in range(0, 8, 2):
            pygame.draw.rect(board, black, (y*cellSize, fb*cellSize, cellSize, cellSize))

        for fw in range(1, 9, 2):
            pygame.draw.rect(board, black, ((y+1)*cellSize, fw*cellSize, cellSize, cellSize))
    return board

if __name__=="__main__": 
    main() 