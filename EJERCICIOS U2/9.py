import matplotlib.pyplot as plt
import numpy as np

num_puntos = 100

x = np.random.rand(num_puntos)
y = np.random.rand(num_puntos)

plt.scatter(x, y)
plt.title('Patrón de Puntos Aleatorios')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.show()
