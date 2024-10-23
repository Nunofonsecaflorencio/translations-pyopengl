import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from random import randint

from objects.square import Square

class App:
    def __init__(self):
        self.CELL_SIZE = 40
        self.ROWS = 15
        self.COLS = 20
        self.DISPLAY_SIZE = (self.COLS * self.CELL_SIZE, self.ROWS * self.CELL_SIZE)
    
        # Inicialize Pygame
        pygame.init()
        pygame.display.set_mode(self.DISPLAY_SIZE, DOUBLEBUF | OPENGL)
        self.clock = pygame.time.Clock()
        
        # Setup OpenGL
        self._set_up_opengl()
        
        # Cubo
        # self.cube = Cube(size=1, color=(1.0, 0.0, 0.0))
        self.snake = Square((1, 1), self.CELL_SIZE, (0, 1, 0))
        self.apple = Square((5, 5), self.CELL_SIZE, (1, 0, 0))
        
        

    def _set_up_opengl(self) -> None:
        glClearColor(0.1, 0.2, 0.2, 1)
        # gluPerspective(45, (self.DISPLAY_SIZE[0] / self.DISPLAY_SIZE[1]), 0.1, 50.0)
        gluOrtho2D(0, self.DISPLAY_SIZE[0], 0, self.DISPLAY_SIZE[1])
        # glTranslatef(0.0, 0.0, -5)
        
    

    def run(self) -> None:
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                # self.translate(event)

                if event.type == pygame.KEYDOWN:
                    if event.key== pygame.K_UP:
                        self.snake.direction = (0, 1)
                    if event.key == pygame.K_DOWN:
                        self.snake.direction = (0, -1)
                    if event.key == pygame.K_LEFT:
                        self.snake.direction = (-1, 0)
                    if event.key == pygame.K_RIGHT:
                        self.snake.direction = (1, 0)
             
             
            
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            
            self.draw_grid()
            
            # Collision
            if (self.snake.row, self.snake.col) == (self.apple.row, self.apple.col):
                self.apple.row, self.apple.col = randint(0, self.ROWS - 1), randint(0, self.COLS - 1)
            
            # Wormhole :)
            if self.snake.row < 0:
                self.snake.row = self.ROWS
            if self.snake.row > self.ROWS:
                self.snake.row = 0
            if self.snake.col < 0:
                self.snake.col = self.COLS
            if self.snake.col > self.COLS:
                self.snake.col = 0
            
            for square in [self.snake, self.apple]:
                glPushMatrix()
                square.update()  
                square.draw()
                glPopMatrix()
            
            pygame.display.flip()
            self.clock.tick(10)

    def quit(self) -> None:
        pygame.quit()
    
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