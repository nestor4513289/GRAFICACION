import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z1 = np.sin(np.sqrt(x**2 + y**2))
z2 = np.cos(np.sqrt(x**2 + y**2))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

surf1 = ax.plot_surface(x, y, z1, cmap='viridis')
surf2 = ax.plot_surface(x, y, z2, cmap='plasma')

ax.light_sources = [("directional", (1, 1, 1), (0.5, 0.5, 0.5))]
ax.set_box_aspect([1,1,1]) 

plt.show()
