import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def update(frame):
    a = 1.0 + np.sin(frame * 0.1)  
    b = 0.8 + np.cos(frame * 0.1)  
    ellipse.set_width(a * 2)
    ellipse.set_height(b * 2)
    return ellipse,

fig, ax = plt.subplots()
ax.set_aspect('equal')

ellipse = plt.Rectangle((0, 0), 0, 0, fc='blue', alpha=0.5)
ax.add_patch(ellipse)

ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

ani = animation.FuncAnimation(fig, update, frames=200, interval=50)

plt.show()
