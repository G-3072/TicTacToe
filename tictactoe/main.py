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
        display.DrawBoard()
        gameInput = userInput.GameInput(events)
        
        if gameInput is not None:
            game.Move(gameInput)
            game.NextTurn()
            
        
        
    elif state == "end":
        display.EndScreen()
        
    for event in events:    #check if window was closed
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()