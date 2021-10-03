from enum import Enum


class TicTacToeDirection(Enum):
    COLUMN = 0
    ROW = 1
    DIAG = 2
    RDIAG = 3


# 19.2 (pg. 266)
class TicTacToeBoard(object):
    def __init__(self):
        self.state = [[None, None, None],
                      [None, None, None],
                      [None, None, None]]
        self._winner = None

    def __getitem__(self, item):
        return self.state[item]

    def set(self, i, j, value):
        if self.state[i][j] != value and self._winner is not None:
            self._winner = None  # invalidate winner if change made to board
        self.state[i][j] = value

    def check_direction(self, direction=None):
        if direction == TicTacToeDirection.COLUMN:
            for i in range(3):
                piece = self[0][i]
                if piece is None:
                    return None
                if all([piece == self[x][i] for x in range(1, 3)]):
                    return piece
            return None
        elif direction == TicTacToeDirection.ROW:
            for i in range(3):
                piece = self[i][0]
                if piece is None:
                    return None
                if all([piece == self[i][x] for x in range(1, 3)]):
                    return piece
            return None
        elif direction == TicTacToeDirection.DIAG:
            piece = self[0][0]
            if piece is None:
                return None
            for i in range(1, 3):
                if self[i][i] != piece:
                    return None
            return piece
        elif direction == TicTacToeDirection.RDIAG:
            piece = self[0][2]
            if piece is None:
                return None
            for i in range(1, 3):
                if self[i][2-i] != piece:
                    return None
            return piece
        return None

    @property
    def winner(self):
        if self._winner is not None:
            return self._winner
        for direction in TicTacToeDirection:
            check = self.check_direction(direction)
            if check is not None:
                self._winner = check
                return check
        return None

    def is_win_state(self) -> bool:
        return self.winner is not None

    def __str__(self) -> str:
        return '\n'.join([str(row) for row in self])


if __name__ == '__main__':
    board = TicTacToeBoard()
    board.set(0, 0, 'o')
    board.set(1, 1, 'x')
    board.set(2, 2, 'o')
    board.set(0, 1, 'x')
    board.set(0, 2, 'o')
    board.set(2, 1, 'x')
    print(board)
    print('win:', board.is_win_state())
    print('winner:', board.winner)
