import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from objects.cube import Cube

class App:
    def __init__(self):
        self.DISPLAY_SIZE = (640, 480)
    
        # Inicialize Pygame
        pg.init()
        pg.display.set_mode(self.DISPLAY_SIZE, DOUBLEBUF | OPENGL)
        self.clock = pg.time.Clock()
        
        # Setup OpenGL
        self._set_up_opengl()
        
        self.cube = Cube(1, (1.0, 0.0, 0.0))
        

    def _set_up_opengl(self) -> None:
        glClearColor(0.1, 0.2, 0.2, 1)
        gluPerspective(45, (self.DISPLAY_SIZE[0] / self.DISPLAY_SIZE[1]), 0.1, 50.0)
        glTranslatef(0.0, 0.0, -5)

    def run(self) -> None:
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            
            glRotatef(1, 3, 1, 1)
            self.cube.draw()
            
            pg.display.flip()
            self.clock.tick(60)

    def quit(self) -> None:
        pg.quit()


if __name__ == "__main__":

    my_app = App()
    my_app.run()
    my_app.quit()