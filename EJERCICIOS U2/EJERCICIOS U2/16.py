import tkinter as tk

def paint(event):
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    canvas.create_oval(x1, y1, x2, y2, fill=current_color.get(), outline='')

def fill_color(event):
    start_color = canvas.getpixel((event.x, event.y))
    target_color = current_color.get()
    if start_color != target_color:
        flood_fill(event.x, event.y, start_color, target_color)

def flood_fill(x, y, start_color, target_color):
    stack = [(x, y)]

    while stack:
        x, y = stack.pop()

        if canvas.getpixel((x, y)) == start_color:
            canvas.put(target_color, (x, y))

            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < canvas.winfo_width() and 0 <= ny < canvas.winfo_height():
                    stack.append((nx, ny))

def change_color(color):
    current_color.set(color)

root = tk.Tk()
root.title("Paint App")

current_color = tk.StringVar(root, "black")

canvas = tk.Canvas(root, width=600, height=400, bg='white')
canvas.pack(expand=True, fill=tk.BOTH)

colors = ["red", "green", "blue", "yellow", "black", "white"]
for i, color in enumerate(colors):
    tk.Button(root, bg=color, command=lambda c=color: change_color(c)).pack(side=tk.LEFT)

canvas.bind("<B1-Motion>", paint)
canvas.bind("<Button-1>", fill_color)

root.mainloop()
