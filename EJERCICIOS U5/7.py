import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

angle = 0

def cube():
    glBegin(GL_QUADS)
    vertices = [
        [1, -1, -1],
        [1, 1, -1],
        [-1, 1, -1],
        [-1, -1, -1],
        [1, -1, 1],
        [1, 1, 1],
        [-1, -1, 1],
        [-1, 1, 1]
    ]
    edges = [
        [0, 1, 2, 3],
        [3, 2, 7, 6],
        [6, 7, 5, 4],
        [4, 5, 1, 0],
        [1, 5, 7, 2],
        [4, 0, 3, 6]
    ]
    for edge in edges:
        glColor3fv((0, 1, 0)) 
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def cone():
    quadric = gluNewQuadric()
    gluQuadricNormals(quadric, GLU_SMOOTH)
    gluCylinder(quadric, 1, 0, 2, 20, 2)

def draw():
    global angle
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluPerspective(45, (800 / 600), 0.1, 50.0)
    glTranslatef(0, 0, -10)

 
    glPushMatrix()
    glTranslatef(-2, 0, -5)
    glRotatef(angle, 1, 1, 0)  
    cube()
    glPopMatrix()

    
    glPushMatrix()
    glTranslatef(2, 0, -15)
    glRotatef(angle, 0, 1, 1)  
    cone()
    glPopMatrix()

    angle += 1  

    pygame.display.flip()
    pygame.time.wait(10)

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glEnable(GL_DEPTH_TEST)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw()

if __name__ == "__main__":
    main()
