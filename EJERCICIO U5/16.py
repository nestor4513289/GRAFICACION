import pygame
import sys

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Selección de Objetos')

rect = pygame.Rect(200, 200, 100, 100)
rect_color = RED  

def draw_scene():
    screen.fill(WHITE)
    pygame.draw.rect(screen, rect_color, rect)
    pygame.display.flip()

running = True
while running:
    draw_scene()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  
            pos = pygame.mouse.get_pos()
            if rect.collidepoint(pos):
                rect_color = BLACK  

pygame.quit()
sys.exit()
