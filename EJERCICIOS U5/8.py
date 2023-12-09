import glfw
from OpenGL.GL import *

def cambiar_color_fondo():
    glClearColor(2, 3, 0, 5) 
    glClear(GL_COLOR_BUFFER_BIT)


def main():
   
    if not glfw.init():
        return

    #
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

   
    window = glfw.create_window(800, 600, "Cambiar Color de Fondo OpenGL", None, None)
    if not window:
        glfw.terminate()
        return

   
    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        glfw.poll_events()

   
        cambiar_color_fondo()

    
        glfw.swap_buffers(window)

 
    glfw.terminate()

if __name__ == "__main__":
    main()
