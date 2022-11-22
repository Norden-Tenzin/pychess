from constants import *
from chessmen import *
from game_notation import GameNotation

# # loading images
# # Black pieces 
# b_bishop = pygame.image.load(B_BISHOP)
# b_king = pygame.image.load(B_KING)
# b_knight = pygame.image.load(B_KNIGHT)
# b_pawn = pygame.image.load(B_PAWN)
# b_queen = pygame.image.load(B_QUEEN)
# b_rook = pygame.image.load(B_ROOK)

# # White pieces
# w_bishop = pygame.image.load(W_BISHOP)
# w_king = pygame.image.load(W_KING)
# w_knight = pygame.image.load(W_KNIGHT)
# w_pawn = pygame.image.load(W_PAWN)
# w_queen = pygame.image.load(W_QUEEN)
# w_rook = pygame.image.load(W_ROOK)

# Sprite Groups
whitepieces = pygame.sprite.Group()
blackpieces = pygame.sprite.Group()
boardpieces = pygame.sprite.Group()

def initialize():
    pygame.init()
    screen = pygame.display.set_mode((SIZE, SIZE+20))
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

def draw_show_turn(screen, curr_turn):
    # SEPERATOR
    pygame.draw.rect(screen, DARKER, (0, SIZE, SIZE+20, 2))
    # whites turn
    
    if curr_turn == 0:
        pygame.draw.rect(screen, WHITE, (0, SIZE+2, SIZE+20, 18))
        textSurface = CURRTURN.render("White's Turn", True, BLACK)
        screen.blit(textSurface, (5, SIZE))
    if curr_turn == 1:
        pygame.draw.rect(screen, BLACK, (0, SIZE+2, SIZE+20, 18))
        textSurface = CURRTURN.render("Black's Turn", True, WHITE)
        screen.blit(textSurface, (5, SIZE))
def draw_font(play_as, screen):
    
    numbs = NUMBS.copy()
    alpha = ALPHA[::-1].copy()
    colornumbs = [DARKER, WHITE]
    coloralpha = [WHITE, DARKER]
    

    if play_as == 1:
        for i in range(0, 8):
            textSurface = MYFONT.render(numbs[i], True, colornumbs[i % 2])
            screen.blit(textSurface, (2, CELLSIZE * i))
        for i in range(0, 8):
            textSurface = MYFONT.render(alpha[i], True, coloralpha[i % 2])
            screen.blit(textSurface, ((CELLSIZE * (i+1)) - (CELLSIZE*.25), SIZE - (CELLSIZE*.4)))
    elif play_as == 0:
        for i in range(0, 8):
            textSurface = MYFONT.render(numbs[::-1][i], True, colornumbs[i % 2])
            screen.blit(textSurface, (2, CELLSIZE * i))
        for i in range(0, 8):
            textSurface = MYFONT.render(alpha[::-1][i], True, coloralpha[i % 2])
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
    pygame.draw.rect(screen, ORANGE, (currx*CELLSIZE, curry*CELLSIZE, CELLSIZE, CELLSIZE))

