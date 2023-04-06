import pygame, sys, random
from pygame.locals import *
from turtle import Turtle
pygame.init()
 
# Colours
BACKGROUND = (255, 255, 255)
 
WINDOW_WIDTH = 1280 
WINDOW_HEIGHT = 720 
 
pygame.display.set_caption('My Game!')
 
# The main function that controls the game
def main () :
    looping = True
    surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    bob = Turtle(surface, pygame.Vector2(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

    # *********************************** START MOVING TURTLE 
    surface.fill(BACKGROUND)
    # Write the Y
    bob.TurnRight()
    bob.TurnRight()
    bob.MoveForward()
    bob.TurnLeft()
    bob.MoveForward()
    bob.TurnLeft()
    bob.MoveForward()
    bob.TurnRight()
    bob.TurnRight()
    bob.MoveForward()
    bob.MoveForward()
    bob.TurnRight()
    bob.MoveForward()

    # Stop painting and move to position to start o
    bob.StopPainting()
    bob.TurnRight()
    bob.MoveForward()
    bob.MoveForward()
    bob.TurnRight()
    bob.MoveForward()
    bob.MoveForward()
    bob.TurnRight()
    bob.StartPainting()

    # Write the o
    bob.MoveForward()
    bob.TurnLeft()
    bob.MoveForward()
    bob.TurnLeft()
    bob.MoveForward()
    bob.TurnLeft()
    bob.MoveForward()

    # Stop painting and move to position to start l
    bob.StopPainting()
    bob.TurnRight()
    bob.TurnRight()
    bob.MoveForward()
    bob.MoveForward()
    bob.TurnRight()
    bob.StartPainting()

    # Write the l
    bob.MoveForward()
    bob.MoveForward()
    bob.TurnLeft()
    bob.MoveForward()

    # Stop painting and move to position to start final o
    bob.StopPainting()
    bob.TurnLeft()
    bob.MoveForward()
    bob.MoveForward()
    bob.TurnRight()
    bob.MoveForward()
    bob.TurnRight()
    bob.StartPainting()

    # Write the o
    bob.MoveForward()
    bob.TurnLeft()
    bob.MoveForward()
    bob.TurnLeft()
    bob.MoveForward()
    bob.TurnLeft()
    bob.MoveForward()
    


    pygame.display.update()
    # *********************************** FINISH MOVING TURTLE 
  
    # Loop forever until exit is pressed
    while looping :
        # Get inputs
        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
                sys.exit()
 
main()
