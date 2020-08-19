import math
import pygame
import random
import sys
import math
import numpy as np
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
    # print(np.matrix(maparr))
    return maparr


def writeGame(Chessmen, posx, posy): # turns 2d arr to text
    maparr = readGame()
    game_map = []
    one_line = ""

    locationholder = ""
    output = ""
    empty = "##"

    for i, line in enumerate(maparr):
        for j, tile in enumerate(line):
            if tile.split("-")[1] == Chessmen.name:
                maparr[i][j] = maparr[i][j].split("-")[0] + "-" + empty
                maparr[math.floor(posy/50)][math.floor(posx/50)] = maparr[math.floor(
                    posy/50)][math.floor(posx/50)].split("-")[0] + "-" + Chessmen.name
    for line in maparr:
        for tile in line:
            one_line = one_line + tile + ","
        game_map.append(one_line + "\n")
        one_line = ""

    # print(np.matrix(game_map))
    file = open(GAMEFILE, "w+")
    file.writelines(game_map)