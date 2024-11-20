import numpy as np

from src import Board

class Tree:
    def __init__(self, board: Board, maximizer: str):
        self.evaluatedMoves = dict()
        self.board: Board = board
        self.maximizer: str = maximizer

    def _getTurn(self):
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
        moves = np.empty((1, 2), dtype=np.int8)

        for i, row in enumerate(self.board):
            for j, square in enumerate(row):
                if square == ".":
                    moves = np.append(moves, [[i, j]], axis=0)

        moves = np.delete(moves, 0, 0)
        return moves

    def _getWinner(self):
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

    def getBestMove(self):

        turn = self._getTurn()
        moves = self._getMoves()
        branches = np.empty(moves.__len__(), dtype=object)
        
        if moves.__len__() == 0:
            return None

        for i, move in enumerate(moves):

            newBoard = self.board.copy()
            newBoard[move[0], move[1]] = turn
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
        self.score: int
        self.board: Board = board
        self.branches: np.ndarray
        self.maximizer: str = maximizer
        self.minimizer: str = "O" if maximizer == "X" else "X"
        self.turn: str = self._getTurn()
        self.evaluatedMoves = dict()

    def _getBranches(self):

        # nextTurn = "X" if self.turn == "O" else "O"

        moves = self._getMoves()
        self.branches = np.empty(moves.__len__(), dtype=object)

        for i, move in enumerate(moves):
            newBoard = self.board.copy()
            newBoard[move[0], move[1]] = self.turn
            self.branches[i] = Branch(newBoard, self.maximizer)

    def getScore(self):
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
    
class Bot:
    def __init__(self):
        self.maximizer = "O"
    
    def getMove(self, board: Board):
        minimax = Tree(board, self.maximizer)
        
        
        return minimax.getBestMove()