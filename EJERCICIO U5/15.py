import pygame
import sys

pygame.init()

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Escena Táctil")

clock = pygame.time.Clock()

circles = [] 

running = True
while running:
    screen.fill(BLACK)  
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN: 
            if event.button == 1: 
                pos = pygame.mouse.get_pos() 
                radius = 30  
                circles.append((pos, radius))  
    for circle in circles:
        pygame.draw.circle(screen, RED, circle[0], circle[1])  

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()
