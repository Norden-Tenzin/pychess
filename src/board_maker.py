import string
import numpy as np
from constants import *

alphabetsoup = list(map(chr, range(97, 105)))
def make_piece_dicts(play_as, pieces_to_show = None):
    # TODO pieces_to_show = ['ki', "Ki"]
    back_pieces = BACK_PIECES.copy()
    back_pawns = BACK_PAWNS.copy()
    front_pieces = FRONT_PIECES.copy()
    front_pawns = FRONT_PAWNS.copy()

    if pieces_to_show:
        front_pawns = [i if i in pieces_to_show else "##" for i in front_pawns]
        front_pieces = [i if i in pieces_to_show else "##" for i in front_pieces]
        back_pawns = [i if i in pieces_to_show else "##" for i in back_pawns]
        back_pieces = [i if i in pieces_to_show else "##" for i in back_pieces]
        
    if play_as == 0:
        front_temp={}
        for i, a in enumerate(alphabetsoup + alphabetsoup):
            if i < 8:
                front_temp[a+str(2)] = front_pawns[i]
                front_temp[a+str(1)] = front_pieces[i]
        back_temp={}
        for i, a in enumerate(alphabetsoup + alphabetsoup):
            if i < 8:
                back_temp[a+str(7)] = back_pawns[i]
                back_temp[a+str(8)] = back_pieces[i]
    elif play_as == 1:
        front_temp={}
        for i, a in enumerate(alphabetsoup[::-1] + alphabetsoup[::-1]):
            if i < 8:
                front_temp[a+str(7)] = front_pawns[i]
                front_temp[a+str(8)] = front_pieces[i]
        back_temp={}
        for i, a in enumerate(alphabetsoup[::-1] + alphabetsoup[::-1]):
            if i < 8:
                back_temp[a+str(2)] = back_pawns[i]
                back_temp[a+str(1)] = back_pieces[i]
    return(front_temp, back_temp)

def get_val_temp(temp, key):
    for k, v in temp.items():  
        if k == key:
            return v
    return None

def board_empty(play_as):
    oneList =[]
    oneBoard = []
    if play_as == 0:
        for x in range(8, 0, -1):
            for i, y in enumerate(alphabetsoup):
                oneList.append((y + str(x) + "-##"))
            oneBoard.append(oneList)
            oneList = []
    if play_as == 1:
        for x in range(1, 9, 1):
            for i, y in enumerate(alphabetsoup[::-1]):
                oneList.append((y + str(x) + "-##"))
            oneBoard.append(oneList)
            oneList = []
    return oneBoard

def board_empty_just_location(play_as):
    oneList =[]
    oneBoard = []
    if play_as == 0:
        for x in range(8, 0, -1):
            for i, y in enumerate(alphabetsoup):
                oneList.append((y + str(x)))
            oneBoard.append(oneList)
            oneList = []
    if play_as == 1:
        for x in range(1, 9, 1):
            for i, y in enumerate(alphabetsoup[::-1]):
                oneList.append((y + str(x)))
            oneBoard.append(oneList)
            oneList = []
    return oneBoard

# play as 0 means white, play as 1 means black. 
def board_arr_maker(play_as, pieces_to_show = None):
    front_pieces, back_pieces = make_piece_dicts(play_as, pieces_to_show)
    oneBoard = board_empty(play_as)
    for x, line in enumerate(oneBoard):
        for y, item in enumerate(line):
            if get_val_temp(front_pieces, item.split('-', 1)[0]):
                v = get_val_temp(front_pieces, item.split('-', 1)[0])
                oneBoard[x][y] = item.split('-', 1)[0] + "-" + v
            if get_val_temp(back_pieces, item.split('-', 1)[0]):
                v = get_val_temp(back_pieces, item.split('-', 1)[0])
                oneBoard[x][y] = item.split('-', 1)[0] + "-" + v
    return oneBoard

if __name__ == "__main__":
    play_as = 1
    # b = board_arr_maker(play_as, ['ki', 'Ki', 'qu', 'Qu', 'ro', 'Ro', 'kn', 'Kn', 'bi', 'Bi'])
    b = board_arr_maker(play_as)
    print(np.matrix(b))

