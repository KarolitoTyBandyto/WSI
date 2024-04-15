import numpy as np
from copy import deepcopy


class TicTacToe:
    def __init__(self):
        self.board = np.zeros((3,3))
        self.turn = 1
        self.winner = 0
        self.done = False
        self.moves = 0
        self.last_move = None

    def reset(self):
        self.board = np.zeros((3,3))
        self.turn = 1
        self.winner = 0
        self.done = False
        self.moves = 0

    def step(self, action: tuple):
        self.last_move = action
        if self.done:
            return self.board, self.winner, self.done

        if self.board[action[0], action[1]] == 0:
            self.board[action[0], action[1]] = self.turn
            self.moves += 1
            if self.check_winner():
                self.winner = self.turn
                self.done = True
            elif self.moves == 9:
                self.done = True
            self.turn = -self.turn

        return self.board, self.winner, self.done

    def check_winner(self):
        for i in range(3):
            if self.board[i,0] == self.board[i,1] == self.board[i,2] != 0:
                return True
            if self.board[0,i] == self.board[1,i] == self.board[2,i] != 0:
                return True
        if self.board[0,0] == self.board[1,1] == self.board[2,2] != 0:
            return True
        if self.board[0,2] == self.board[1,1] == self.board[2,0] != 0:
            return True
        return False

    def print_board(self):
        for i in range(3):
            for j in range(3):
                if self.board[i,j] == 1:
                    print('X', end=' ')
                elif self.board[i,j] == -1:
                    print('O', end=' ')
                else:
                    print('.', end=' ')
            print()
        print()

    def copy(self):
        return deepcopy(self)
    
    def undo_last_move(self):
        action = self.last_move
        self.board[action[0], action[1]] = 0
        self.turn = -self.turn
        self.moves -= 1

    def get_valid_moves(self):
        return np.argwhere(self.board == 0)

    def get_state(self):
        return self.board

    def get_winner(self):
        return self.winner

    def get_turn(self):
        return self.turn

    def get_done(self):
        return self.done

    def get_moves(self):
        return self.moves

def main():
    game = TicTacToe()
    game.print_board()
    game.step((0,0))
    game.print_board()
    game.step((1,1))
    game.print_board()
    game.step((0,1))
    game.print_board()
    game.step((1,0))
    game.print_board()


if __name__ == '__main__':
    main()