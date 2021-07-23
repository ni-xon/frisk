import pygame
import random


ROWS, COLS = 8, 8
HEIGHT = 800
WIDTH = (HEIGHT // ROWS) + HEIGHT
SQUARE_SIZE = HEIGHT // COLS

# RGB
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (128, 128, 128)
YELLOW = (255, 255, 0)
DARK_GREEN = (3, 125, 80)
ORANGE = (255, 165, 0)

# LIGHTER
LIGHT_RED = (255, 102, 102)
LIGHT_BLUE = (102, 178, 255)
LIGHT_GREEN = (153, 255, 153)
LIGHT_ORANGE = (255, 204, 153)
LIGHT_GRAY = (224, 224, 224)

#
NO_PLAYERS = 4

# PLAYER COLOURS
PLAYER_COLOURS = [GRAY, RED, BLUE, GREEN, ORANGE]
PLAYER_LIGHTER_COLOURS = [LIGHT_GRAY, LIGHT_RED, LIGHT_BLUE, LIGHT_GREEN, LIGHT_ORANGE]

# Territory Constants
TER_NUM = ROWS      # "How to calc #Territories" can be changed later with team
X = (((ROWS*COLS)%TER_NUM)/2)+2

COLOUR_LIST = []
for _ in range(TER_NUM):
    COLOUR_LIST.append(tuple(random.choices(range(256), k=3)))

# PIECE COSTS
UNIT_COST = 20

# DEFAULT POWER VALUES
BUILDING_POWER = 500
UNIT_POWER = 100