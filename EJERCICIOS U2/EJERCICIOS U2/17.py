import pygame
import sys

pygame.init()

blanco = (255, 255, 255)
negro = (0, 0, 0)

ancho, alto = 600, 400
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption('Dibujar Palabras')

reloj = pygame.time.Clock()

def mostrar_texto(texto, x, y, tamaño=30):
    fuente = pygame.font.SysFont(None, tamaño)
    texto_renderizado = fuente.render(texto, True, negro)
    ventana.blit(texto_renderizado, (x, y))

terminado = False
texto_ingresado = ""
while not terminado:
    ventana.fill(blanco)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            terminado = True
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN:
                print(texto_ingresado)  
                texto_ingresado = ""  
            elif evento.key == pygame.K_BACKSPACE:
                texto_ingresado = texto_ingresado[:-1] 
            else:
                texto_ingresado += evento.unicode  
    
    mostrar_texto("Ingresa texto:", 20, 20)
    mostrar_texto(texto_ingresado, 20, 60)
    
    pygame.display.flip()
    reloj.tick(30)

pygame.quit()
sys.exit()
