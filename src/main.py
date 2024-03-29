from environment import *

def main():
    # board_arr_maker
    # args: play_as and an optional arg on which pieces to show. 

    # play_as as 0 - white, 1 - black
    playAs = 0
    # board = board_arr_maker(0, ['ki', 'Ki', 'qu', 'Qu', 'ro', 'Ro', 'kn', 'Kn', 'bi', 'Bi'])
    # board = board_arr_maker(0, ['ki', 'Ki', 'qu', 'Qu', 'bi', 'Bi'])

    board = board_arr_maker(playAs)
    screen = initialize()
    draw_board(screen)
    draw_pieces(screen, board)
    game_loop(screen, board, playAs)

if __name__ == "__main__":
    main()
