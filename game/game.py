import numpy as np
from .board import Board


class Game:
    def __init__(self):
        self.board = Board()
        self.winner: str
        self.turn: str
        self.movesPlayed: int

    def makeMove(self, position: tuple):
        """
        Sets symbol in comuter representation of the playing board.
        uses turn as symbol.\n
        does not check if move is allowed.\n

        Args:
            position (tuple): position of the square where the move should be made
        """

        self.board[position] = self.turn

        if self.turn == "X":
            self.turn = "O"
        elif self.turn == "O":
            self.turn = "X"
        self.movesPlayed += 1

    def isDraw(self):
        """
        checks if teh game has resultet in a draw

        Returns:
            bool: True -> Draw.\n
            False -> no draw
        """
        if self.movesPlayed >= 9 and self.checkWinner() is None:
            return True

        return False

    def checkWinner(self):
        """
        checks if someone won the game and returns winner

        Returns:
            winnter (str): player1 means X won.\n
            player2 means O won. \n
            None means no winner
        """
        for row in self.board:
            if row[0] == row[1] == row[2] != ".":
                return row[0]

        for col in range(3):
            if self.board[0, col] == self.board[1, col] == self.board[2, col] != ".":
                return self.board[0, col]

        if self.board[0, 0] == self.board[1, 1] == self.board[2, 2] != ".":
            return self.board[0, 0]

        if self.board[0, 2] == self.board[1, 1] == self.board[2, 0] != ".":
            return self.board[0, 2]

    def isMoveAllowed(self, position: tuple):
        """
        checks if a position is empty -> if move is allowed.

        Args:
            position (tuple): position to check if empty

        Returns:
            (bool): True -> move is allowed. False -> Move not allowed
        """
        if self.board[position] == ".":
            return True
        else:
            return False

    def Reset(self):
        """
        Reset game for a rematch
        """
        self.board.clear()
        self.movesPlayed = 0
        self.turn = "X"
        
