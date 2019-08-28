import pygame
from snakegame import principal

try:
    pygame.init()
except:
    print('pygame module not found!')

principal.game()