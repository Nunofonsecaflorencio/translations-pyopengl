from OpenGL.GL import *
from OpenGL.GLU import *

class Cube:
    def __init__(self, size, color):
        self.size = size
        self.color = color
        self._define()
        
    def _define(self):
        d = self.size / 2.0
        self.verticies = (
            (d, d, -d),
            (-d, d, -d),
            (-d, -d, -d),
            (d, -d, -d),
            (d, d, d),
            (-d, d, d),
            (-d, -d, d),
            (d, -d, d),
        )
        self.edges = (
            (0, 1), (1, 2), (2, 3), (3, 0), # Back face
            (4, 5), (5, 6), (6, 7), (7, 4), # Front face
            (0, 4), (1, 5), (2, 6), (3, 7), # Back-Front Connections
        )
    
    def draw(self):
        glColor3f(*self.color)
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.verticies[vertex])
        glEnd()