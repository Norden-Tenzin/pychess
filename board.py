import pygame
import sys
from constants import *


def readGame():
    with open(GAMEFILE, 'r') as f:
        game_map = f.readlines()
    game_map = [line.strip() for line in game_map]
    print(game_map)


def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    screen.fill(WHITE)

    board = drawBoard()
    readGame()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

        screen.blit(board, board.get_rect())
        pygame.display.flip()


def drawBoard():
    board = pygame.Surface((CELLSIZE * 8, CELLSIZE * 8))
    board.fill((WHITE))

    for y in range(0, 8, 2):
        for fb in range(0, 8, 2):
            pygame.draw.rect(board, BLACK, (y*CELLSIZE, fb *
                                            CELLSIZE, CELLSIZE, CELLSIZE))

        for fw in range(1, 9, 2):
            pygame.draw.rect(board, BLACK, ((y+1)*CELLSIZE,
                                            fw*CELLSIZE, CELLSIZE, CELLSIZE))
    return board


if __name__ == "__main__":
    main()
