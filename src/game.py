import numpy as np
import pygame
from .board import Board
from .display import Display
from .config import *
from .human import Human
from .bot import Bot


class Game:
    def __init__(self):
        pygame.init()
        self.board = Board()    #computer representation of the board 
        self.movesPlayed: int = 0   #counter of how many moves have been played
        self.state: int = gameState.START   #state of the state machine
        self.previousState: int     #previous game state so rematches go to correct mode
        self.display: Display = Display()   #display object to handle all graphics
        self.player1: Human = Human("X")    #player who plays X. always human for start- and endscreen inputs
        self.player2: object    #player who plays O. human or bot depending on gamemode
        self.currentPlayer: object = self.player1 #which player is currently playing

    def play(self):
        """
        run game
        """

        running = True
        
        while running:
            pygame.display.flip()  # Update display
            events = pygame.event.get()  # Get pygame events
            
            match self.state:
                case gameState.START:
                    self.display.StartScreen()
                    if self.player1.CheckButtonClick(MULTI_PLAYER_RECT, events):
                        self.player2 = Human("O")
                        self.state = gameState.MULTIPLAYER
                    if self.player1.CheckButtonClick(SINGLE_PLAYER_RECT, events):
                        self.player2 = Bot("O", self.player1)
                        self.state = gameState.SINGLEPLAYER
                    if self.player1.CheckButtonClick(QUIT_RECT, events):
                        pygame.quit()
                        running = False
                    
                case gameState.SINGLEPLAYER:
                    if self._checkWinner() is not None or self._isDraw():
                        self.previousState = self.state
                        self.state = gameState.END
                    if self.currentPlayer is self.player1:
                        move = self.currentPlayer.getMove(events=events)
                    elif self.currentPlayer is self.player2:
                        move = self.currentPlayer.getMove(board = self.board)
                    if move is not None:
                        self._makeMove(move)
                    self.display.DrawBoard(self.board)
                
                case gameState.MULTIPLAYER:
                    if self._checkWinner() is not None or self._isDraw():
                        self.previousState = self.state
                        self.state = gameState.END
                    move = self.currentPlayer.getMove(events = events)
                    if move is not None:
                        self._makeMove(move)
                    self.display.DrawBoard(self.board)
                    
                case gameState.END:
                    winner = self._checkWinner()
                    self.display.EndScreen(winner)
                    if self.player1.CheckButtonClick(REMATCH_RECT, events):
                        self._reset()
                        self.display.ClearScreen()
                        self.state = self.previousState
                    if self.player1.CheckButtonClick(BACK_RECT, events):
                        self._reset()
                        self.state = gameState.START
                    if self.player1.CheckButtonClick(QUIT_RECT, events):
                        pygame.quit()
                        running = False
                
            for event in events:  
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False

    def _makeMove(self, move: tuple):
        """
        Sets the symbol of the currentplayer on the board and updates currentPlayer varaible

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
            bool: True -> Draw, False -> no Draw
        """
        if self.movesPlayed >= 9 and self._checkWinner() is None:
            return True

        return False

    def _checkWinner(self):
        """
        checks if someone won the game and returns winner

        Returns:
            winnter (str): symbol of the player that won ( X or O). None if no winner
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
        Reset game to starting state
        """
        self.board.clear()
        self.movesPlayed = 0
        self.currentPlayer = self.player1