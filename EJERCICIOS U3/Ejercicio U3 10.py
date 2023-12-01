import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Función para rotar un punto (coordenadas homogéneas) por un ángulo dado
def rotate_point(point, angle):
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle), 0],
        [np.sin(angle), np.cos(angle), 0],
        [0, 0, 1]
    ])
    return rotation_matrix.dot(point)

# Triángulo inicial en coordenadas homogéneas
triangle = np.array([
    [0, 1, 0],  # Punto A
    [1, -1, 0], # Punto B
    [-1, -1, 0] # Punto C
])

# Crear la figura y los ejes
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

# Crear los objetos de línea para representar el triángulo
line, = ax.plot([], [], 'r-')
line.set_data([], [])

# Función de inicialización
def init():
    line.set_data([], [])
    return line,

# Función de animación
def animate(frame):
    angle = frame * np.pi / 180  # Cambia el ángulo por cada frame
    rotated_triangle = np.array([rotate_point(point, angle) for point in triangle.T]).T
    x = np.append(rotated_triangle[:, 0], rotated_triangle[0, 0])  # Añade el primer punto al final para cerrar el triángulo
    y = np.append(rotated_triangle[:, 1], rotated_triangle[0, 1])  # Añade el primer punto al final para cerrar el triángulo
    line.set_data(x, y)
    return line,

# Crear la animación
ani = FuncAnimation(fig, animate, frames=360, init_func=init, blit=True, interval=50)

# Mostrar la animación
plt.show()
