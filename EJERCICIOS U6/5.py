import turtle

screen = turtle.Screen()
screen.title("Escala de un círculo")
screen.bgcolor("white")
pen = turtle.Turtle()


def dibujar_circulo():
    pen.circle(100)  

def escalar_circulo(factor_escala):
    pen.clear()  
    nuevo_radio = 100 * factor_escala
    pen.circle(nuevo_radio)  

dibujar_circulo()

factor = float(input("Ingresa el factor de escala (por ejemplo, 1.5 para aumentar el tamaño en un 50%): "))

escalar_circulo(factor)

turtle.done()
