import pygame

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Textura en Rectángulo')

texture = pygame.image.load('C:\\Users\\nesto\\OneDrive\\Escritorio\\EJERCICIOS U2\\1.1.png')

texture = pygame.transform.scale(texture, (200, 150))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(texture, (300, 200))

    pygame.display.flip()

pygame.quit()
