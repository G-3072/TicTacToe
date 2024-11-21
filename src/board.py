import numpy as np
import copy


class Board:
    def __init__(self):
        self._board = np.full((3, 3), fill_value=".", dtype=str)

    def __str__(self):

        return "\n".join([" ".join(map(str, row)) for row in self._board]) + "\n"

    def __iter__(self):
        for row in self._board:
            yield row
    
    def _isMoveAllowed(self, x:int, y:int):
        if self._board[x,y] == ".":
            return True
        else:
            return False

    def setSquare(self, x:int, y:int, player: str):
        if self._isMoveAllowed(x,y) == True:
            self._board[x,y] = player
    
    def checkSquare(self, x:int, y:int):
        return self._board[x,y]

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
