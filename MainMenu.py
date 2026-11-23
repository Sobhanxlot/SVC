def rgb(r, g, b):
    return r, g, b

import pygame
from var import *
from init import *
from assets import *

pygame.init()

class MainMenu:
    def __init__(self):
        screen.fill(rgb(19, 27, 43))

        # navar samt chap
        pygame.draw.rect(screen, rgb(48, 56, 65), (0,50, 50, HEIGHT))


        # navar bala
        pygame.draw.rect(screen, rgb(48, 56, 65), (0,0, WIDTH, 50))
        icon = pygame.image.load(rp("logonbg.png"))
        icon = pygame.transform.smoothscale(icon, (40, 40))
        screen.blit(icon, (5, 5))

        # joda kaardan navar ha
        pygame.draw.line(screen, rgb(47, 74, 99), (0, 49), (WIDTH, 49), 2)
        pygame.draw.line(screen, rgb(47, 74, 99), (49,50), (49, HEIGHT), 2)