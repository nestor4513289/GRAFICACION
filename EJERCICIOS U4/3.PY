import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

displacement = 0.2
x_left = x - displacement
x_right = x + displacement

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

ax1.imshow(z, cmap='viridis')
ax1.set_title('Imagen izquierda')

ax2.imshow(z, cmap='viridis')
ax2.set_title('Imagen derecha')

ax1.imshow(z, extent=(x.min(), x.max(), y.min(), y.max()), cmap='viridis', alpha=0.7, origin='lower')
ax2.imshow(z, extent=(x.min(), x.max(), y.min(), y.max()), cmap='viridis', alpha=0.7, origin='lower')

plt.show()
