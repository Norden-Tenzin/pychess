# this will hold the classes of the chess pieces

import pygame
import random
from constants import *
import numpy as np
import math


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


def writeGame(Chessmen, posx, posy):
    maparr = readGame()
    game_map = []
    one_line = ""

    locationholder = ""
    output = ""
    empty = "##"

    # changes the values of the 2d arr
    for i, line in enumerate(maparr):
        for j, tile in enumerate(line):
            if tile.split("-")[1] == Chessmen.name:
                maparr[i][j] = maparr[i][j].split("-")[0] + "-" + empty
                maparr[math.floor(posy/50)][math.floor(posx/50)] = maparr[math.floor(
                    posy/50)][math.floor(posx/50)].split("-")[0] + "-" + Chessmen.name

    # turns 2d arr to game_map
    for line in maparr:
        for tile in line:
            one_line = one_line + tile + ","
        game_map.append(one_line + "\n")
        one_line = ""
    # print(np.matrix(game_map))

    file = open(GAMEFILE, "w+")
    file.writelines(game_map)


class Chessmen(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.clicked = False
        self.xpos = xpos
        self.ypos = ypos


# king queen bishop knight rook pawn
class King(Chessmen):
    def __init__(self, name, xpos, ypos):  
        super().__init__(xpos, ypos)
        self.name = name
        if(self.name.islower()):
            self.image = pygame.image.load(W_KING)
        else:
            self.image = pygame.image.load(B_KING)
        self.rect = self.image.get_rect()

        self.rect.x = self.xpos
        self.rect.y = self.ypos

    def moveset(self, posx, posy):
        # x = j y = i
        maparr = readGame()
        for i, line in enumerate(maparr):
            for j, tile in enumerate(line):
                if tile.split("-")[1] == self.name:
                    # print("I: " + str(i*50) + " J: " + str(j*50))
                    # print(math.floor(posx/50) * 50)
                    if (math.floor(posx/50) * 50 == j*50-(1*50)) and (math.floor(posy/50) * 50 == i*50-(0*50)):
                        print("left")
                        return True
                    elif (math.floor(posx/50) * 50 == j*50+(1*50)) and (math.floor(posy/50) * 50 == i*50-(0*50)):
                        print("right")
                        return True
                    elif (math.floor(posx/50) * 50 == j*50-(0*50)) and (math.floor(posy/50) * 50 == i*50-(1*50)):
                        print("up")
                        return True
                    elif (math.floor(posx/50) * 50 == j*50-(0*50)) and (math.floor(posy/50) * 50 == i*50+(1*50)):
                        print("down")
                        return True
                    elif (math.floor(posx/50) * 50 == j*50-(1*50)) and (math.floor(posy/50) * 50 == i*50-(1*50)):
                        print("upleft")
                        return True
                    elif (math.floor(posx/50) * 50 == j*50+(1*50)) and (math.floor(posy/50) * 50 == i*50-(1*50)):
                        print("upright")
                        return True
                    elif (math.floor(posx/50) * 50 == j*50-(1*50)) and (math.floor(posy/50) * 50 == i*50+(1*50)):
                        print("downleft")
                        return True
                    elif (math.floor(posx/50) * 50 == j*50+(1*50)) and (math.floor(posy/50) * 50 == i*50+(1*50)):
                        print("downright")
                        return True
                    else:
                        return False

    def possiblemoves(self, posx, posy):
        maparr = readGame()
        if maparr[math.floor(posy/50)][math.floor(posx/50)].find("##") >= 0 and self.moveset(posx, posy):
            return True
        else:
            return False

    def move(self, posx, posy):
        maparr = readGame()
        if self.possiblemoves(posx, posy):
            # print(np.matrix(maparr))
            writeGame(self, posx, posy)
            self.rect.x = math.floor(posx/50) * 50
            self.rect.y = math.floor(posy/50) * 50
        # elif self.canTake():

        else:
            for i, line in enumerate(maparr):
                for j, tile in enumerate(line):
                    if tile.split("-")[1] == self.name:
                        # print("I: " + str(i) + " J: " + str(j))
                        self.rect.x = j*50
                        self.rect.y = i*50
    def take(self, posx, posy):



class Queen(Chessmen):
    def __init__(self, name, xpos, ypos):  
        super().__init__(xpos, ypos)
        self.name = name
        if(self.name.islower()):
            self.image = pygame.image.load(W_QUEEN)
        else:
            self.image = pygame.image.load(B_QUEEN)
        self.rect = self.image.get_rect()

        self.rect.x = self.xpos
        self.rect.y = self.ypos


class Bishop(Chessmen):
    def __init__(self, name, xpos, ypos):  
        super().__init__(xpos, ypos)
        self.name = name
        if(self.name.islower()):
            self.image = pygame.image.load(W_BISHOP)
        else:
            self.image = pygame.image.load(B_BISHOP)
        self.rect = self.image.get_rect()

        self.rect.x = self.xpos
        self.rect.y = self.ypos


class Knight(Chessmen):
    def __init__(self, name, xpos, ypos):  
        super().__init__(xpos, ypos)
        self.name = name
        if(self.name.islower()):
            self.image = pygame.image.load(W_KNIGHT)
        else:
            self.image = pygame.image.load(B_KNIGHT)
        self.rect = self.image.get_rect()

        self.rect.x = self.xpos
        self.rect.y = self.ypos


class Rook(Chessmen):
    def __init__(self, name, xpos, ypos):  
        super().__init__(xpos, ypos)
        self.name = name
        if(self.name.islower()):
            self.image = pygame.image.load(W_ROOK)
        else:
            self.image = pygame.image.load(B_ROOK)
        self.rect = self.image.get_rect()

        self.rect.x = self.xpos
        self.rect.y = self.ypos


class Pawn(Chessmen):
    def __init__(self, name, xpos, ypos):
        super().__init__(xpos, ypos)
        self.name = name
        if(self.name.islower()):
            self.image = pygame.image.load(W_PAWN)
        else:
            self.image = pygame.image.load(B_PAWN)
        self.rect = self.image.get_rect()

        self.rect.x = self.xpos
        self.rect.y = self.ypos


# king = King("ki",0,0)
# king.show()
