from environment import *
from image_resizer import cut_and_resize_image

def main(play_as):
    # board_arr_maker
    # args:
    # play_as as 0 - white, 1 - black
    # if_connect 0 - no, 1 - yes
    # board = board_arr_maker(play_as, ['ki', 'Ki', 'qu', 'Qu', 'ro', 'Ro', 'kn', 'Kn', 'bi', 'Bi'])
    # board = board_arr_maker(0, ['ki', 'Ki', 'qu', 'Qu', 'bi', 'Bi'])
    # cut_and_resize_image()

    board = board_arr_maker(play_as)
    screen = initialize()
    draw_board(screen)
    draw_pieces(screen, board, play_as)
    game_loop(screen, board, play_as)

if __name__ == "__main__":
    # play_as as 0 - white, 1 - black
    main(0)
