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
        self._winner = None  # cache winner to reduce calculations

    def __getitem__(self, item):
        return self.state[item]

    def set(self, i, j, value):
        if self[i][j] != value and self._winner is not None:
            self._winner = None  # invalidate winner if change made to board
        self.state[i][j] = value

    def _check_cols(self):
        for i in range(3):
            p = self[0][i]
            if p is None:
                return None
            if all([p == self[x][i] for x in range(1, 3)]):
                return p
        return None

    def _check_rows(self):
        for i in range(3):
            p = self[i][0]
            if p is None:
                return None
            if all([p == self[i][x] for x in range(1, 3)]):
                return p
        return None

    def _check_diag(self):
        p = self[0][0]
        if p is None:
            return None
        for i in range(1, 3):
            if self[i][i] != p:
                return None
        return p

    def _check_rdiag(self):
        p = self[0][2]
        if p is None:
            return None
        for i in range(1, 3):
            if self[i][2 - i] != p:
                return None
        return p

    def check_direction(self, direction=None):
        # Returns the winning value/player or None if there isn't a winner
        if direction == TicTacToeDirection.COLUMN:
            return self._check_cols()
        elif direction == TicTacToeDirection.ROW:
            return self._check_rows()
        elif direction == TicTacToeDirection.DIAG:
            return self._check_diag()
        elif direction == TicTacToeDirection.RDIAG:
            return self._check_rdiag()
        return ''

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
