import tkinter as tk
from PIL import Image, ImageTk

ruta_imagen = 'C:\\Users\\nesto\\OneDrive\\Escritorio\\EJERCICIOS U2\\1.jpg' 
ventana = tk.Tk()
ventana.title("Mostrar imagen")

imagen = Image.open(ruta_imagen)
imagen = ImageTk.PhotoImage(imagen)

etiqueta_imagen = tk.Label(ventana, image=imagen)
etiqueta_imagen.pack()

ventana.mainloop()
