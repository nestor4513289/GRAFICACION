import matplotlib.pyplot as plt

# Coordenadas del polígono (en este caso, un triángulo)
x = [1, 3, 2]  # Coordenadas x
y = [1, 1, 4]  # Coordenadas y

# Dibujar el polígono
plt.figure(figsize=(6, 6))
plt.plot(x + [x[0]], y + [y[0]], marker='o')  # Agregar el primer punto al final para cerrar el polígono
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Polígono con coordenadas conocidas')
plt.grid(True)
plt.show()