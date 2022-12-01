import pygame
pygame.font.init()
# Color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK = (125, 135, 150)
LIGHTDARK = (156, 169, 189)
DARKER = (90, 98, 111)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
ORANGE = (255,99,71)
LIGHTORANGE = (255, 157, 143)
YELLOW  = (255,255,0)

# font
MYFONT = pygame.font.SysFont('arialblack', 15)
CURRTURN = pygame.font.SysFont('arialblack', 12)

# Sizes
UISPACE = 400
SIZE = 400 
# screen size
SCREEN_SIZE = (SIZE, SIZE+20)
CELLSIZE = int(SIZE/8)
INDEXSIZE = int(SIZE/50)

# File add
GAMEFILE = "game.txt"

# Image add
B_BISHOP = "../assets/b_bishop.png"
B_KING = "../assets/b_king.png"
B_KNIGHT = "../assets/b_knight.png"
B_PAWN = "../assets/b_pawn.png"
B_QUEEN = "../assets/b_queen.png"
B_ROOK = "../assets/b_rook.png"

W_BISHOP = "../assets/w_bishop.png"
W_KING = "../assets/w_king.png"
W_KNIGHT = "../assets/w_knight.png"
W_PAWN = "../assets/w_pawn.png"
W_QUEEN = "../assets/w_queen.png"
W_ROOK = "../assets/w_rook.png"

TICK = "../assets/tick.png"

# Lists 
ALPHA = ["a", "b", "c", "d", "e", "f", "g", "h"]
NUMBS = ["1", "2", "3", "4", "5", "6", "7", "8"]

BACK_PIECES = ["Ro", "Kn", "Bi", "Qu", "Ki", "Bi", "Kn", "Ro"]
BACK_PAWNS = ["Pa", "Pa", "Pa", "Pa", "Pa", "Pa", "Pa", "Pa"]

FRONT_PAWNS = ["pa", "pa", "pa", "pa", "pa", "pa", "pa", "pa"]
FRONT_PIECES = ["ro", "kn", "bi", "qu", "ki", "bi", "kn", "ro"]
# NUMBS = ["8", "7", "6", "5", "4", "3", "2", "1"]