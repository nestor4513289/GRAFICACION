import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


x = np.array([1, 1, -1, -1, 1, 1, -1, -1])
y = np.array([1, -1, -1, 1, 1, -1, -1, 1])
z = np.array([1, 1, 1, 1, -1, -1, -1, -1])

fig = plt.figure()


ax = fig.add_subplot(121, projection='3d')
ax.set_title('Proyección de perspectiva')
ax.plot(x, y, z)


ax = fig.add_subplot(122, projection='3d')
ax.set_title('Proyección ortográfica')
ax.plot(x, y, z)
ax.view_init(azim=0, elev=90)  

plt.show()
