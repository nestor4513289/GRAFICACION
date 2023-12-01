import tkinter as tk
from math import sqrt


def calcular_distancia(p1, p2):
    return sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)


def dibujar_punto(event):
    x, y = event.x, event.y
    canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill="black")
    puntos.append((x, y))
    if len(puntos) == 2:
        distancia = calcular_distancia(puntos[0], puntos[1])
        distancia_label.config(text=f"Distancia entre los puntos: {distancia:.2f} unidades")


root = tk.Tk()
root.title("Calculadora de Distancia entre Puntos")


canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()


distancia_label = tk.Label(root, text="Haz click para dibujar puntos")
distancia_label.pack()


puntos = []


canvas.bind("<Button-1>", dibujar_punto)


root.mainloop()
