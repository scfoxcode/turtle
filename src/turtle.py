import pygame

MOVE_AMMOUNT = 50 
LINE_COLOR = (255, 0, 0)

class Turtle:
    directions = ('N', 'E', 'S', 'W')
    movements = (
        pygame.Vector2(0, -MOVE_AMMOUNT), 
        pygame.Vector2(MOVE_AMMOUNT, 0), 
        pygame.Vector2(0, MOVE_AMMOUNT), 
        pygame.Vector2(-MOVE_AMMOUNT, 0), 
    )

    def __init__(self, surface, initialPosition):
        self.position = initialPosition 
        self.surface = surface
        self.direction = 0 
        self.paint = True

    def StopPainting(self):
        self.paint = False

    def StartPainting(self):
        self.paint = True 

    def TurnLeft(self):
        self.direction -= 1
        if self.direction < 0:
            self.direction = len(Turtle.directions) - 1 

    def TurnRight(self):
        self.direction += 1
        if self.direction >= len(Turtle.directions):
            self.direction = 0

    def MoveForward(self):
        start = self.position
        end = self.position + Turtle.movements[self.direction]

        if self.paint:
            pygame.draw.line(self.surface, LINE_COLOR, start, end, width = 5)

        self.position = end
