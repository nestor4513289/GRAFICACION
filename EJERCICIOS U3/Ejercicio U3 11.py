import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Función para convertir coordenadas homogéneas a estándar
def homogeneous_to_standard(point):
    return point[:-1] / point[-1]

# Función para convertir coordenadas estándar a homogéneas
def standard_to_homogeneous(point):
    return np.append(point, 1)

# Puntos en coordenadas homogéneas
homogeneous_points = np.array([
    [1, 2, 1],
    [3, 4, 2],
    [5, 6, 3]
])

# Convertir coordenadas homogéneas a estándar
standard_points = np.apply_along_axis(homogeneous_to_standard, 1, homogeneous_points)

# Configurar la visualización
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')
ax.grid(True)
ax.set_title('Conversión de Coordenadas')

# Crear objetos de puntos
homogeneous_plot, = ax.plot([], [], 'bo', label='Homogéneas')
standard_plot, = ax.plot([], [], 'ro', label='Estándar')
ax.legend()

# Función para inicializar la gráfica
def init():
    homogeneous_plot.set_data([], [])
    standard_plot.set_data([], [])
    return homogeneous_plot, standard_plot

# Función para actualizar la animación
def update(frame):
    homogeneous_plot.set_data(homogeneous_points[:frame+1, 0], homogeneous_points[:frame+1, 1])
    standard_plot.set_data(standard_points[:frame+1, 0], standard_points[:frame+1, 1])
    return homogeneous_plot, standard_plot

# Crear la animación
ani = FuncAnimation(fig, update, frames=range(3), init_func=init, blit=True, repeat=False, interval=1000)
plt.show()
