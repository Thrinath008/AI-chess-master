
# square_index(rank, file) → Converts (rank, file) into a 0–63 index (chess square ID).
# index_to_rank_file(index) → Converts a 0–63 index back into (rank, file).
# print_bitboard(bitboard) → Shows the bitboard as a chessboard grid (1 = occupied, . = empty).
# set_bit(bitboard, square) → Places a piece by setting the bit at a square to 1.
# clear_bit(bitboard, square) → Removes a piece by setting the bit at a square to 0.
# is_bit_set(bitboard, square) → Checks if a square is occupied in the bitboard.
# get_set_bits(bitboard) → Returns a list of all occupied squares (where bits are 1).
# pop_count(bitboard) → Counts how many pieces (1 bits) are on the bitboard.
# lsb_index(bitboard) → Finds the lowest square (least significant bit) that’s occupied.
# msb_index(bitboard) → Finds the highest square (most significant bit) that’s occupied.
# squares_to_bitboard(squares) → Creates a bitboard from a list of square indices.
# mirror_vertical(bitboard) → Flips the board up-down (White ↔ Black perspective).
# mirror_horizontal(bitboard) → Flips the board left-right (files a↔h swappe


from typing import List

BOARD_SIZE = 8
NUM_SQUARES = 64

SQUARE_MASKS = [1 << sq for sq in range(NUM_SQUARES)]

def square_index(rank: int, file: int)-> int:       #for eg mawa sindex(2,2) = 2X8+2 = 18
    return rank * BOARD_SIZE + file


def index_to_rank(index: int)-> (int, int) :
    return divmod(index, BOARD_SIZE)

def print_bitboard(bitboard: int) -> None:
    print ("Bitboard")
    for rank in reversed(range(BOARD_SIZE)):
        line = ""
        for file in range(BOARD_SIZE):
            idx = square_index(rank, file)
            if (bitboard >> idx) & 1:
                line += "1 "
            else:
                line += ". "
        print(line)
    print()

def set_bit(bitboard : int, square: int)-> int:
    return bitboard | SQUARE_MASKS[square]

def clear_bit(bitboard: int,square : int)->int:
    return bitboard & ~SQUARE_MASKS[square]