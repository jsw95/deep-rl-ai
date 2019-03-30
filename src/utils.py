import numpy as np


def board_to_array(board):
    """Transforms the 0s and Xs to numpy array of -1, 1, 0"""

    mapper = {
        "X": 1,
        "O": -1,
        " ": 0
    }

    board_array = np.array([mapper[sq] for sq in board])
    return board_array



