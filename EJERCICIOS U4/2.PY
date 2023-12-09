import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np


vertices = np.array([
    [0, 0, 0],  
    [1, 0, 0],  
    [1, 1, 0],  
    [0, 1, 0],  
    [0.5, 0.5, 1]  
])


caras = [[vertices[0], vertices[1], vertices[4]],
         [vertices[1], vertices[2], vertices[4]],
         [vertices[2], vertices[3], vertices[4]],
         [vertices[3], vertices[0], vertices[4]],
         [vertices[0], vertices[1], vertices[2], vertices[3]]]

fig = plt.figure()

ax = fig.add_subplot(121, projection='3d')
ax.add_collection3d(Poly3DCollection(caras, facecolors='cyan', linewidths=1, edgecolors='black'))
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Proyección en perspectiva')

ax = fig.add_subplot(122)
for cara in caras:
    ax.plot([v[0] for v in cara + [cara[0]]], [v[1] for v in cara + [cara[0]]], 'cyan', linewidth=1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Proyección ortogonal')

plt.tight_layout()
plt.show()
