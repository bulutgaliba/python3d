import OpenGL.GL as gl
import OpenGL.GLU as glu
import pygame
 
def draw_cube():
    # Küpün kenarlarının koordinatları
    vertices = ((-1, -1, -1),
                ( 1, -1, -1),
                ( 1,  1, -1),
                (-1,  1, -1),
                (-1, -1,  1),
                ( 1, -1,  1),
                ( 1,  1,  1),
                (-1,  1,  1))
 
    # Küpün yüzeylerinin belirlenmesi
    edges = ((0,1), (0,3), (0,4),
             (2,1), (2,3), (2,6),
             (5,1), (5,4), (5,6),
             (7,3), (7,4), (7,6))
 
    # Küpün kenarlarının çizilmesi
    gl.glBegin(gl.GL_LINES)
    for edge in edges:
        for vertex in edge:
            gl.glVertex3fv(vertices[vertex])
    gl.glEnd()
 
def main():
    # Ekran boyutu
    width, height = 800, 600
 
    # Pygame penceresi oluşturma
    pygame.init()
    pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
    pygame.display.set_caption("3D Küp")
 
    # Perspektif projeksiyonunun ayarlanması
    gl.glViewport(0, 0, width, height)
    gl.glMatrixMode(gl.GL_PROJECTION)
    glu.gluPerspective(45, width / height, 0.1, 50.0)
    gl.glMatrixMode(gl.GL_MODELVIEW)
    gl.glLoadIdentity()
    glu.gluLookAt(3, 3, 3, 0, 0, 0, 0, 1, 0)
 
    # Ana döngü
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
 
        # Ekranı temizleme
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
 
        # Küpün çizilmesi
        draw_cube()
 
        # Ekranı güncelleme
        pygame.display.flip()
 
if __name__ == '__main__':
    main()
