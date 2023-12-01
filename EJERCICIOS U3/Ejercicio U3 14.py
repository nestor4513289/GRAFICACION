import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Generar un polígono irregular de ejemplo
points = np.array([[1, 1], [2, 3], [4, 5], [6, 3], [5, 1]])

# Definir el área rectangular de recorte
clip_rect = [2, 2, 4, 4]  # [xmin, ymin, ancho, altura]

# Función para animar
def animate(i):
    plt.clf()

    # Dibujar el polígono irregular
    plt.plot(points[:, 0], points[:, 1], 'b-')

    # Dibujar el área de recorte rectangular
    rect = plt.Rectangle((clip_rect[0], clip_rect[1]), clip_rect[2], clip_rect[3], fill=False, edgecolor='r')
    plt.gca().add_patch(rect)

    # Definir límites de la gráfica
    plt.xlim(0, 8)
    plt.ylim(0, 6)

# Crear la figura y la animación
fig = plt.figure()
ani = animation.FuncAnimation(fig, animate, frames=100, interval=100)
plt.show()
