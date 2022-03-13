from chessmen import *
import image_resizer
import constants
from board_maker import board_arr_maker
# loading images

# Black pieces 
b_bishop = pygame.image.load(B_BISHOP)
b_king = pygame.image.load(B_KING)
b_knight = pygame.image.load(B_KNIGHT)
b_pawn = pygame.image.load(B_PAWN)
b_queen = pygame.image.load(B_QUEEN)
b_rook = pygame.image.load(B_ROOK)

# White pieces
w_bishop = pygame.image.load(W_BISHOP)
w_king = pygame.image.load(W_KING)
w_knight = pygame.image.load(W_KNIGHT)
w_pawn = pygame.image.load(W_PAWN)
w_queen = pygame.image.load(W_QUEEN)
w_rook = pygame.image.load(W_ROOK)

# Sprite Groups
whitepieces = pygame.sprite.Group()
blackpieces = pygame.sprite.Group()
boardpieces = pygame.sprite.Group()

def initialize():
    pygame.init()
    screen = pygame.display.set_mode((SIZE, SIZE))
    pygame.display.set_caption("Multiplayer Chess")
    return screen

def drawBoard(screen):
    screen.fill((DARKER))
    for y in range(0, 8, 2):
        for fb in range(0, 8, 2):
            pygame.draw.rect(screen, WHITE, (y*CELLSIZE, fb *
                                            CELLSIZE, CELLSIZE, CELLSIZE))
        for fw in range(1, 9, 2):
            pygame.draw.rect(screen, WHITE, ((y+1)*CELLSIZE,
                                            fw*CELLSIZE, CELLSIZE, CELLSIZE))

    pygame.font.init()
    numbs = ["8", "7", "6", "5", "4", "3", "2", "1"]
    alpha = ["a", "b", "c", "d", "e", "f", "g", "h"]
    colornumbs = [DARKER, WHITE]
    coloralpha = [WHITE, DARKER]

    myfont = pygame.font.SysFont('arialblack', 15)
    for i in range(0, 8):
        textSurface = myfont.render(numbs[i], True, colornumbs[i % 2])
        screen.blit(textSurface, (2, CELLSIZE * i))
    for i in range(0, 8):
        textSurface = myfont.render(alpha[i], True, coloralpha[i % 2])
        screen.blit(textSurface, ((CELLSIZE * (i+1)) - (CELLSIZE*.25), SIZE - (CELLSIZE*.4)))

def drawPieces(screen, board):  # 3
    maparr = board
    letterHolder = ""
    for i, line in enumerate(maparr):
        for j, tile in enumerate(line):
            if(tile.split("-")[1].lower() == "bi"):
                if(tile.split("-")[1].strip()[0].islower()):
                    whitepieces.add(
                        Bishop(tile.split("-")[1], tile.split("-")[0], (j)*CELLSIZE, (i)*CELLSIZE))
                else:
                    blackpieces.add(
                        Bishop(tile.split("-")[1], tile.split("-")[0], (j)*CELLSIZE, (i)*CELLSIZE))
            elif(tile.split("-")[1].lower() == "ki"):
                if(tile.split("-")[1].strip()[0].islower()):
                    whitepieces.add(
                        King(tile.split("-")[1], tile.split("-")[0], (j)*CELLSIZE, (i)*CELLSIZE))
                else:
                    blackpieces.add(
                        King(tile.split("-")[1], tile.split("-")[0], (j)*CELLSIZE, (i)*CELLSIZE))
            elif(tile.split("-")[1].lower() == "kn"):
                if(tile.split("-")[1].strip()[0].islower()):
                    whitepieces.add(
                        Knight(tile.split("-")[1], tile.split("-")[0], (j)*CELLSIZE, (i)*CELLSIZE))
                else:
                    blackpieces.add(
                        Knight(tile.split("-")[1], tile.split("-")[0], (j)*CELLSIZE, (i)*CELLSIZE))
            elif(tile.split("-")[1].lower() == "pa"):
                if(tile.split("-")[1].strip()[0].islower()):
                    whitepieces.add(
                        Pawn(tile.split("-")[1], tile.split("-")[0], (j)*CELLSIZE, (i)*CELLSIZE))
                else:
                    blackpieces.add(
                        Pawn(tile.split("-")[1], tile.split("-")[0], (j)*CELLSIZE, (i)*CELLSIZE))
            elif(tile.split("-")[1].lower() == "qu"):
                if(tile.split("-")[1].strip()[0].islower()):
                    whitepieces.add(
                        Queen(tile.split("-")[1], tile.split("-")[0], (j)*CELLSIZE, (i)*CELLSIZE))
                else:
                    blackpieces.add(
                        Queen(tile.split("-")[1], tile.split("-")[0], (j)*CELLSIZE, (i)*CELLSIZE))
            elif(tile.split("-")[1].lower() == "ro"):
                if(tile.split("-")[1].strip()[0].islower()):
                    whitepieces.add(
                        Rook(tile.split("-")[1], tile.split("-")[0], (j)*CELLSIZE, (i)*CELLSIZE))
                else:
                    blackpieces.add(
                        Rook(tile.split("-")[1], tile.split("-")[0], (j)*CELLSIZE, (i)*CELLSIZE))
    boardpieces.add(whitepieces)
    boardpieces.add(blackpieces)

# seperate the gameloop with rendering the board
def gameLoop(screen, maparr):
    game_map_arr = maparr
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
                if event.button == 1:
                    for chesspiece in boardpieces:
                        if chesspiece.rect.collidepoint(posx, posy):
                            chesspiece.clicked = True

            if event.type == pygame.MOUSEBUTTONUP:
                for chesspiece in boardpieces:
                    chesspiece.clicked = False
                if selected:
                    movekind, game_map_arr = selected[0].move(posx, posy, game_map_arr)
                    if selected[0].name.strip()[0].islower() and movekind == 1:
                        collision_list = pygame.sprite.spritecollide(selected[0], blackpieces, True)
                    elif selected[0].name.strip()[0].isupper() and movekind == 1:
                        collision_list = pygame.sprite.spritecollide(selected[0], whitepieces, True)
                    selected = []

        for chesspiece in boardpieces:
            if chesspiece.clicked == True:
                selected = [chesspiece]
            if selected:
                selected[0].rect.x = (math.floor(posx)) - 25
                selected[0].rect.y = (math.floor(posy)) - 25
        drawBoard(screen)
        blackpieces.draw(screen)
        whitepieces.draw(screen)
        pygame.display.flip()
