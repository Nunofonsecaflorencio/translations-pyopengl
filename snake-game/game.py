import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from snake import Snake
from food import Food

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_mode(
            (WINDOW_WIDTH, WINDOW_HEIGHT), DOUBLEBUF | OPENGL)
        gluOrtho2D(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT)

        self.snake = Snake()
        self.food = Food()
        self.running = True
        
    def handle_events(self):
        pass
