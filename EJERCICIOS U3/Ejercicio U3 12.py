import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Creamos una figura y un eje
fig, ax = plt.subplots()
ax.set_aspect('equal')

# Creamos un objeto inicial (por ejemplo, un triángulo)
object_points = np.array([[0, 0], [1, 0], [0.5, 1], [0, 0]])

# Función para inicializar la animación
def init():
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    return []

# Función de animación
def animate(i):
    # Traslación
    translation_matrix = np.array([[1, 0.01 * i], [0, 1]])  # Cambia la traslación en el eje x
    translated_points = np.dot(object_points, translation_matrix)
    
    # Rotación
    angle = np.radians(1 * i)  # Cambia el ángulo de rotación
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])
    rotated_points = np.dot(translated_points, rotation_matrix)

    # Actualizamos la posición del objeto en el gráfico
    ax.clear()
    ax.plot(rotated_points[:, 0], rotated_points[:, 1])
    return []

# Creamos la animación
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=360, interval=20, blit=True)

# Mostramos la animación
plt.show()