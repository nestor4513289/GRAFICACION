import matplotlib.pyplot as plt

# Coordenadas de los vértices del triángulo
x = [0, 1, 0]  # coordenadas x
y = [0, 0, 1]  # coordenadas y

# Dibujar el triángulo
plt.figure()
plt.plot(x, y, marker='o')  # 'marker' define el tipo de marcador en los vértices
plt.title('Triángulo en el plano cartesiano')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.grid(True)
plt.axis('equal')  # Establece la misma escala en ambos ejes para que se vea como un triángulo

# Mostrar el gráfico
plt.show()