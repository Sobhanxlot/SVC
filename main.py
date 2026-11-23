def rgb(r, g, b):
    return r, g, b

# Import Library
import pygame
import sys

# Import Files
from var import *
from MainMenu import *
from init import *


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    MainMenu()

    pygame.display.update()