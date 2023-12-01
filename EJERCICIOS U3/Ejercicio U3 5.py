import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Función para rotar un punto en 2D alrededor del origen
def rotate_point(point, angle):
    x, y = point
    new_x = x * np.cos(angle) - y * np.sin(angle)
    new_y = x * np.sin(angle) + y * np.cos(angle)
    return new_x, new_y

# Definir los vértices del cuadrado
square = np.array([[1, 1], [-1, 1], [-1, -1], [1, -1], [1, 1]])

# Crear la figura y el eje
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
line, = ax.plot([], [], 'r-')

# Función de inicialización: crea el gráfico vacío
def init():
    line.set_data([], [])
    return line,

# Función de animación: realiza la rotación y actualiza el gráfico
def animate(frame):
    angle = frame * np.pi / 180  # Ángulo de rotación en radianes
    rotated_square = np.array([rotate_point(point, angle) for point in square])
    x = rotated_square[:, 0]
    y = rotated_square[:, 1]
    line.set_data(x, y)
    return line,

# Crear la animación
frames = 360  # Número de cuadros en la animación (360 grados)
ani = FuncAnimation(fig, animate, frames=frames, init_func=init, blit=True)

plt.title('Rotación de un cuadrado')
plt.show()
