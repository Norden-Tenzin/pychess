from environment import *
from image_resizer import cut_and_resize_image
def main():
    # board_arr_maker
    # args: play_as and an optional arg on which pieces to show. 

    # play_as as 0 - white, 1 - black
    play_as = 1
    # board = board_arr_maker(play_as, ['ki', 'Ki', 'qu', 'Qu', 'ro', 'Ro', 'kn', 'Kn', 'bi', 'Bi'])
    # board = board_arr_maker(0, ['ki', 'Ki', 'qu', 'Qu', 'bi', 'Bi'])
    # cut_and_resize_image()
    board = board_arr_maker(play_as)
    print(np.matrix(board))
    screen = initialize()
    draw_board(screen)
    draw_pieces(screen, board, play_as)
    game_loop(screen, board, play_as)

if __name__ == "__main__":
    main()
