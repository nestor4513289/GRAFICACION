def encontrar_interseccion(m1, b1, m2, b2):
    if m1 == m2:
        if b1 == b2:
            return f"Ambas líneas son la misma: y = {m1}x + {b1}"
        else:
            return "Las líneas son paralelas y no se intersectan."
    else:
        x = (b2 - b1) / (m1 - m2)
        y = m1 * x + b1
        return f"Las líneas se intersectan en el punto ({x}, {y})"

m1 = 5
b1 = 3
m2 = -2
b2 = 4

resultado = encontrar_interseccion(m1, b1, m2, b2)
print(resultado)
