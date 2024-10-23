import random

from OpenGL.GL import *
from OpenGL.GLU import *

SNAKE_SIZE = 20


class Food:
    def __init__(self):
        self.position = self.generate_position()

    def generate_position(self):
        return (
            round(random.randint(0, 800 - SNAKE_SIZE), -1),
            round(random.randint(0, 600 - SNAKE_SIZE), -1)
        )

    def draw(self):
        glPushMatrix()
        glTranslatef(self.position[0], self.position[1], 0)
        glColor3f(1, 0, 0)
        glBegin(GL_QUADS)
        glVertex2f(-SNAKE_SIZE / 2, -SNAKE_SIZE / 2)
        glVertex2f(SNAKE_SIZE / 2, -SNAKE_SIZE / 2)
        glVertex2f(SNAKE_SIZE / 2, SNAKE_SIZE / 2)
        glVertex2f(-SNAKE_SIZE / 2, SNAKE_SIZE / 2)
        glEnd()
        glPopMatrix()
