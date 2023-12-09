import pygame
import math


pygame.init()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


width, height = 400, 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Rotación de un cuadrado')

clock = pygame.time.Clock()

def draw_square(angle):
    square_size = 100
    square = pygame.Surface((square_size, square_size), pygame.SRCALPHA)
    pygame.draw.rect(square, WHITE, (0, 0, square_size, square_size))

  
    rotated_square = pygame.transform.rotate(square, angle)

  
    square_rect = rotated_square.get_rect(center=(width // 2, height // 2))

    return rotated_square, square_rect

angle = 0

running = True
while running:
    window.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    rotated_square, square_rect = draw_square(angle)
    window.blit(rotated_square, square_rect)

    angle += 1  

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
