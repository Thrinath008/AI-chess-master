from typing import List

BOARD_SIZE = 8
NUM_SQUARES = 64

SQUARE_MASKS = [1 << sq for sq in range(NUM_SQUARES)]

def square_index(rank: int, file: int)-> int:       #for eg mawa sindex(2,2) = 2X8+2 = 18
    return rank * BOARD_SIZE + file


def index_to_rank(index: int)-> int :
    return divmod(index, BOARD_SIZE)