import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Función para realizar la traslación
def translate(point, translation):
    return point + translation

# Puntos iniciales del objeto
points = np.array([[1, 1], [2, 3], [3, 2]])

# Vector de traslación
translation_vector = np.array([3, 4])

# Función de inicialización para crear el gráfico vacío
def init():
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    return []

# Función de animación para actualizar los puntos
def update(frame):
    ax.clear()
    new_points = [translate(point, translation_vector) for point in points]
    ax.plot(*zip(*new_points), marker='o')
    return []

fig, ax = plt.subplots()
animation = FuncAnimation(fig, update, frames=np.arange(0, 10), init_func=init, blit=True)
plt.show()
