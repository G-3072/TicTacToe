from game.display import display
from game.logic import *
from game.player import *

import pygame, sys

disp = display()

disp.LoadTextures()
disp.StartScreen()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


