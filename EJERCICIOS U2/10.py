import tkinter as tk

def draw_line(event):
    global start_x, start_y
    if start_x is None and start_y is None:
        start_x = event.x
        start_y = event.y
    else:
        canvas.create_line(start_x, start_y, event.x, event.y)
        start_x = None
        start_y = None

def clear_canvas():
    canvas.delete("all")

root = tk.Tk()
root.title("Dibujar líneas entre puntos")

canvas = tk.Canvas(root, width=600, height=400)
canvas.pack()

start_x = None
start_y = None

canvas.bind("<Button-1>", draw_line)

clear_button = tk.Button(root, text="Limpiar", command=clear_canvas)
clear_button.pack()

root.mainloop()