def draw_pieces(screen, board, play_as):
    maparr = board
    letterHolder = ""
    for i, line in enumerate(maparr):
        for j, tile in enumerate(line):
            if(tile.split("-")[1].lower() == "bi"):
                if(tile.split("-")[1].strip()[0].islower()):
                    whitepieces.add(
                        Bishop(play_as, tile.split("-")[1], tile.split("-")[0], (j)*CELLSIZE, (i)*CELLSIZE))
                else:
                    blackpieces.add(
                        Bishop(play_as, tile.split("-")[1], tile.split("-")[0], (j)*CELLSIZE, (i)*CELLSIZE))
            elif(tile.split("-")[1].lower() == "ki"):
                if(tile.split("-")[1].strip()[0].islower()):
                    whitepieces.add(
                        King(play_as, tile.split("-")[1], tile.split("-")[0], (j)*CELLSIZE, (i)*CELLSIZE))
                else:
                    blackpieces.add(
                        King(play_as, tile.split("-")[1], tile.split("-")[0], (j)*CELLSIZE, (i)*CELLSIZE))
            elif(tile.split("-")[1].lower() == "kn"):
                if(tile.split("-")[1].strip()[0].islower()):
                    whitepieces.add(
                        Knight(play_as, tile.split("-")[1], tile.split("-")[0], (j)*CELLSIZE, (i)*CELLSIZE))
                else:
                    blackpieces.add(
                        Knight(play_as, tile.split("-")[1], tile.split("-")[0], (j)*CELLSIZE, (i)*CELLSIZE))
            elif(tile.split("-")[1].lower() == "pa"):
                if(tile.split("-")[1].strip()[0].islower()):
                    whitepieces.add(
                        Pawn(play_as, tile.split("-")[1], tile.split("-")[0], (j)*CELLSIZE, (i)*CELLSIZE))
                else:
                    blackpieces.add(
                        Pawn(play_as, tile.split("-")[1], tile.split("-")[0], (j)*CELLSIZE, (i)*CELLSIZE))
            elif(tile.split("-")[1].lower() == "qu"):
                if(tile.split("-")[1].strip()[0].islower()):
                    whitepieces.add(
                        Queen(play_as, tile.split("-")[1], tile.split("-")[0], (j)*CELLSIZE, (i)*CELLSIZE))
                else:
                    blackpieces.add(
                        Queen(play_as, tile.split("-")[1], tile.split("-")[0], (j)*CELLSIZE, (i)*CELLSIZE))
            elif(tile.split("-")[1].lower() == "ro"):
                if(tile.split("-")[1].strip()[0].islower()):
                    whitepieces.add(
                        Rook(play_as, tile.split("-")[1], tile.split("-")[0], (j)*CELLSIZE, (i)*CELLSIZE))
                else:
                    blackpieces.add(
                        Rook(play_as, tile.split("-")[1], tile.split("-")[0], (j)*CELLSIZE, (i)*CELLSIZE))
    boardpieces.add(whitepieces)
    boardpieces.add(blackpieces)

def write_notation(name, to):
    pass

def move_condition(curr_turn, play_as):
    pass

