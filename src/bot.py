import numpy as np

from .board import Board
from .player import Player

# to get the best moves to play the bot uses a minimax algorithm. algorithm from theese websites:
# https://www.youtube.com/watch?v=5y2a0Zhgq0U
# https://www.neverstopbuilding.com/blog/minimax
# https://www.youtube.com/watch?v=l-hh51ncgDI&t=197s    in this video only 0:00 - 6:20

class Tree:
    def __init__(self, board: Board, maximizer: object, minimizer: object, currentPlayer: object):
        self.evaluatedMoves = dict()    # dictionariy containing all possible moves linked to their score
        self.board: Board = board   # representation of the tictactoe board for the algoorithm to work with
        self.maximizer: object = maximizer  #player trying to maximize the score (bot)
        self.minimizer: object = minimizer  #player trying to minimize the score (human)
        self.currentPlayer: object = currentPlayer  #refrence to player object which's turn it is to play
        
    def _nextTurn(self):
        """
        update currentPlayer for next move
        """
        if self.currentPlayer is self.maximizer:
            self.currentPlayer = self.minimizer
        elif self.currentPlayer is self.minimizer:
            self.currentPlayer = self.maximizer

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
        check if someone won the game and return the Symbol of the winner

        Returns:
            winner (str): rturns winner as X or O 
        """
        #check rows of board for win
        for i, _ in enumerate(self.board):
            if self.board.checkSquare(i, 0) == self.board.checkSquare(i, 1) == self.board.checkSquare(i, 2) != ".":
                return self.board.checkSquare(i, 0)
        #check columns of board for wins
        for col, _ in enumerate(self.board):
            if self.board.checkSquare(0, col) == self.board.checkSquare(1, col) == self.board.checkSquare(2, col) != ".":
                return self.board.checkSquare(0, col)
        #check left to right diagonal of board for win
        if self.board.checkSquare(0, 0) == self.board.checkSquare(1, 1) == self.board.checkSquare(2, 2) != ".":
            return self.board.checkSquare(0, 0)
        #check right to eft diagonal of board for win
        if self.board.checkSquare(0, 2) == self.board.checkSquare(1, 1) == self.board.checkSquare(2, 0) != ".":
            return self.board.checkSquare(1, 1)

    def getBestMove(self):
        """
        selects the best move the bot can play and returns it

        Returns:
            move (tuple): tuple of the best move 
        """
        moves = self._getMoves()
        if moves.__len__() == 0:    #dont do anything if game is over
            return None
        
        branches = np.empty(moves.__len__(), dtype=object)
        
        for i, move in enumerate(moves):

            newBoard = self.board.copy()
            newBoard.setSquare(move[0], move[1], self.currentPlayer.getSymbol())
            branches[i] = Branch(newBoard, self.maximizer, self.minimizer, self.currentPlayer)

            self.evaluatedMoves[int(branches[i].getScore())] = (
                int(move[0]),
                int(move[1]),
            )

        if self.evaluatedMoves.get(1) is not None:
            return self.evaluatedMoves.get(1)
        elif self.evaluatedMoves.get(0) is not None:
            return self.evaluatedMoves.get(0)
        else:
            return self.evaluatedMoves.get(-1)


class Branch(Tree):

    def __init__(self, board: Board, maximizer: object, minimizer:object, currentPlayer: object):
        self.score: int     #score of current branch (1, 0, -1)
        self.board: Board = board   #computer representation of current board
        self.branches: np.ndarray   #list of all branches. each branch is for posiible move from current branch
        
        self.currentPlayer: object = currentPlayer  # reference to player which's turn it is to play
        self.maximizer: object = maximizer  #player trying to maximise the score (bot)
        self.minimizer: object = minimizer  #player trying to minimize the score (human)

    def _getBranches(self):

        """
        creates array containing branches for every possible move
        """

        moves = self._getMoves()
        self.branches = np.empty(moves.__len__(), dtype=object)

        for i, move in enumerate(moves):
            newBoard = self.board.copy()
            newBoard.setSquare(move[0], move[1], self.currentPlayer.getSymbol())
            self.branches[i] = Branch(board=newBoard, maximizer=self.maximizer, minimizer=self.minimizer, currentPlayer=self.currentPlayer)

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
            elif winner == self.maximizer.getSymbol():
                # win
                self.score = 1
            elif winner == self.minimizer.getSymbol():
                # lose
                self.score = -1
        else:
            self._nextTurn()
            self._getBranches()
            scores = np.zeros(self.branches.__len__(), dtype=int)

            for i, branch in enumerate(self.branches):
                scores[i] = branch.getScore()

            if self.currentPlayer is self.maximizer:
                self.score = max(scores)
            elif self.currentPlayer is self.minimizer:
                self.score = min(scores)

        return self.score
    
class Bot(Player):
    def __init__(self, symbol: str, player1: object):
        self._symbol = symbol
        self.maximizer = self
        self.minimizer = player1
        
    def getSymbol(self):
        return self._symbol
    
    def getMove(self, board: Board = None):
        minimax = Tree(board = board, maximizer = self.maximizer, minimizer = self.minimizer, currentPlayer = self)
        return minimax.getBestMove()