import numpy as np

from .board import Board
from ._player import Player


class Tree:
    def __init__(self, board: Board, maximizer: str):
        self.evaluatedMoves = dict()
        self.board: Board = board
        self.maximizer: str = maximizer

    def _getTurn(self):
        """
        get which players turn it is

        Returns:
            (str): X or O
        """
        xcnt = ocnt = 0

        for i, row in enumerate(self.board):
            for j, square in enumerate(row):
                if square == "X":
                    xcnt += 1
                elif square == "O":
                    ocnt += 1

        if xcnt > ocnt:
            return "O"
        else:
            return "X"

    def _getMoves(self):
        """
        retruns array of all possible moves on board

        Returns:
            moves (np.NDarray): array containing tuples of all possible moves
        """
        moves = np.empty((1, 2), dtype=np.int8)

        for i, row in enumerate(self.board):
            for j, square in enumerate(row):
                if square == ".":
                    moves = np.append(moves, [[i, j]], axis=0)

        moves = np.delete(moves, 0, 0)
        return moves

    def _getWinner(self):
        """
        check if someone won the game and return the winner

        Returns:
            winner (str): rturns winner as X or O 
        """
        for i, _ in enumerate(self.board):
            if self.board.checkSquare(i, 0) == self.board.checkSquare(i, 1) == self.board.checkSquare(i, 2) != ".":
                return self.board.checkSquare(i, 0)

        for col in range(3):
            if self.board.checkSquare(0, col) == self.board.checkSquare(1, col) == self.board.checkSquare(2, col) != ".":
                return self.board.checkSquare(0, col)

        if self.board.checkSquare(0, 0) == self.board.checkSquare(1, 1) == self.board.checkSquare(2, 2) != ".":
            return self.board.checkSquare(0, 0)

        if self.board.checkSquare(0, 2) == self.board.checkSquare(1, 1) == self.board.checkSquare(2, 0) != ".":
            return self.board.checkSquare(1, 1)

    def getBestMove(self):
        """
        selects the best move the bot can play and returns it

        Returns:
            move (tuple): tuple of the best move 
        """
        turn = self._getTurn()
        moves = self._getMoves()
        branches = np.empty(moves.__len__(), dtype=object)
        
        if moves.__len__() == 0:
            return None

        for i, move in enumerate(moves):

            newBoard = self.board.copy()
            newBoard.setSquare(move[0], move[1], turn)
            branches[i] = Branch(newBoard, self.maximizer)

            self.evaluatedMoves[int(branches[i].getScore())] = (
                int(move[0]),
                int(move[1]),
            )

        # for i, val in enumerate(self.evaluatedMoves.values()):
        try:
            return self.evaluatedMoves[1]
        except KeyError:
            try:
                return self.evaluatedMoves[0]
            except KeyError:
                return self.evaluatedMoves[-1]


class Branch(Tree):

    def __init__(self, board: Board, maximizer: str):
        self.score: int     #score of current branch (1, 0, -1)
        self.board: Board = board   #computer representation of current board
        self.branches: np.ndarray   #list of all branches. each branch is for posiible move from current branch
        self.maximizer: str = maximizer # mplayer trying to maximize the branch score
        self.minimizer: str = "O" if maximizer == "X" else "X"  #player trying to minimize the score
        self.turn: str = self._getTurn()    #current turn
        self.evaluatedMoves = dict()    #dictionary linking possible moves to score for players to select
        

    def _getBranches(self):

        """
        creates array containing brances for every possible move
        """

        moves = self._getMoves()
        self.branches = np.empty(moves.__len__(), dtype=object)

        for i, move in enumerate(moves):
            newBoard = self.board.copy()
            newBoard.setSquare(move[0], move[1], self.turn)
            self.branches[i] = Branch(newBoard, self.maximizer)

    def getScore(self):
        """
        simulates all future boards and gets a best score for branch

        Returns:
            score (int): score of the branch
        """
        winner = self._getWinner()
        moves = self._getMoves()

        if moves.__len__() == 0 or winner is not None:
            if winner is None:
                # draw
                self.score = 0
            elif winner == self.maximizer:
                # win
                self.score = 1
            elif winner == self.minimizer:
                # lose
                self.score = -1
        else:
            self._getBranches()
            scores = np.zeros(self.branches.__len__(), dtype=int)

            for i, branch in enumerate(self.branches):
                scores[i] = branch.getScore()

            if self.turn == self.maximizer:
                self.score = max(scores)
            elif self.turn == self.minimizer:
                self.score = min(scores)

        return self.score
    
class Bot(Player):
    def __init__(self, symbol: str):
        self.symbol = symbol
        self.maximizer = "O"
        
    def getSymbol(self):
        return self.symbol
    
    def getMove(self, events: list = None, board: Board = None):
        """
        wrapper function for simple use. get the move the bot should play

        Args:
            board (Board): the current board

        Returns:
            move (tuple): move to play
        """
        minimax = Tree(board, self.maximizer)
        return minimax.getBestMove()