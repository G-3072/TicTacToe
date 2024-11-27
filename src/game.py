import numpy as np
import pygame
from .board import Board
from .display import Display
from .config import *
from .player import Human
from .bot import Bot


class Game:
    def __init__(self):
        self.board = Board()    #computer representation of the board 
        self.movesPlayed: int = 0   #counter of how many moves have been played
        self.state: int = gameState.START   #state of the state machine
        self.display: Display   # display object to handle all graphics
        self.player1: Human     
        self.player2: object
        self.currentPlayer: object  #which player is currently playing
        
        
    def setup(self):
        pygame.init()
        self.display = Display()
        self.player1 = Human("X")
        self.currentPlayer = self.player1

    def play(self):
        
        self.setup()
        running = True
        
        while running:
            pygame.display.flip()  # Update display
            events = pygame.event.get()  # Get pygame events
            match self.state:
                case gameState.START:
                    
                    self.display.StartScreen()
                    if self.player1.CheckButtonClick(MULTI_PLAYER_RECT, events):
                        self.player2 = Human("O")
                        self.state = gameState.PLAYING
                    if self.player1.CheckButtonClick(SINGLE_PLAYER_RECT, events):
                        self.player2 = Bot("O")
                        self.state = gameState.PLAYING
                    if self.player1.CheckButtonClick(QUIT_RECT, events):
                        pygame.quit()
                        return
                    
                case gameState.PLAYING:
                    
                    if self._checkWinner() is not None or self._isDraw():
                        self.state = gameState.END
                    move = self.currentPlayer.getMove(events=events, board= self.board)
                    if move is not None:
                        self._makeMove(move)
                    self.display.DrawBoard(self.board)
                    
                case gameState.END:
                    
                    winner = self._checkWinner()
                    self.display.EndScreen(winner)
                    if self.player1.CheckButtonClick(REMATCH_RECT, events):
                        self._reset()
                        self.display.ClearScreen()
                        self.state = gameState.PLAYING
                    if self.player1.CheckButtonClick(BACK_RECT, events):
                        self._reset()
                        self.state = gameState.START
                    if self.player1.CheckButtonClick(QUIT_RECT, events):
                        pygame.quit()
                        return
                
            for event in events:  
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

    def _makeMove(self, move: tuple):
        """
        Sets symbol in comuter representation of the playing board.
        uses turn as symbol.\n
        does not check if move is allowed.\n

        Args:
            move (tuple): position of the square where the move should be made
        """
        
        if self.board._isMoveAllowed(move[0], move[1]):
            self.board.setSquare(move[0], move[1], self.currentPlayer.getSymbol())
            
            if self.currentPlayer is self.player1:
                self.currentPlayer = self.player2
                
            elif self.currentPlayer is self.player2:
                self.currentPlayer = self.player1
                
            self.movesPlayed += 1
        

    def _isDraw(self):
        """
        checks if teh game has resultet in a draw

        Returns:
            bool: True -> Draw.\n
            False -> no draw
        """
        if self.movesPlayed >= 9 and self._checkWinner() is None:
            return True

        return False

    def _checkWinner(self):
        """
        checks if someone won the game and returns winner

        Returns:
            winnter (str): player1 means X won.\n
            player2 means O won. \n
            None means no winner
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

    def _reset(self):
        """
        Reset game for a rematch
        """
        self.board.clear()
        self.movesPlayed = 0
        self.currentPlayer = self.player1
        