# TODO seperate the gameloop with rendering the board
def game_loop(screen, maparr, play_as):
    move_mem = []
    game_notation = GameNotation()
    curr_turn = 0

    game_map_arr = maparr
    selected = []
    is_path = False

    while True:
        posx, posy = pygame.mouse.get_pos()
        mouse_posy, mouse_posx = math.floor(posy/CELLSIZE), math.floor(posx/CELLSIZE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print(move_mem)
                    # print game_notation
                    game_notation.print_save()
                    sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for chesspiece in boardpieces:
                        if chesspiece.rect.collidepoint(posx, posy):
                            path = None
                            chesspiece.clicked = True
                            path, curr = chesspiece.clear_paths(mouse_posx, mouse_posy, play_as, maparr)
                            is_path = True

            if event.type == pygame.MOUSEBUTTONUP:
                for chesspiece in boardpieces:
                    chesspiece.clicked = False
                
                # if a chess piece has been selected 
                if selected: 

                    print("CURR TURN: {}".format(curr_turn))
                    move_line = []
                    # if its the white's turn and the selected piece is also white

                    # whites turn
                    # curr = 0
                    # play_as = 0
                    old_posy, old_posx = location_to_pos(play_as, selected[0].location)
                    selected_name = selected[0].name
                    print("MOUSE POS: {}, {}".format(mouse_posx, mouse_posy))
                    if play_as == 0:
                        print("WHITE PLAYS")
                        # white
                        if curr_turn == 0 and selected[0].name.islower():
                            print("WHITE MOVES")
                            movekind, game_map_arr, is_path = selected[0].move(play_as, mouse_posx, mouse_posy, game_map_arr)
                            print("MOVEKIND: {}".format(movekind))
                            print("is_path: {}".format(is_path))
                            if movekind > -1:
                                # successful move, now change turn
                                curr_turn = 1
                                move_mem.append("WHITE: NAME: {} FROM: [{},{}] TO: [{},{}]".format(selected_name, old_posx, old_posy, mouse_posx, mouse_posy))
                                game_notation.write_turn(selected_name, pos_to_location(play_as, (mouse_posx, mouse_posy)))
                            else:
                                # recenter
                                movekind, game_map_arr, is_path = selected[0].move(play_as, old_posx, old_posy, game_map_arr)
                        # black
                        elif curr_turn == 1 and not selected[0].name.islower():
                            print("BLACK MOVES")
                            movekind, game_map_arr, is_path = selected[0].move(play_as, mouse_posx, mouse_posy, game_map_arr)
                            print("MOVEKIND: {}".format(movekind))
                            if movekind > -1:
                                # successful move, now change turn
                                curr_turn = 0
                                move_mem.append("BLACK: NAME: {} FROM: [{},{}] TO: [{},{}]".format(selected_name, old_posx, old_posy, mouse_posx, mouse_posy,))
                                game_notation.write_turn(selected_name, pos_to_location(play_as, (mouse_posx, mouse_posy)))
                            else:
                                # recenter
                                oldPos = location_to_pos(play_as, selected[0].location)
                                movekind, game_map_arr, is_path = selected[0].move(play_as, old_posx, old_posy, game_map_arr)
                        
                        # else not the right turn
                        else:
                            print("MISS MOVE")
                            movekind, game_map_arr, is_path = selected[0].move(play_as, old_posx, old_posy, game_map_arr)
                            print("MOVEKIND: {}".format(movekind))

                    
                    if play_as == 1:
                        print("BLACK PLAYS")
                        # black
                        if curr_turn == 1 and selected[0].name.islower():
                            print("BLACK MOVES")
                            print("MOUSE POS: {}, {}".format(mouse_posx, mouse_posy))
                            movekind, game_map_arr, is_path = selected[0].move(play_as, mouse_posx, mouse_posy, game_map_arr)
                            print("MOVEKIND: {}".format(movekind))

                            if movekind > -1:
                                curr_turn = 0
                                move_mem.append("WHITE: NAME: {} FROM: [{},{}] TO: [{},{}]".format(selected_name, old_posx, old_posy, mouse_posx, mouse_posy,))
                                game_notation.write_turn(selected_name, pos_to_location(play_as, (mouse_posx, mouse_posy)))
                                # get new_location
                                # add move_line
                            else:
                                # recenter
                                movekind, game_map_arr, is_path = selected[0].move(play_as, old_posx, old_posy, game_map_arr)
                        
                        # white
                        elif curr_turn == 0 and not selected[0].name.islower():
                            print("WHITE MOVES")
                            movekind, game_map_arr, is_path = selected[0].move(play_as, mouse_posx, mouse_posy, game_map_arr)
                            print("MOVEKIND: {}".format(movekind))

                            if movekind > -1:
                                curr_turn = 1
                                move_mem.append("BLACK: NAME: {} FROM: [{},{}] TO: [{},{}]".format(selected_name, old_posx, old_posy, mouse_posx, mouse_posy,))
                                game_notation.write_turn(selected_name, pos_to_location(play_as, (mouse_posx, mouse_posy)))
                                # add move_line
                            else:
                                # recenter
                                movekind, game_map_arr, is_path = selected[0].move(play_as, old_posx, old_posy, game_map_arr)
                        
                        # else not the right turn
                        else:
                            print("MISS MOVE")
                            movekind, game_map_arr, is_path = selected[0].move(play_as, old_posx, old_posy, game_map_arr)
                    
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
        draw_show_turn(screen, curr_turn)
        if is_path:
            draw_path(screen, path, curr)

        draw_font(play_as, screen)
        blackpieces.draw(screen)
        whitepieces.draw(screen)
        pygame.display.flip()
