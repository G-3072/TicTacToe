from game.display import Display
from game.logic import Logic
from game.input import Input

import pygame, sys, os, json
import numpy as np

#------------------------------ Loading config file ------------------------------
config_path = os.path.join(os.path.dirname(__file__), "config.json")

with open(config_path, "r") as file:
    config = json.load(file)

#------------------------------ creating class instances ------------------------------
display = Display()
inputs = Input()
game = Logic()


#------------------------------ initializing variables ------------------------------
running = True
state = "start"

display.LoadTextures()


#------------------------------ game Loop ------------------------------
while running:
    pygame.display.flip()   #update display
    
    if state == "start":
        
        display.StartScreen()
        
        
    elif state == "singleplayer":
        display.DrawBoard()
        
    elif state == "multiplayer":
        display.DrawBoard()
        
    elif state == "end":
        display.EndScreen()
        
    for event in pygame.event.get():    #check if window was closed
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()