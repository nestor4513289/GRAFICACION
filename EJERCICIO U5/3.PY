import matplotlib.pyplot as plt
import numpy as np

def dibujar_triangulo():

    triangulo_original = np.array([[0, 0], [1, 0], [0.5, 1], [0, 0]])

    plt.figure(figsize=(5, 5))
    plt.plot(triangulo_original[:, 0], triangulo_original[:, 1], 'b-')
    plt.fill(triangulo_original[:, 0], triangulo_original[:, 1], color='lightblue')
    plt.title('Triángulo Original')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid()
    plt.axis('equal')

    traslacion_x = 2
    traslacion_y = 3

    traslacion = np.array([[1, 0, traslacion_x],
                           [0, 1, traslacion_y],
                           [0, 0, 1]])

    triangulo_trasladado = np.dot(triangulo_original, traslacion[:2, :2].T) + traslacion[:2, 2]

    plt.figure(figsize=(5, 5))
    plt.plot(triangulo_trasladado[:, 0], triangulo_trasladado[:, 1], 'g-')
    plt.fill(triangulo_trasladado[:, 0], triangulo_trasladado[:, 1], color='lightgreen')
    plt.title('Triángulo Trasladado')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid()
    plt.axis('equal')

    plt.show()

dibujar_triangulo()
