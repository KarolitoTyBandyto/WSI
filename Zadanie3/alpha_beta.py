import numpy as np
from tic_tac_toe import TicTacToe
import random


NODES_PRUNED = 0


def alpha_beta_search(
    state: TicTacToe,
    depth: int,
    alpha: float = -np.inf,
    beta: float = np.inf,
    maximizing_player: bool = True,
) -> tuple[float, int]:
    global NODES_PRUNED

    if depth == 0 or state.get_done():
        return state.get_winner(), None
    moves_list = []
    best_move = None

    if maximizing_player:
        max_eval = -np.inf
        for move in state.get_valid_moves():
            state_copy = state.copy()
            state_copy.step(move)
            eval, _ = alpha_beta_search(state_copy, depth - 1, alpha, beta, False)
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                NODES_PRUNED += 1
                break
        return max_eval, best_move
    else:
        min_eval = np.inf
        for move in state.get_valid_moves():
            state_copy = state.copy()
            state_copy.step(move)
            eval, _ = alpha_beta_search(state_copy, depth - 1, alpha, beta, True)
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                NODES_PRUNED += 1
                break

        return min_eval, best_move

def main():
    game = TicTacToe()
    winners = []
    while not game.get_done():
        if game.get_turn() == 1:
            _, move = alpha_beta_search(game.copy(), 100, maximizing_player=True)
            game.step(move)
        else:
            # game.print_board()
            # print(game.get_valid_moves())
            # move = input(("Enter move:"))
            # move = tuple(map(int, move.split(",")))
            # print(move)
            # game.step(move)
            _, move = alpha_beta_search(game.copy(), 100, maximizing_player=False)
            game.step(move)
        game.print_board()
    print("Winner:", game.get_winner())



if __name__ == "__main__":
    main()
