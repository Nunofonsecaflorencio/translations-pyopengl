import pygame as pg
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram,compileShader

from objects.triangle import Triangle
from utils import create_shader



class App:
    """
        For now, the app will be handling everything.
        Later on we'll break it into subcomponents.
    """

    def __init__(self):
        """ Initialise the program """

        self._set_up_pygame()

        self._set_up_timer()

        self._set_up_opengl()
        
        self._create_assets()
    
    def _set_up_pygame(self) -> None:
        """
            Initialize and configure pygame.
        """

        pg.init()
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK,
                                    pg.GL_CONTEXT_PROFILE_CORE)
        pg.display.set_mode((640,480), pg.OPENGL|pg.DOUBLEBUF)

    def _set_up_timer(self) -> None:
        """
            Set up the app's timer.
        """

        self.clock = pg.time.Clock()
    
    def _set_up_opengl(self) -> None:
        """
            Configure any desired OpenGL options
        """

        glClearColor(0.1, 0.2, 0.2, 1)
    
    def _create_assets(self) -> None:
        """
            Create all of the assets needed for drawing.
        """

        self.triangle = Triangle()
        self.shader = create_shader(
            vertex_filepath = "shaders/vertex.txt", 
            fragment_filepath = "shaders/fragment.txt")
    
    def run(self) -> None:
        """ Run the app """

        running = True
        while (running):
            #check events
            for event in pg.event.get():
                if (event.type == pg.QUIT):
                    running = False
            #refresh screen
            glClear(GL_COLOR_BUFFER_BIT)

            glUseProgram(self.shader)
            self.triangle.arm_for_drawing()
            self.triangle.draw()

            pg.display.flip()

            #timing
            self.clock.tick(60)

    def quit(self) -> None:
        """ cleanup the app, run exit code """

        self.triangle.destroy()
        glDeleteProgram(self.shader)
        pg.quit()


if __name__ == "__main__":

    my_app = App()
    my_app.run()
    my_app.quit()