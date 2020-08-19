from chessmen import *
from boardmaker import init as boardinit
## loading images
# Black
b_bishop = pygame.image.load(B_BISHOP)
b_king = pygame.image.load(B_KING)
b_knight = pygame.image.load(B_KNIGHT)
b_pawn = pygame.image.load(B_PAWN)
b_queen = pygame.image.load(B_QUEEN)
b_rook = pygame.image.load(B_ROOK)

# White
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

    # # TODO to add text inside the game on the sides
    # pygame.font.init()
    # myfont = pygame.font.SysFont('Comic Sans Ms', 30)
    # textSurface = myfont.render("Something", False, BLACK)
    # board.blit(textSurface,(0,0))
    return board


def drawPieces(screen):  # 3
    maparr = readGame()
    letterHolder = ""
    for i, line in enumerate(maparr):
        for j, tile in enumerate(line):
            if(tile.split("-")[1].lower() == "bi"):
                if(tile.split("-")[1].strip()[0].islower()):
                    whitepieces.add(
                        Bishop(tile.split("-")[1], (j)*CELLSIZE, (i)*CELLSIZE))
                else:
                    blackpieces.add(
                        Bishop(tile.split("-")[1], (j)*CELLSIZE, (i)*CELLSIZE))
            elif(tile.split("-")[1].lower() == "ki"):
                if(tile.split("-")[1].strip()[0].islower()):
                    whitepieces.add(
                        King(tile.split("-")[1], (j)*CELLSIZE, (i)*CELLSIZE))
                else:
                    blackpieces.add(
                        King(tile.split("-")[1], (j)*CELLSIZE, (i)*CELLSIZE))
            elif(tile.split("-")[1].lower() == "kn"):
                if(tile.split("-")[1].strip()[0].islower()):
                    whitepieces.add(
                        Knight(tile.split("-")[1], (j)*CELLSIZE, (i)*CELLSIZE))
                else:
                    blackpieces.add(
                        Knight(tile.split("-")[1], (j)*CELLSIZE, (i)*CELLSIZE))
            elif(tile.split("-")[1].lower() == "pa"):
                if(tile.split("-")[1].strip()[0].islower()):
                    whitepieces.add(
                        Pawn(tile.split("-")[1], (j)*CELLSIZE, (i)*CELLSIZE))
                else:
                    blackpieces.add(
                        Pawn(tile.split("-")[1], (j)*CELLSIZE, (i)*CELLSIZE))
            elif(tile.split("-")[1].lower() == "qu"):
                if(tile.split("-")[1].strip()[0].islower()):
                    whitepieces.add(
                        Queen(tile.split("-")[1], (j)*CELLSIZE, (i)*CELLSIZE))
                else:
                    print("here")
                    blackpieces.add(
                        Queen(tile.split("-")[1], (j)*CELLSIZE, (i)*CELLSIZE))
            elif(tile.split("-")[1].lower() == "ro"):
                if(tile.split("-")[1].strip()[0].islower()):
                    whitepieces.add(
                        Rook(tile.split("-")[1], (j)*CELLSIZE, (i)*CELLSIZE))
                else:
                    blackpieces.add(
                        Rook(tile.split("-")[1], (j)*CELLSIZE, (i)*CELLSIZE))
    boardpieces.add(whitepieces)
    boardpieces.add(blackpieces)
    print(whitepieces)
    print(blackpieces)


def gameLoop(screen):
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
                    movekind = selected[0].move(posx, posy)
                    if movekind == 1:
                        collision_list = pygame.sprite.spritecollide(
                            selected[0], blackpieces, True)
                    selected = []

                drag_id = 0
        for chesspiece in boardpieces:
            if chesspiece.clicked == True:
                selected = [chesspiece]
            if selected:
                selected[0].rect.x = (math.floor(posx)) - 25
                selected[0].rect.y = (math.floor(posy)) - 25
        board = drawBoard()
        screen.blit(board, board.get_rect())
        blackpieces.draw(screen)
        whitepieces.draw(screen)
        pygame.display.flip()


def main():
    boardinit()
    screen = initialize()
    board = drawBoard()
    screen.blit(board, board.get_rect())
    drawPieces(screen)
    gameLoop(screen)


if __name__ == "__main__":
    main()
