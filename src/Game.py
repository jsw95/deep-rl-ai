from src.utils import *


class Game:

    def __init__(self):
        self.name = "Tic Tac Toe"
        self.board = [' '] * 9
        self.board_array = board_to_array(self.board)
        self.search_tree = self.board
        self.winners = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        self.board_log = []

    def is_over(self):
        if self.is_win() or self.is_draw():
            return True
        else:
            return False

    def get_update(self):
        return 1

    def turn(self, loc, player):
        self.board_log.append(self.board)
        self.board[loc] = player

    def is_win(self):
        for win in self.winners:
            if (self.board[win[0]] == self.board[win[1]]
                    and self.board[win[0]] == self.board[win[2]]
                    and self.board[win[0]] != ' '):
                return True

    def is_draw(self):
        if ' ' not in self.board:
            return True

    def reset_board(self):
        self.board = [' '] * 9

    def print_board(self):

        print('\n-------------')
        print('| {} | {} | {} |'.format(self.board[0], self.board[1], self.board[2]))
        print('-------------')
        print('| {} | {} | {} |'.format(self.board[3], self.board[4], self.board[5]))
        print('-------------')
        print('| {} | {} | {} |'.format(self.board[6], self.board[7], self.board[8]))
        print('-------------\n')
