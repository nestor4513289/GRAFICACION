import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x_box = np.array([0, 1, 1, 0, 0, 1, 1, 0])
y_box = np.array([0, 0, 1, 1, 0, 0, 1, 1])
z_box = np.array([0, 0, 0, 0, 1, 1, 1, 1])

ax.plot(x_box, y_box, z_box, color='blue')

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x_sphere = 0.5 * np.outer(np.cos(u), np.sin(v))
y_sphere = 0.5 * np.outer(np.sin(u), np.sin(v))
z_sphere = 0.5 * np.outer(np.ones(np.size(u)), np.cos(v))

ax.plot_surface(x_sphere, y_sphere, z_sphere, color='red')

ax.view_init(elev=20, azim=30) 

plt.show()
