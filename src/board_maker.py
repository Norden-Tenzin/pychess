import string
import numpy as np
from constants import *

alphabetsoup = list(map(chr, range(97, 105)))
def make_temp(pieces_to_show = None):
    # pieces_to_show = ['ki', "Ki"]
    blackpieces = ["Ro", "Kn", "Bi", "Qu", "Ki", "Bi", "Kn", "Ro", "Pa", "Pa", "Pa", "Pa", "Pa", "Pa", "Pa", "Pa"]
    whitepieces = ["pa", "pa", "pa", "pa", "pa", "pa", "pa", "pa", "ro", "kn", "bi", "qu", "ki", "bi", "kn", "ro"]
    if pieces_to_show:
        whitepieces = [i if i in pieces_to_show else "##" for i in whitepieces]
        blackpieces = [i if i in pieces_to_show else "##" for i in blackpieces]
    white_temp={}
    for i, a in enumerate(alphabetsoup[::-1] + alphabetsoup[::-1]):
        if i < 8:
            white_temp[a+str(2)] = whitepieces[i]
        else:
            white_temp[a+str(1)] = whitepieces[i]
    black_temp={}
    for i, a in enumerate(alphabetsoup + alphabetsoup):
        if i < 8:
            black_temp[a+str(8)] = blackpieces[i]
        else:
            black_temp[a+str(7)] = blackpieces[i]
    return(white_temp, black_temp)

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

# play as 0 means white, play as 1 means black. 
def board_arr_maker(play_as, pieces_to_show = None):
    white_pieces, black_pieces = make_temp(pieces_to_show)
    oneBoard = board_empty(play_as)
    for x, line in enumerate(oneBoard):
        for y, item in enumerate(line):
            if get_val_temp(white_pieces, item.split('-', 1)[0]):
                v = get_val_temp(white_pieces, item.split('-', 1)[0])
                oneBoard[x][y] = item.split('-', 1)[0] + "-" + v
            if get_val_temp(black_pieces, item.split('-', 1)[0]):
                v = get_val_temp(black_pieces, item.split('-', 1)[0])
                oneBoard[x][y] = item.split('-', 1)[0] + "-" + v
    return oneBoard

# def board_arr_maker_old():
#     oneList = []
#     oneBoard = []
#     for x in range(8, 0, -1):
#         for i, y in enumerate(alphabetsoup):
#             if x == 8:
#                 oneList.append(y + str(x) + "-" + str(blackpieces[i]))
#             elif x == 7:
#                 oneList.append(y + str(x) + "-" + str(blackpieces[i+8]))
#             elif x == 2:
#                 oneList.append(y + str(x) + "-" + str(whitepieces[i]))
#             elif x == 1:
#                 oneList.append(y + str(x) + "-" + str(whitepieces[i+8]))
#             else:
#                 oneList.append(y + str(x) + "-##")
#         oneBoard.append(oneList)
#         oneList = []
#     # print(np.matrix(oneBoard))
#     return oneBoard

# def board_file_maker():
#     oneList = ""
#     oneBoard = []
#     for x in range(8, 0, -1):
#         for i, y in enumerate(alphabetsoup):
#             if x == 8:
#                 oneList = (oneList + y + str(x) + "-" + str(blackpieces[i]) + ",")
#             elif x == 7:
#                 oneList = (oneList + y + str(x) + "-" + str(blackpieces[i+8]) + ",")
#             elif x == 2:
#                 oneList = (oneList + y + str(x) + "-" + str(whitepieces[i]) + ",")
#             elif x == 1:
#                 oneList = (oneList + y + str(x) + "-" + str(whitepieces[i+8]) + ",")
#             else:
#                 oneList = (oneList + y + str(x) + "-##,")
#         oneBoard.append(oneList + "\n")
#         oneList = ""
#     file = open(GAMEFILE, "w+")
#     file.writelines(oneBoard)

if __name__ == "__main__":
    play_as = 1
    b = board_arr_maker(play_as, ['ki', 'Ki', 'qu', 'Qu'])
    # print(np.matrix(b))