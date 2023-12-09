import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np

def main():

    if not glfw.init():
        return

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    window = glfw.create_window(800, 600, "Ventana OpenGL", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    vertices = np.array([
        -0.5, -0.5, 0.0,
         0.5, -0.5, 0.0,
         0.0,  0.5, 0.0
    ], dtype=np.float32)

    vertex_shader_source = """
    #version 330 core
    layout (location = 0) in vec3 aPos;
    void main()
    {
        gl_Position = vec4(aPos.x, aPos.y, aPos.z, 1.0);
    }
    """

    fragment_shader_source = """
    #version 330 core
    out vec4 FragColor;
    void main()
    {
        FragColor = vec4(1.0f, 0.5f, 0.2f, 1.0f);
    }
    """

    vertex_shader = OpenGL.GL.shaders.compileShader(vertex_shader_source, GL_VERTEX_SHADER)
    fragment_shader = OpenGL.GL.shaders.compileShader(fragment_shader_source, GL_FRAGMENT_SHADER)

    shader_program = OpenGL.GL.shaders.compileProgram(vertex_shader, fragment_shader)

    VAO = glGenVertexArrays(1)
    glBindVertexArray(VAO)

    VBO = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(GLfloat), None)
    glEnableVertexAttribArray(0)

    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)

    while not glfw.window_should_close(window):
        glfw.poll_events()

        glClearColor(0.2, 0.3, 0.3, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        glUseProgram(shader_program)
        glBindVertexArray(VAO)
        glDrawArrays(GL_TRIANGLES, 0, 3)

        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == "__main__":
    main()
