import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Crear una figura y ejes
fig, ax = plt.subplots()

# Definir los puntos del cuadrado
x = [1, 1, 3, 3, 1]  # Coordenadas x de los vértices
y = [1, 3, 3, 1, 1]  # Coordenadas y de los vértices

# Dibujar el cuadrado
ax.plot(x, y, 'b')  # Dibujar líneas entre los puntos

# Mostrar el cuadrado en el plano cartesiano
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Cuadrado en el plano cartesiano')
plt.grid(True)
plt.axis('equal')  # Para que los ejes tengan la misma escala

plt.show()
