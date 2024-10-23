import pygame

from OpenGL.GL import *
from OpenGL.GLU import *

SNAKE_SIZE = 20
SNAKE_SPEED = 20


class Snake:
    def __init__(self):
        self.positions = [(400, 300)]
        self.direction = (1, 0)
        self.length = 5

    def draw(self):
        for x, y in self.positions:
            glPushMatrix()
            glTranslatef(x, y, 0)
            glColor3f(0, 1, 0)
            glBegin(GL_QUADS)

            glVertex2f(-SNAKE_SIZE / 2, -SNAKE_SIZE / 2)
            glVertex2f(SNAKE_SIZE / 2, -SNAKE_SIZE / 2)
            glVertex2f(SNAKE_SIZE / 2, SNAKE_SIZE / 2)
            glVertex2f(-SNAKE_SIZE / 2, SNAKE_SIZE / 2)

            glEnd()
            glPopMatrix()

    def move(self):
        head_x, head_y = self.positions[0]
        new_x = head_x + self.direction[0] * SNAKE_SPEED
        new_y = head_y + self.direction[1] * SNAKE_SPEED

        new_head = (new_x, new_y)

        self.positions = [new_head] + self.positions[:-1]

    def grow(self):
        self.positions.append(self.positions[-1])

    def change_direction(self, new_direction):
        if new_direction == "UP" and self.direction != (0, -1):
            self.direction = (0, 1)
        elif new_direction == "DOWN" and self.direction != (0, 1):
            self.direction = (0, -1)
        elif new_direction == "LEFT" and self.direction != (1, 0):
            self.direction = (-1, 0)
        elif new_direction == "RIGHT" and self.direction != (-1, 0):
            self.direction = (1, 0)

    def check_collisions(self):
        head_x, head_y = self.positions[0]

        if head_x < 0 or head_x > 800 or head_y < 0 or head_y > 600:
            return True

        if self.positions[0] in self.positions[1:]:
            return True

        return False
