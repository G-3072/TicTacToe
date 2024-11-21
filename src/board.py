import numpy as np
import copy


class Board:
    def __init__(self):
        self._board = np.full((3, 3), fill_value=".", dtype=str)

    def __getitem__(self, index):
        if isinstance(index, int):
            return self._board[index, :]
        else:
            row, col = index
            return self._board[row, col]

    def __setitem__(self, index, value):
        if isinstance(index, int):
            self._board[index, :] = value
        else:
            row, col = index
            self._board[row, col] = value

    def __str__(self):

        return "\n".join([" ".join(map(str, row)) for row in self._board]) + "\n"

    def __iter__(self):
        for row in self._board:
            yield row

    def clear(self):
        """
        resets board to starting state
        """
        self._board = np.full((3, 3), fill_value=".")

    def copy(self):
        """
        returns a copy of the object

        Returns:
            Board: copy of current object
        """
        return copy.deepcopy(self)
