import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Definir el polígono inicial
polygon = np.array([[1, 1], [2, 1], [1.5, 2]])

# Parámetros para el cambio de escala
scale_factor = 2.0  # Factor de escala

# Función para aplicar el cambio de escala al polígono
def scale_polygon(polygon, scale_factor):
    return polygon * scale_factor

# Función para actualizar el gráfico en cada cuadro de la animación
def update(frame):
    ax.clear()
    
    # Aplicar el cambio de escala al polígono en cada cuadro
    scaled_polygon = scale_polygon(polygon, 1 + 0.1 * np.sin(frame / 10))
    
    # Dibujar el polígono original y el polígono escalado
    ax.plot(*np.append(polygon, [polygon[0]], axis=0).T, marker='o', linestyle='-', color='blue', label='Original')
    ax.plot(*np.append(scaled_polygon, [scaled_polygon[0]], axis=0).T, marker='o', linestyle='-', color='red', label='Escalado')
    
    ax.legend()
    ax.set_title('Cambio de escala de un polígono')

# Configurar la figura y el gráfico
fig, ax = plt.subplots()
ax.set_aspect('equal')
animation = FuncAnimation(fig, update, frames=200, interval=50)
plt.show()