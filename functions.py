import pygame
pygame.init()

#COLORS
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

#GLOBAL VARIABLES
width = 640 #largura
height = 480 #altura
initial_size = 10
score_height = 40
clock = pygame.time.Clock()
background = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake")

#TEXTS FUNCTION
def text(msg, cor, text_size, x, y):
    font = pygame.font.SysFont(None, text_size)
    text1 = font.render(msg, True, cor)
    background.blit(text1, [x,y])

#APPLE RANDOM
def apple(apple_x, apple_y):
    pygame.draw.rect(background, red, [apple_x, apple_y, initial_size, initial_size])

#SNAKE GROWTH
def snake(snakeXY):
    for XY in snakeXY:
        pygame.draw.rect(background, black, [XY[0], XY[1], initial_size, initial_size])

