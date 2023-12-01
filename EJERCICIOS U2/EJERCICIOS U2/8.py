import matplotlib.pyplot as plt
import numpy as np


def ecuacion(x):
    return x ** 2 

x_vals = np.linspace(-10, 10, 100) 

y_vals = ecuacion(x_vals)

plt.figure(figsize=(8, 6))
plt.scatter(x_vals, y_vals, color='red', label='Puntos según ecuación')
plt.title('Gráfico de puntos según una ecuación')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()
plt.grid(True)
plt.show()
