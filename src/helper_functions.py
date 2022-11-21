import math
import pygame
import random
import sys
import math
import numpy as np
from board_maker import *
from constants import *

# holds all the main imports
# helper funcs
def readGame():  # turns the text into a 2d arr
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
    return maparr

def writeGame(Chessmen, posx, posy, maparr):  # turns 2d arr to text
    game_map = []
    one_line = ""
    locationholder = ""
    output = ""
    empty = "##"

    for i, line in enumerate(maparr):
        for j, tile in enumerate(line):
            if tile.split("-")[0] == Chessmen.location and tile.split("-")[1] == Chessmen.name:
                maparr[i][j] = maparr[i][j].split("-")[0] + "-" + empty
                maparr[posy][posx] = maparr[posy][posx].split("-")[0] + "-" + Chessmen.name
    return maparr

def location_to_pos(play_as, location):
    # print("IN LOCATION_TO_POS")
    # print("LOCATION: {}".format(location))
    # print(play_as, location)
    xval = 0
    yval = 0
    alpha = ALPHA.copy()
    numbs = NUMBS.copy()
    final = []
    # e,2 = 4,6
    if play_as == 0:
        for i, letter in enumerate(alpha):
            if letter == location.strip()[0]:
                xval = i

        for j, numb in enumerate(numbs[::-1]):
            if numb == location.strip()[1]:
                yval = j
        final = [yval, xval]
    else:
        for i, letter in enumerate(alpha[::-1]):
            if letter == location.strip()[0]:
                xval = i

        for j, numb in enumerate(numbs):
            if numb == location.strip()[1]:
                yval = j
        final = [yval, xval]
    # print("POS: {}".format(final))
    return final

def pos_to_location(play_as, pos):
    # print("IN POS_TO_LOCATION")
    # print("POS: {}".format(pos))
    # letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    # numbs = [8, 7, 6, 5, 4, 3, 2, 1]
    # final = letters[pos[1]] + str(numbs[pos[0]])
    final = board_empty(play_as)[pos[0]][pos[1]].split("-")[0]
    # print("LOCATION: {}".format(final))
    return final

def func_test(play_as):
    board = board_empty_just_location(play_as)
    for i, line in enumerate(board):
        for j, item in enumerate(line):
            y, x = location_to_pos(play_as, item)
            board[i][j] = "{},{}".format(x, y) 
    print(np.matrix(board))

if __name__ == "__main__":
    sample_loc = "d7"
    pos = location_to_pos(1, sample_loc)
    print(pos)
    print(pos_to_location(1, pos))
    # func_test(1)
    # board = board_empty_just_location(1)
    # print(np.matrix(board))
    