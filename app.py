import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from objects.cube import Cube

class App:
    def __init__(self):
        self.DISPLAY_SIZE = (640, 480)
    
        # Inicialize Pygame
        pygame.init()
        pygame.display.set_mode(self.DISPLAY_SIZE, DOUBLEBUF | OPENGL)
        self.clock = pygame.time.Clock()
        
        # Setup OpenGL
        self._set_up_opengl()
        
        # Cubo
        self.cube = Cube(size=1, color=(1.0, 0.0, 0.0))
        

    def _set_up_opengl(self) -> None:
        glClearColor(0.1, 0.2, 0.2, 1)
        gluPerspective(45, (self.DISPLAY_SIZE[0] / self.DISPLAY_SIZE[1]), 0.1, 50.0)
        glTranslatef(0.0, 0.0, -5)
        
    

    def run(self) -> None:
        running = True
        while running:
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.translate(event)

            
            
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            
            # glRotatef(1, 3, 1, 1)
            self.cube.draw()
            
            pygame.display.flip()
            self.clock.tick(60)

    def quit(self) -> None:
        pygame.quit()
    
    def translate(self, event):
         if event.type == pygame.KEYDOWN:
            if event.key== pygame.K_UP:
                glTranslatef(0, 0.5, 0)
            if event.key == pygame.K_DOWN:
                glTranslatef(0, -0.5, 0)
            if event.key == pygame.K_LEFT:
                glTranslatef(-0.5, 0, 0)
            if event.key == pygame.K_RIGHT:
                glTranslatef(0.5, 0, 0)
        
    


if __name__ == "__main__":

    my_app = App()
    my_app.run()
    my_app.quit()