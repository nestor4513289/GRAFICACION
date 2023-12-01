import matplotlib.pyplot as plt
import numpy as np

def draw_ellipse(a, b):
    t = np.linspace(0, 2*np.pi, 100)
    x = a * np.cos(t)
    y = b * np.sin(t)
    return x, y

def draw_hyperbola(a, b):
    t = np.linspace(-2, 2, 100)
    x = a * np.cosh(t)
    y = b * np.sinh(t)
    return x, y

def draw_parabola(a):
    x = np.linspace(-10, 10, 100)
    y = a * x**2
    return x, y

def plot_shape(x, y, title):
    plt.figure()
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
    plt.show()

while True:
    print("Selecciona una opción:")
    print("1. Dibujar elipse")
    print("2. Dibujar hipérbola")
    print("3. Dibujar parábola")
    print("4. Salir")
    
    opcion = input("Ingrese el número de la opción: ")
    
    if opcion == "1":
        a = float(input("Ingrese el valor de 'a' para la elipse: "))
        b = float(input("Ingrese el valor de 'b' para la elipse: "))
        x, y = draw_ellipse(a, b)
        plot_shape(x, y, 'Elipse')
    elif opcion == "2":
        a = float(input("Ingrese el valor de 'a' para la hipérbola: "))
        b = float(input("Ingrese el valor de 'b' para la hipérbola: "))
        x, y = draw_hyperbola(a, b)
        plot_shape(x, y, 'Hipérbola')
    elif opcion == "3":
        a = float(input("Ingrese el valor de 'a' para la parábola: "))
        x, y = draw_parabola(a)
        plot_shape(x, y, 'Parábola')
    elif opcion == "4":
        print("Saliendo...")
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")
