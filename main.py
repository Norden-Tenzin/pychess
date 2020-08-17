# comments are just there for me to understand whats going on

import pygame
import sys
import math
import numpy as np
from constants import *
from chessmen import *
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

# variables
done = False
key_list = pygame.sprite.Group()


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

     # TODO to add text inside the game on the sides
    # pygame.font.init()
    # myfont = pygame.font.SysFont('Comic Sans Ms', 30)
    # textSurface = myfont.render("Something", False, BLACK)
    # board.blit(textSurface,(0,0))
    return board


def readGame(): # turns the text into a 2d arr
    maparr = []
    one_line = []
    one_tile = ""
    with open(GAMEFILE, 'r') as f:
        game_map = f.readlines()
    game_map = [line.strip() for line in game_map]
    
    for i, tile in enumerate(game_map):
        for j, tile_content in enumerate(tile):
            one_tile = one_tile + tile_content
            if(tile_content == ","):
                one_tile = one_tile.replace(',', "")
                one_line.append(one_tile)
                one_tile = ""
        maparr.insert(i, one_line)
        one_line = []
    # print(np.matrix(maparr))
    return maparr

def writeGame(Chessmen):
    maparr = readGame()

    # file = open(GAMEFILE, "w+")
    # file.writelines(map2d)


def drawPieces(screen):  # 3
    maparr = readGame()
    letterHolder = ""

    # having letters for location might have been a mistake
    # i - board x axis index, j - board y axis index

    # renders pieces from the 2d arr ## this might not be req at all
    # letter holder possibilities: bi ki kn pa qu ro and uppercase total 12 + ## = 13
    # writeGame(maparr)

    for i, line in enumerate(maparr):
        for j, tile in enumerate(line):
            # if(tile.split("-")[1] == "##"):
            #     i += i
            if(tile.split("-")[1].lower() == "bi"):
                key_list.add(
                    Bishop(tile.split("-")[1], (j)*CELLSIZE, (i)*CELLSIZE))
            elif(tile.split("-")[1].lower() == "ki"):
                key_list.add(
                    King(tile.split("-")[1], (j)*CELLSIZE, (i)*CELLSIZE))
            elif(tile.split("-")[1].lower() == "kn"):
                key_list.add(
                    Knight(tile.split("-")[1], (j)*CELLSIZE, (i)*CELLSIZE))
            elif(tile.split("-")[1].lower() == "pa"):
                key_list.add(
                    Pawn(tile.split("-")[1], (j)*CELLSIZE, (i)*CELLSIZE))
            elif(tile.split("-")[1].lower() == "qu"):
                key_list.add(
                    Queen(tile.split("-")[1], (j)*CELLSIZE, (i)*CELLSIZE))
            elif(tile.split("-")[1].lower() == "ro"):
                key_list.add(
                    Rook(tile.split("-")[1], (j)*CELLSIZE, (i)*CELLSIZE))

def gameLoop(screen):
    maparr = readGame()
    selected = []
    while True:
        posx, posy = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # if event.button == 3:
                #     key_list.add(Chessmen(x, y)) dont want to add to the list
                if event.button == 1:
                    for chesspiece in key_list:
                        if chesspiece.rect.collidepoint(posx, posy):
                            chesspiece.clicked = True

            if event.type == pygame.MOUSEBUTTONUP:
                for chesspiece in key_list:
                    chesspiece.clicked = False
                if selected:
                    selected[0].move(posx, posy)
                    selected = []
                # chesspiece.move(posx, posy)
                drag_id = 0
        for chesspiece in key_list:
            if chesspiece.clicked == True:
                selected = [chesspiece]
            if selected:
                selected[0].rect.x = (math.floor(posx)) - 25
                selected[0].rect.y = (math.floor(posy)) - 25
                # print(str(selected[0].name) + ": x => " +
                #       str(math.floor(posx/50)) + " y => " + str(math.floor(posy/50)))
                # print(maparr[(math.floor(posy/50))][(math.floor(posx/50))])
        board = drawBoard()
    # blit adds the new surface onto the old surface
        screen.blit(board, board.get_rect())
        key_list.draw(screen)
        pygame.display.update()


def main():
    screen = initialize()

    board = drawBoard()
    screen.blit(board, board.get_rect())
    drawPieces(screen)  # 2 initializes the board with pieces
    gameLoop(screen)  # 1


if __name__ == "__main__":
    main()
