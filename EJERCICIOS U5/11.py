import pygame
from pygame.locals import *
import sys


pygame.init()


width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Vista Isométrica 3D')


WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


def project(x, y, z):

    x_screen = (x - y) * 0.866
    y_screen = -z + (x + y) * 0.5
    return x_screen, y_screen

cube_vertices = [
    (-50, -50, -50),
    (-50, -50, 50),
    (-50, 50, -50),
    (-50, 50, 50),
    (50, -50, -50),
    (50, -50, 50),
    (50, 50, -50),
    (50, 50, 50)
]

cube_edges = [
    (0, 1), (1, 3), (3, 2), (2, 0),
    (4, 5), (5, 7), (7, 6), (6, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

running = True
while running:
    screen.fill(WHITE)

    for edge in cube_edges:
        start = cube_vertices[edge[0]]
        end = cube_vertices[edge[1]]
        start_screen = project(*start)
        end_screen = project(*end)
        pygame.draw.line(screen, RED, (width/2 + start_screen[0], height/2 + start_screen[1]),
                         (width/2 + end_screen[0], height/2 + end_screen[1]), 2)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
sys.exit()
