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

def draw_board(screen):
    screen.fill((DARKER))
    for y in range(0, 8, 2):
        for fb in range(0, 8, 2):
            pygame.draw.rect(screen, WHITE, (y*CELLSIZE, fb *
                                            CELLSIZE, CELLSIZE, CELLSIZE))
        for fw in range(1, 9, 2):
            pygame.draw.rect(screen, WHITE, ((y+1)*CELLSIZE,
                                            fw*CELLSIZE, CELLSIZE, CELLSIZE))

def draw_font(screen):
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

def draw_path(screen, path, curr):
    currx, curry = curr
    for k, v in path.items():
        if v['open']:
            for x, y in v['open']:
                pygame.draw.rect(screen, GREEN, (CELLSIZE*y, CELLSIZE*x, CELLSIZE, CELLSIZE))
        if v['hit']:
            for x, y in v['hit']:
                pygame.draw.rect(screen, RED, (CELLSIZE*y, CELLSIZE*x, CELLSIZE, CELLSIZE))
            # pygame.draw.rect(screen, RED, (CELLSIZE*v['hit'][1], CELLSIZE*v['hit'][0], CELLSIZE, CELLSIZE))
    pygame.draw.rect(screen, ORANGE, (currx, curry, CELLSIZE, CELLSIZE))

def draw_pieces(screen, board):  # 3
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

def write_notation(name, to):
    pass

# TODO seperate the gameloop with rendering the board
def game_loop(screen, maparr, playAs):
    move_mem = []
    curr_turn = 0

    game_map_arr = maparr
    selected = []
    is_path = False

    while True:
        posx, posy = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print(move_mem)
                    sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for chesspiece in boardpieces:
                        if chesspiece.rect.collidepoint(posx, posy):
                            path = None
                            chesspiece.clicked = True
                            path, curr = chesspiece.clear_paths(posx, posy, playAs, maparr)
                            is_path = True

            if event.type == pygame.MOUSEBUTTONUP:
                for chesspiece in boardpieces:
                    chesspiece.clicked = False
                
                # if a chess piece has been selected 
                if selected: 

                    print(curr_turn)
                    move_line = []
                    # if its the white's turn and the selected piece is also white
                    if curr_turn == 0 and selected[0].name[0].islower():
                        old_pos = location_to_pos(selected[0].location)
                        pos = math.floor(posy/CELLSIZE), math.floor(posx/CELLSIZE)

                        movekind, game_map_arr, is_path = selected[0].move(posx, posy, game_map_arr)

                        print(movekind)

                        if movekind > -1:
                            curr_turn = 1
                            name = selected[0].name


                            move_mem.append("WHITE: NAME: {} FROM: [{},{}] TO: [{},{}]".format(name, old_pos[1], old_pos[0], pos[1], pos[0]))

                            # get new_location
                            # add move_line
                        else:
                            # recenter
                            oldPos = location_to_pos(selected[0].location)
                            movekind, game_map_arr, is_path = selected[0].move(oldPos[1], oldPos[0], game_map_arr)
                    # if its the black's turn and the selected piece is also black
                    elif curr_turn == 1 and selected[0].name[0].isupper():
                        old_pos = location_to_pos(selected[0].location)
                        pos = math.floor(posy/CELLSIZE), math.floor(posx/CELLSIZE)

                        movekind, game_map_arr, is_path = selected[0].move(posx, posy, game_map_arr)
                        
                        print(movekind)

                        if movekind > -1:
                            curr_turn = 0
                            name = selected[0].name
                            move_mem.append("BLACK: NAME: {} FROM: [{},{}] TO: [{},{}]".format(name, old_pos[1], old_pos[0], pos[1], pos[0]))

                            # add move_line
                        else:
                            # recenter
                            oldPos = location_to_pos(selected[0].location)
                            movekind, game_map_arr, is_path = selected[0].move(oldPos[1], oldPos[0], game_map_arr)
                    # else not the right turn
                    else:
                        oldPos = location_to_pos(selected[0].location)
                        movekind, game_map_arr, is_path = selected[0].move(oldPos[1], oldPos[0], game_map_arr)

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

        draw_board(screen)

        if is_path:
            draw_path(screen, path, curr)

        draw_font(screen)
        blackpieces.draw(screen)
        whitepieces.draw(screen)
        pygame.display.flip()
