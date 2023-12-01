import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Función para determinar el código de región de un punto
def compute_code(x, y, xmin, ymin, xmax, ymax):
    code = 0
    if x < xmin:  # A la izquierda del área de recorte
        code |= 1
    elif x > xmax:  # A la derecha del área de recorte
        code |= 2
    if y < ymin:  # Por debajo del área de recorte
        code |= 4
    elif y > ymax:  # Por encima del área de recorte
        code |= 8
    return code

# Función para aplicar el algoritmo de recorte
def cohen_sutherland(x1, y1, x2, y2, xmin, ymin, xmax, ymax):
    code1 = compute_code(x1, y1, xmin, ymin, xmax, ymax)
    code2 = compute_code(x2, y2, xmin, ymin, xmax, ymax)
    accept = False

    while True:
        if not (code1 | code2):  # Ambos puntos dentro del área de recorte
            accept = True
            break
        elif code1 & code2:  # Ambos puntos están fuera de una misma región, por lo que la línea está completamente fuera
            break
        else:
            x = 0
            y = 0
            if code1:
                code_out = code1
            else:
                code_out = code2

            if code_out & 1:  # Punto está a la izquierda del área de recorte
                x = xmin
                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
            elif code_out & 2:  # Punto está a la derecha del área de recorte
                x = xmax
                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
            elif code_out & 4:  # Punto está por debajo del área de recorte
                y = ymin
                x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
            elif code_out & 8:  # Punto está por encima del área de recorte
                y = ymax
                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)

            if code_out == code1:
                x1, y1 = x, y
                code1 = compute_code(x1, y1, xmin, ymin, xmax, ymax)
            else:
                x2, y2 = x, y
                code2 = compute_code(x2, y2, xmin, ymin, xmax, ymax)

    return accept, x1, y1, x2, y2

# Definir el área de recorte y el polígono
xmin, ymin, xmax, ymax = 30, 30, 70, 70
polygon = [(40, 40), (60, 80), (80, 50), (70, 30), (50, 50)]

# Crear la figura
fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)

# Función de animación
def animate(i):
    ax.clear()
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    # Dibujar el área de recorte
    rect = plt.Rectangle((xmin, ymin), xmax - xmin, ymax - ymin, fill=False)
    ax.add_patch(rect)

    # Dibujar el polígono original
    ax.plot(*zip(*polygon), marker='o', color='blue')

    # Recortar el polígono
    new_polygon = []
    for i in range(len(polygon)):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % len(polygon)]
        accept, new_x1, new_y1, new_x2, new_y2 = cohen_sutherland(x1, y1, x2, y2, xmin, ymin, xmax, ymax)
        if accept:
            new_polygon.append((new_x1, new_y1))
        new_polygon.append((new_x2, new_y2))

    # Dibujar el polígono recortado
    ax.plot(*zip(*new_polygon), marker='o', color='red')

# Crear la animación
ani = animation.FuncAnimation(fig, animate, frames=10, interval=500, blit=False)
plt.show()
