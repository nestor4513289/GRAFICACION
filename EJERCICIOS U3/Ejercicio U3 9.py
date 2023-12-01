import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Definir el polígono original
original_polygon = np.array([[1, 1], [2, 1], [1.5, 2]])

# Factor de escala para el polígono
scale_factor = 2

# Función para escalar el polígono
def scale_polygon(polygon, scale):
    return polygon * scale

# Crear una figura y un eje
fig, ax = plt.subplots()

# Función de inicialización: dibuja el polígono original
def init():
    ax.plot(original_polygon[:, 0], original_polygon[:, 1], 'b-', label='Original')
    ax.legend()
    return ax

# Función de actualización: escala el polígono y actualiza la gráfica
def update(frame):
    ax.clear()
    scaled_polygon = scale_polygon(original_polygon, frame)
    ax.plot(original_polygon[:, 0], original_polygon[:, 1], 'b-', label='Original')
    ax.plot(scaled_polygon[:, 0], scaled_polygon[:, 1], 'r--', label=f'Scaled {frame}x')
    ax.legend()
    return ax

# Crear la animación
frames = np.linspace(1, scale_factor, 100)  # 100 frames para la animación
ani = FuncAnimation(fig, update, frames=frames, init_func=init, blit=False, interval=50)

plt.show()
