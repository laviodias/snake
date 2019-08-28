import pygame
from random import randrange
from snakegame import functions

pygame.init()

#PRINCIPAL
def game():
    #SNAKE INITIAL POSITION
    pos_x = functions.width/2
    pos_y = functions.height/2

    #APPLE INITIAL POSITION
    apple_x = randrange(0, functions.height - functions.initial_size, 10)
    apple_y = randrange(0, functions.height - functions.initial_size - functions.score_height, 10)

    #VELOCITIES
    vel_x = vel_y = 0

    #SNAKE SIZE
    snakeXY = []
    snakeSize = 1

    #GAME CONDITIONS
    exit = True
    end_game = False
    points = 0
    while exit:
        while end_game:
            for event in pygame.event.get():
                #TO LEAVE
                if event.type == pygame.QUIT:
                    exit = False
                    end_game = False
                #TO RESET
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        pos_x = functions.width / 2
                        pos_y = functions.height / 2
                        apple_x = randrange(0, functions.height - functions.initial_size, 10)
                        apple_y = randrange(0, functions.height - functions.initial_size - functions.score_height, 10)
                        vel_x = vel_y = 0
                        snakeXY = []
                        snakeSize = 1
                        exit = True
                        end_game = False
                        points = 0
                    #TO EXIT
                    elif event.key == pygame.K_e:
                        exit = False
                        end_game = False
                #TO CLICK BUTTONS
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if x > functions.width/2-80 and y > 180 and x < (functions.width/2-90)+180 and y < 220:
                        pos_x = functions.width / 2
                        pos_y = functions.height / 2
                        apple_x = randrange(0, functions.height - functions.initial_size, 10)
                        apple_y = randrange(0, functions.height - functions.initial_size - functions.score_height, 10)
                        vel_x = vel_y = 0
                        snakeXY = []
                        snakeSize = 1
                        exit = True
                        end_game = False
                        points = 0
                    elif x > functions.width/2-90 and y > 240 and x < (functions.width/2-90)+200 and y < 280:
                        exit = False
                        end_game = False
            #CONF BUTTONS AND TEXTS
            functions.background.fill(functions.white)
            functions.text('Game Over', functions.red, 72, functions.width / 3 - 17, 35)
            functions.text('Final Score: ' + str(points), functions.black, 50, functions.width / 3 +5, 120)
            pygame.draw.rect(functions.background, functions.black, [functions.width / 2 - 90, 180, 200, 40])
            functions.text('Reset(R)', functions.white, 40, functions.width / 2 - 40, 185)
            pygame.draw.rect(functions.background, functions.black, [functions.width / 2 - 90, 240, 200, 40])
            functions.text('Exit(E)', functions.white, 40, functions.width / 2 - 30, 245)
            pygame.display.update()
        #KEYS TO MOVE
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and vel_x != functions.initial_size:
                    vel_y = 0
                    vel_x = -functions.initial_size
                elif event.key == pygame.K_RIGHT and vel_x != -functions.initial_size:
                    vel_y = 0
                    vel_x = functions.initial_size
                elif event.key == pygame.K_UP and vel_y != functions.initial_size:
                    vel_x = 0
                    vel_y = -functions.initial_size
                elif event.key == pygame.K_DOWN and vel_y != -functions.initial_size:
                    vel_x = 0
                    vel_y = functions.initial_size
        #GAME
        if exit:
            functions.background.fill(functions.white)
            pos_x += vel_x
            pos_y += vel_y

            if any(Bloco == snake_head for Bloco in snakeXY[:-1]):
                end_game = True
            #EAT APPLE
            if pos_x == apple_x and pos_y == apple_y:
                apple_x = randrange(0, functions.height - functions.initial_size, 10)
                apple_y = randrange(0, functions.height - functions.initial_size - functions.score_height, 10)
                snakeSize+=2
                points+=1
            #SNAKE GROWS
            snake_head = []
            snake_head.append(pos_x)
            snake_head.append(pos_y)
            snakeXY.append(snake_head)

            if len(snakeXY) > snakeSize:
                del snakeXY[0]
            #WALLS
            if pos_x >= functions.width or pos_x <= 0-functions.initial_size or pos_y >= functions.height - functions.score_height or pos_y <= 0-functions.initial_size:
                end_game = True
            #SCOREBOARD
            pygame.draw.rect(functions.background, functions.black, [0, functions.height - functions.score_height, functions.width, functions.score_height])
            functions.text('Score: '+str(points), functions.white, 20, 10, functions.height-27)

            functions.snake(snakeXY)
            functions.apple(apple_x, apple_y)
            functions.clock.tick(18)
            pygame.display.update()