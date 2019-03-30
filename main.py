from src.Game import Game
from src.Player import *
from src.utils import *
from src.QLearner import QLearner
from pprint import pprint


def move_sequence(player, game, qlearner):
    move = player.random_move(game.board)
    update = game.get_update()
    qlearner.add_to_table(game.board, move, update)
    game.turn(move, player.tile)
    game.print_board()

def main():
    game = Game()
    player_one = RandomPlayer(tile="X")
    player_two = RandomPlayer(tile="O")
    ql = QLearner()

    for epoch in range(100):
        while True:
            if not game.is_over():
                move_sequence(player_one, game, ql)
            else:
                break

            if not game.is_over():
                move_sequence(player_two, game, ql)
            else:
                break

        game.reset_board()

        if epoch % 100 == 99:
            pprint(ql.table["[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']"])


if __name__ == '__main__':
    main()
