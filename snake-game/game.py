import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from snake import Snake, SNAKE_SIZE
from food import Food

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_mode(
            (WINDOW_WIDTH, WINDOW_HEIGHT), DOUBLEBUF | OPENGL)
        gluOrtho2D(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT)

        self.snake = Snake()
        self.food = Food()
        self.running = True

    def draw_grid(self):
        glPushMatrix()

        glScale(self.CELL_SIZE, self.CELL_SIZE, 0)

        glColor(0, 0, 0, .2)
        glBegin(GL_LINES)

        for j in range(self.ROWS):
            glVertex(0, j)
            glVertex(self.COLS, j)
        for i in range(self.COLS):
            glVertex(i, 0)
            glVertex(i, self.ROWS)
        glEnd()
        glPopMatrix()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    self.snake.change_direction("UP")
                elif event.key == K_DOWN:
                    self.snake.change_direction("DOWN")
                elif event.key == K_LEFT:
                    self.snake.change_direction("LEFT")
                elif event.key == K_RIGHT:
                    self.snake.change_direction("RIGHT")

    def check_food_collision(self):
        head_x, head_y = self.snake.positions[0]
        food_x, food_y = self.food.position

        if abs(head_x - food_x) < SNAKE_SIZE and abs(head_y - food_y) < SNAKE_SIZE:
            self.snake.grow()
            self.food = Food()

    def run(self):
        while self.running:
            self.handle_events()
            self.snake.move()
            self.check_food_collision()

            if not self.snake.just_grew and self.snake.check_collisions():
                self.running = False

            glClear(GL_COLOR_BUFFER_BIT)

            # self.draw_grid()
            self.snake.draw()
            self.food.draw()

            pygame.display.flip()
            pygame.time.wait(100)

        pygame.quit()
