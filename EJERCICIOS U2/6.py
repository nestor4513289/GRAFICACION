import matplotlib.pyplot as plt

def graficar_puntos(coordenadas):
    x = [coordenada[0] for coordenada in coordenadas]
    y = [coordenada[1] for coordenada in coordenadas]

    plt.scatter(x, y)
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.title('Gráfico de Coordenadas')
    plt.grid(True)
    plt.show()

def ingresar_coordenadas():
    coordenadas = []
    while True:
        coordenada = input("Ingresa las coordenadas en formato 'x,y' (o escribe 'fin' para terminar): ")
        if coordenada.lower() == 'fin':
            break
        try:
            x, y = map(float, coordenada.split(','))
            coordenadas.append((x, y))
        except ValueError:
            print("Formato incorrecto. Introduce las coordenadas en el formato 'x,y'.")

    return coordenadas


print("Ingresa las coordenadas. Cuando hayas terminado, escribe 'fin'.")
puntos = ingresar_coordenadas()


if puntos:
    graficar_puntos(puntos)
else:
    print("No se han ingresado coordenadas para graficar.")
