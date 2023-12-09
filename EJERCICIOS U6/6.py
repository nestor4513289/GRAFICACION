import pygame
import sys
import math


pygame.init()


width, height = 600, 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Transformaciones')


black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

triangle_points = [(0, -50), (-50, 50), (50, 50)]

x, y = width // 2, height // 2

angle = 0

scale = 1.0

clock = pygame.time.Clock()

running = True
while running:
    window.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x += 1
    y += 1

    
    angle += 1  
    rotated_points = []
    for point in triangle_points:
        rotated_x = point[0] * math.cos(math.radians(angle)) - point[1] * math.sin(math.radians(angle))
        rotated_y = point[0] * math.sin(math.radians(angle)) + point[1] * math.cos(math.radians(angle))
        rotated_points.append((rotated_x, rotated_y))

  
    scaled_points = [(point[0] * scale, point[1] * scale) for point in rotated_points]
    scale += 0.01  

    pygame.draw.polygon(window, red, [(x + p[0], y + p[1]) for p in scaled_points])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
