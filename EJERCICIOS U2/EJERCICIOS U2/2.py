import tkinter as tk

def draw_circle(event):
    x, y = event.x, event.y
    canvas.create_oval(x - 20, y - 20, x + 20, y + 20, outline="blue")

def draw_rectangle(event):
    x, y = event.x, event.y
    canvas.create_rectangle(x - 20, y - 20, x + 20, y + 20, outline="red")

def draw_line(event):
    x, y = event.x, event.y
    canvas.create_line(x - 20, y - 20, x + 20, y + 20, fill="green")

root = tk.Tk()
root.title("Dibujar Formas Geométricas")

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

canvas.bind("<Button-1>", draw_circle)
canvas.bind("<Button-2>", draw_rectangle)
canvas.bind("<Button-3>", draw_line)

root.mainloop()
