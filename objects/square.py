from OpenGL.GL import *
from OpenGL.GLU import *

class Square:
    def __init__(self, initial_position, size, color):
        self.col, self.row = initial_position
        self.size = size
        self.color = color
        self.direction = (0, 0)


    def draw(self):
        glColor(*self.color)  # Set color to green
        glBegin(GL_QUADS)
        glVertex(0, 0)                 # Bottom-left
        glVertex(1, 0)          # Bottom-right
        glVertex(1, 1)   # Top-right
        glVertex(0, 1)          # Top-left
        glEnd()
        
        
        
    def update(self):
        
        self.col += self.direction[0]
        self.row += self.direction[1]
        
        glScale(self.size, self.size, 1)
        x = self.col
        y = self.row
        glTranslate(x, y, 0)