import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)

rotate = False
zoom = 0
zoom_factor = 0.1

def draw_cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    global rotate, zoom

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:  
                    zoom += zoom_factor
                elif event.button == 5:  
                    zoom -= zoom_factor
            elif event.type == pygame.MOUSEMOTION:
                if event.buttons[0] == 1:  
                    rotate = True
                    x, y = event.rel
                    glRotatef(y, 1, 0, 0)
                    glRotatef(x, 0, 1, 0)
                else:
                    rotate = False

        if rotate:
            x, y = pygame.mouse.get_pos()
            x = (x - display[0] / 2) / 10
            y = (y - display[1] / 2) / 10
            glRotatef(y, 1, 0, 0)
            glRotatef(x, 0, 1, 0)

        glTranslatef(0.0, 0.0, zoom)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_cube()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
