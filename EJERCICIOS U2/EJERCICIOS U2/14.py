import matplotlib.pyplot as plt
import numpy as np

def plot_conic_section(a, b, conic_type='ellipse'):
    t = np.linspace(0, 2 * np.pi, 100)

    if conic_type == 'ellipse':
        x = a * np.cos(t)
        y = b * np.sin(t)
    elif conic_type == 'parabola':
        x = a * t
        y = b * t**2
    elif conic_type == 'hyperbola':
        x = a * np.cosh(t)
        y = b * np.sinh(t)

    plt.figure(figsize=(6, 6))
    plt.plot(x, y)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title(f'{conic_type.capitalize()} with a={a}, b={b}')
    plt.grid(True)
    plt.show()

a_ellipse = 3
b_ellipse = 2

a_parabola = 1
b_parabola = 1

a_hyperbola = 2
b_hyperbola = 3

plot_conic_section(a_ellipse, b_ellipse, conic_type='ellipse')
plot_conic_section(a_parabola, b_parabola, conic_type='parabola')
plot_conic_section(a_hyperbola, b_hyperbola, conic_type='hyperbola')
