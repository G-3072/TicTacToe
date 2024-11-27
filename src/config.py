import numpy as np
from enum import Enum

#Display Constants
SCREEN_HEIGHT = 900
SCREEN_WIDTH = 900

FIELD_COORDINATES = np.array([
    [[25, 25], [325, 25], [625, 25]],
    [[25, 325], [325, 325], [625, 325]],
    [[25, 625], [325, 625], [625, 625]]
])

MULTI_PLAYER_POS = [300, 400]
SINGLE_PLAYER_POS = [300, 550]
QUIT_POS = [300, 700]
REMATCH_POS = [300, 400]
BACK_POS = [300, 550]

#game
class gameState(Enum):
    START = 0
    SINGLEPLAYER = 1
    MULTIPLAYER = 2
    END = 3

#Input Constants
FIELD_RECTANGLES = np.array([
    [[0, 0, 300, 300], [300, 0, 300, 300], [600, 0, 300, 300]],
    [[0, 300, 300, 300], [300, 300, 300, 300], [600, 300, 300, 300]],
    [[0, 600, 300, 300], [300, 600, 300, 300], [600, 600, 300, 300]]
])

MULTI_PLAYER_RECT = [300, 400, 300, 100]
SINGLE_PLAYER_RECT = [300, 550, 300, 100]
QUIT_RECT = [300, 700, 300, 100]
REMATCH_RECT = [300, 400, 300, 100]
BACK_RECT = [300, 550, 300, 100]