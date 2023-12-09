import pygame
import sys


pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Escena con luces')


white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


object1_pos = (200, 300)
object2_pos = (500, 350)


light1 = pygame.Surface((width, height))
light1.set_colorkey((0, 0, 0))
light1.set_alpha(100)
light1.fill(white)

light2 = pygame.Surface((width, height))
light2.set_colorkey((0, 0, 0))
light2.set_alpha(100)
light2.fill(white)


while True:
    screen.fill(white)

    pygame.draw.circle(screen, red, object1_pos, 50)
    pygame.draw.rect(screen, blue, pygame.Rect(object2_pos[0] - 30, object2_pos[1] - 30, 60, 60))

    screen.blit(light1, (0, 0))
    screen.blit(light2, (0, 0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    pygame.display.flip()
