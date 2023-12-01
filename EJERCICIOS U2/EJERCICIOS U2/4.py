import matplotlib.pyplot as plt

def onclick(event):
    
    x = event.xdata
    y = event.ydata
    
    
    print(f"Coordenadas: x = {x}, y = {y}")


fig, ax = plt.subplots()
ax.set_title('Sistema de Coordenadas')
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')


cid = fig.canvas.mpl_connect('button_press_event', onclick)


plt.show()
