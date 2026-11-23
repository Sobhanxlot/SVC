import pygame
import sys

# Import Files
from var import *
from assets import *




pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SVC")

icon = pygame.image.load(rp("logo.png"))

pygame.display.set_icon(icon)