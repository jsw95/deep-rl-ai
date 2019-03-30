import numpy as np


def free_squares(board):
    free = [i for i in range(len(board)) if board[i] == 0]

    return free


class Player:

    def __init__(self, tile):
        self.hello = "Hi!"
        self.tile = tile

    @staticmethod
    def random_move(board):
        free = [i[0] for i in enumerate(board) if i[1] == ' ']
        choice = np.random.choice(free)
        return choice


class RandomPlayer(Player):

    def __init__(self, tile):
        self.name = "random"
        super(RandomPlayer, self).__init__(tile)


class AgentPlayer(Player):
    def __init__(self, tile):
        self.name = "random"
        super(AgentPlayer, self).__init__(tile)
