import numpy as np
from src.utils import *


class QLearner:

    def __init__(self):
        self.table = {}

    def add_to_table(self, board, move, update):
        """Updates the Q-table board values"""
        board = str(board)

        if board not in self.table:
            # self.table[board] = np.random.rand(9)
            self.table[board] = np.array([0.0] * 9)

        self.table[board][move] += update
