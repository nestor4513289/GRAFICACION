import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Creamos la figura y el eje
fig, ax = plt.subplots()
ax.set_aspect('equal')

# Creamos un punto inicial
point, = ax.plot([], [], 'bo')  # Punto azul

# Función para inicializar la animación
def init():
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    return point,

# Función de animación que actualiza la posición del punto en cada cuadro
def update(frame):
    angle = np.radians(frame)  # Convertimos el número de cuadro a radianes
    x = np.cos(angle)  # Calculamos la coordenada x
    y = np.sin(angle)  # Calculamos la coordenada y
    point.set_data(x, y)  # Actualizamos la posición del punto
    return point,

# Creamos la animación
ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 2), init_func=init, blit=True)

plt.title('Animación con diferentes ángulos de rotación')
plt.show()
