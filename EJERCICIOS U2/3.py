import tkinter as tk
from PIL import Image, ImageDraw


def start_paint(event):
   
    global last_x, last_y
    last_x, last_y = event.x, event.y

def paint(event):
   
    global last_x, last_y
    x, y = event.x, event.y

   
    canvas.create_line((last_x, last_y, x, y), fill="black", width=5)
    draw.line((last_x, last_y, x, y), fill="black", width=5)

   
    last_x, last_y = x, y


def save_image():
    filename = "dibujo.png"
    image.save(filename)
    print(f"Imagen guardada como {filename}")


root = tk.Tk()
root.title("Dibuja y guarda")


canvas_width = 400
canvas_height = 400
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()


image = Image.new("RGB", (canvas_width, canvas_height), "white")
draw = ImageDraw.Draw(image)


canvas.bind("<Button-1>", start_paint)
canvas.bind("<B1-Motion>", paint)


save_button = tk.Button(root, text="Guardar Imagen", command=save_image)
save_button.pack()


root.mainloop()
