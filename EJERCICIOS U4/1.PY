import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np


vertices = np.array([
    [0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],  
    [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]   
])


caras = [
    [vertices[0], vertices[1], vertices[2], vertices[3]],  
    [vertices[4], vertices[5], vertices[6], vertices[7]],  
    [vertices[0], vertices[1], vertices[5], vertices[4]],   
    [vertices[2], vertices[3], vertices[7], vertices[6]],  
    [vertices[1], vertices[2], vertices[6], vertices[5]],  
    [vertices[0], vertices[3], vertices[7], vertices[4]]   
]


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


cubo = Poly3DCollection(caras, alpha=0.25, linewidths=1, edgecolors='black')
ax.add_collection3d(cubo)


ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()


print("Coordenadas de los vértices del cubo:")
for i, v in enumerate(vertices):
    print(f"Vértice {i+1}: {v}")
