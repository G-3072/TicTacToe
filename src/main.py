from game.display import Display
from game.logic import Logic
from game.input import Input

import pygame, sys, numpy as np

display = Display()

running = True
state = "start"

display.LoadTextures()

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