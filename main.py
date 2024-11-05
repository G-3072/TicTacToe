import pygame
import sys
from game import  MULTI_PLAYER_RECT, SINGLE_PLAYER_RECT, QUIT_RECT, REMATCH_RECT, BACK_RECT
from game import Game, Display, PlayerInput

# Initialize Pygame
pygame.init()

# Create instances of your classes
display = Display()
gameLogic = Game()
userInput = PlayerInput()

# Game state variables
running = True
state = "start"
previousState = None

while running:
    pygame.display.flip()  # Update display
    events = pygame.event.get()  # Get pygame events

    if state == "start":
        display.StartScreen()

        if userInput.ButtonCheck(MULTI_PLAYER_RECT, events):
            state = "multiplayer"
            gameLogic.Reset()  # Reset game logic for a new game

        if userInput.ButtonCheck(SINGLE_PLAYER_RECT, events):
            state = "singleplayer"
            gameLogic.Reset()  # Reset game logic for a new game

        if userInput.ButtonCheck(QUIT_RECT, events):
            pygame.quit()
            sys.exit()

    elif state == "singleplayer":

        gameInput = userInput.GameInput(events)

        

    elif state == "multiplayer":
        

        gameInput = userInput.GameInput(events)

        if gameInput is not None and gameLogic.isMoveAllowed(gameInput):
            gameLogic.makeMove(gameInput)

        if gameLogic.checkWinner() is not None:
            state = "end"
            previousState = "multiplayer"
        elif gameLogic.isDraw():
            state = "end"
            previousState = "multiplayer"
        display.DrawBoard(gameLogic.board)

    elif state == "end":
        winner = gameLogic.checkWinner()
        
        if winner is not None:
            display.EndScreen(winner)
        else:
            display.EndScreen("draw")

        if userInput.ButtonCheck(REMATCH_RECT, events):
            gameLogic.Reset()
            display.ClearScreen()
            state = previousState

        if userInput.ButtonCheck(BACK_RECT, events):
            gameLogic.Reset()
            state = "start"

        if userInput.ButtonCheck(QUIT_RECT, events):
            pygame.quit()
            sys.exit()

    for event in events:  
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
