import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dibujando líneas")

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)

running = True
while running:
    screen.fill(white)  

    pygame.draw.line(screen, black, (50, 50), (200, 50), 5)
    pygame.draw.line(screen, red, (50, 100), (200, 100), 3)
    pygame.draw.line(screen, green, (50, 150), (200, 150), 7)
    pygame.draw.line(screen, blue, (50, 200), (200, 200), 2)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
