# comments are just there for me to understand whats going on

import pygame
import sys
from constants import *
from array import *

# loading images
# black
b_bishop = pygame.image.load(B_BISHOP)
b_king = pygame.image.load(B_KING)
b_knight = pygame.image.load(B_KNIGHT)
b_pawn = pygame.image.load(B_PAWN)
b_queen = pygame.image.load(B_QUEEN)
b_rook = pygame.image.load(B_ROOK)

# white
w_bishop = pygame.image.load(W_BISHOP)
w_king = pygame.image.load(W_KING)
w_knight = pygame.image.load(W_KNIGHT)
w_pawn = pygame.image.load(W_PAWN)
w_queen = pygame.image.load(W_QUEEN)
w_rook = pygame.image.load(W_ROOK)


def initialize():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Multiplayer Chess")
    return screen


def drawBoard():
    board = pygame.Surface((CELLSIZE * 8, CELLSIZE * 8))
    board.fill((DARK))

    for y in range(0, 8, 2):
        for fb in range(0, 8, 2):
            pygame.draw.rect(board, WHITE, (y*CELLSIZE, fb *
                                            CELLSIZE, CELLSIZE, CELLSIZE))
        for fw in range(1, 9, 2):
            pygame.draw.rect(board, WHITE, ((y+1)*CELLSIZE,
                                            fw*CELLSIZE, CELLSIZE, CELLSIZE))
    return board


def drawPieces(screen, game_tiles):  # 3
    arr2d = []
    one_line = []
    one_tile = ""
    letterHolder = ""

    # turns the text into a 2d arr
    for i, tile in enumerate(game_tiles):
        for j, tile_content in enumerate(tile):
            one_tile = one_tile + tile_content
            if(tile_content == ")"):
                one_line.append(one_tile)
                one_tile = ""
        arr2d.insert(i, one_line)
        one_line = []
        
    # having letters for location might have been a mistake
    # i - board x axis index, j - board y axis index

    # renders pieces from the 2d arr ## this might not be req at all
    # letter holder possibilities: bi ki kn pa qu ro and uppercase total 12 + ## = 13

    for i, line in enumerate(arr2d):
        for j, tile in enumerate(line):
            tileHolder = tile.strip("()")
            for k, letter in enumerate(tileHolder):
                if(letter == "-"):
                    letterHolder = letterHolder + \
                        tileHolder[k+1] + tileHolder[k+2]
                    if(letterHolder == "##"):
                        i = 10
                    elif(letterHolder.lower() == "bi"):
                        if(letterHolder.islower()):
                            screen.blit(w_bishop, ((j)*CELLSIZE, (i)*CELLSIZE))
                        else:
                            screen.blit(b_bishop, ((j)*CELLSIZE, (i)*CELLSIZE))
                    elif(letterHolder.lower() == "ki"):
                        if(letterHolder.islower()):
                            screen.blit(w_king, ((j)*CELLSIZE, (i)*CELLSIZE))
                        else:
                            screen.blit(b_king, ((j)*CELLSIZE, (i)*CELLSIZE))
                    elif(letterHolder.lower() == "kn"):
                        if(letterHolder.islower()):
                            screen.blit(w_knight, ((j)*CELLSIZE, (i)*CELLSIZE))
                        else:
                            screen.blit(b_knight, ((j)*CELLSIZE, (i)*CELLSIZE))
                    elif(letterHolder.lower() == "pa"):
                        if(letterHolder.islower()):
                            screen.blit(w_pawn, ((j)*CELLSIZE, (i)*CELLSIZE))
                        else:
                            screen.blit(b_pawn, ((j)*CELLSIZE, (i)*CELLSIZE))
                    elif(letterHolder.lower() == "qu"):
                        if(letterHolder.islower()):
                            screen.blit(w_queen, ((j)*CELLSIZE, (i)*CELLSIZE))
                        else:
                            screen.blit(b_queen, ((j)*CELLSIZE, (i)*CELLSIZE))
                    elif(letterHolder.lower() == "ro"):
                        if(letterHolder.islower()):
                            screen.blit(w_rook, ((j)*CELLSIZE, (i)*CELLSIZE))
                        else:
                            screen.blit(b_rook, ((j)*CELLSIZE, (i)*CELLSIZE))
                    k = k + 2
            letterHolder = ""


def readGame():
    with open(GAMEFILE, 'r') as f:
        game_map = f.readlines()
    game_map = [line.strip() for line in game_map]
    return game_map


def gameLoop(screen, game_map):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
        drawPieces(screen, game_map)  # 2
        pygame.display.update()


def main():
    screen = initialize()

    board = drawBoard()
    # blit adds the new surface onto the old surface
    screen.blit(board, board.get_rect())

    game_map = readGame()
    gameLoop(screen, game_map)  # 1


if __name__ == "__main__":
    main()
