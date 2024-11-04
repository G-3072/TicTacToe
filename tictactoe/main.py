from game.display import Display
from game.logic import Logic
from game.userInput import UserInput

import pygame, sys, os, json
import numpy as np

#------------------------------ Loading config file ------------------------------
config_path = os.path.join(os.path.dirname(__file__), "config.json")

with open(config_path, "r") as file:
    config = json.load(file)

#------------------------------ creating class instances ------------------------------
display = Display()
userInput = UserInput()
game = Logic()


#------------------------------ initializing variables ------------------------------
running = True
state = "start"
previousState = ""

display.LoadTextures()


#------------------------------ game Loop ------------------------------
while running:
    pygame.display.flip()   #update display
    events = pygame.event.get() #get pygame events
    
    
    if state == "start":
        
        display.StartScreen()
        
        if userInput.ButtonCheck(config["input"]["MultiPlayerRect"], events):
            state = "multiplayer"
            
        if userInput.ButtonCheck(config["input"]["SinglePlayerRect"], events):
            state = "singleplayer"
            
        if userInput.ButtonCheck(config["input"]["QuitRect"], events):
            pygame.quit()
            sys.exit()
        
        
    elif state == "singleplayer":
        display.DrawBoard()
        
    elif state == "multiplayer":
        
        gameInput = userInput.GameInput(events)
        
        if gameInput is not None:
            if game.isMoveAllowed(gameInput) == True:
                game.Move(gameInput)
                game.NextTurn()
        
        if game.isGameOver() == True:
            state = "end"
            previousState= "multiplayer"
        
        if game.CheckWin() is not None:
            state = "end"
            previousState= "multiplayer"
            
        display.DrawBoard(game.board)
            
            
        
        
    elif state == "end":
        winner = game.CheckWin()
        
        if winner is not None:
            display.EndScreen(winner)
        else:
            display.EndScreen("Draw")
            
        if userInput.ButtonCheck(config["input"]["RematchRect"], events):
            game.Reset()
            display.ClearScreen()
            state = previousState
        
        if userInput.ButtonCheck(config["input"]["BackRect"], events):
            game.Reset()
            state = "start"
            
        if userInput.ButtonCheck(config["input"]["QuitRect"], events):
            pygame.quit()
            sys.exit()
            
            
    for event in events:    #check if window was closed
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()