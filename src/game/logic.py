import pygame, os, json
import numpy as np

config_path = os.path.join(os.path.dirname(__file__), "config.json")

with open(config_path, "r") as file:
    config = json.load(file)


class Logic:
    def __init__(self):
        self.board = np.array(config["logic"]["Board"])
        self.turn: str = "X"
        self.winner: str
        self.movesPlayed: int

    def CheckMove(self, position: tuple):
        """
        CHeck if a move can be made or if the square is occupied

        Args:
            position (tuple): the postition of the square to be checked

        Returns:
            bool: is allowed = True, not allowed = False
        """
        if self.board[position[0]][position[1]] == "":
            return True
        else:
            return False

    def CheckWin(self):
        """
        check if a player has won the game

        Returns:
            str: string of the player who won
        """
        #rows
        for row in self.board:
            if row[0] == row[1] == row[2]  == "X":
                return "player1"
            elif row[0] == row[1] == row[2]  == "O":
                return "player2"
        
        #columns
        for column in range(3):
            if self.board[0, column] == self.board[1, column] == self.board[2, column] == "X":
                return "player1"
            elif self.board[0, column] == self.board[1, column] == self.board[2, column] == "O":
                return "player2"
        
        #diagonals
        d1 = [self.board[0,0],self.board[1,1], self.board[2,2]]
        d2 = [self.board[0,2],self.board[1,1], self.board[2,0]]
        
        if all(x == "X" for x in d1) or all(x == "X" for x in d2):
            return "player1"
        elif all(x == "O" for x in d1) or all(x == "O" for x in d2):
            return "player2"
        
    
    def NextTurn(self):
        """
        function to keep track of how many moves where played.
        """
        self.movesPlayed += 1
        
        if self.turn == "X":
            self.turn = "O"
        elif self.turn == "O":
            self.turn = "X"
        
    def CheckGameOver(self):
        """
        check if the game has ended because there are no more moves to play

        Returns:
            bool: is game over or not
        """
        if self.movesPlayed >= 9:
            return True
        else:
            return False
        
    def Move(self, position: tuple):
        """
        set an X or O on the board depending on whos turn it is 

        Args:
            position (tuple): which square to make the move on
        """
        self.board[position] = self.turn

    def ResetBoard(self):
        """
        resets board to starting state
        """
        self.board = np.array(config["logic"]["Board"])
