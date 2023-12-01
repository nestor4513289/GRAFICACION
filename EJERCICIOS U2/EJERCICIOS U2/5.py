import tkinter as tk

class TransformApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Transformaciones Gráficas")

        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()

        self.circle = self.canvas.create_oval(150, 150, 250, 250, fill="blue")  

        self.translation_button = tk.Button(root, text="Trasladar", command=self.translate)
        self.translation_button.pack()

    def translate(self):
        self.canvas.move(self.circle, 50, 50)  
def main():
    root = tk.Tk()
    app = TransformApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
