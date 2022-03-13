from environment import *

def main():
    board = board_arr_maker(0, ['ki', 'Ki', 'qu', 'Qu', 'ro', 'Ro', 'kn', 'Kn', 'bi', 'Bi'])
    screen = initialize()
    drawBoard(screen)
    drawPieces(screen, board)
    gameLoop(screen, board)

if __name__ == "__main__":
    main()
