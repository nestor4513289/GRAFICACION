import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Puntos iniciales
points = np.array([[1, 1], [2, 2], [3, 3]])

# Definir la función de traslación
def translate(points, tx, ty):
    translation_matrix = np.array([[1, 0, tx],
                                   [0, 1, ty],
                                   [0, 0, 1]])

    # Agregar columna de unos para poder hacer la multiplicación matricial
    homogeneous_coords = np.hstack((points, np.ones((len(points), 1))))

    # Realizar la multiplicación matricial para la traslación
    translated_points = np.dot(homogeneous_coords, translation_matrix.T)[:, :2]
    return translated_points

# Definir la animación
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

# Dibujar los puntos originales
scatter = ax.scatter(points[:, 0], points[:, 1])

# Función de animación
def animate(i):
    translated = translate(points, i * 0.1, i * 0.1)  # Realizar la traslación con valores cambiantes
    scatter.set_offsets(translated)  # Actualizar la posición de los puntos

ani = FuncAnimation(fig, animate, frames=50, interval=100)
plt.show()
