import pygame
import sys


pygame.init()


width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Control de Rotación')


black = (0, 0, 0)
white = (255, 255, 255)

obj_image = pygame.image.load('1.png')
obj_rect = obj_image.get_rect(center=(width // 2, height // 2))

angle = 0

clock = pygame.time.Clock()

running = True
while running:
    screen.fill(white)

 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()
    

    if keys[pygame.K_LEFT]:
        angle += 3
    if keys[pygame.K_RIGHT]:
        angle -= 3
    

    rotated_image = pygame.transform.rotate(obj_image, angle)
    rotated_rect = rotated_image.get_rect(center=obj_rect.center)
    
    screen.blit(rotated_image, rotated_rect.topleft)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
