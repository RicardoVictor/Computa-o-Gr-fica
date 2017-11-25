import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def converte(valor):
    return int(valor[0:valor.find('/')])

def Objeto(arquivo, cor=None):
    if cor is None: 
        cor = (0.7, 0.7, 0.7)
    
    vertices = []
    faces_triangulares = []
    faces_quadriculares = []

    with open(arquivo) as meu_arquivo:
        for linha in meu_arquivo:
            valores = linha.split()

            if len(valores) == 4 and valores[0] == 'v':
                vertices.append((float(valores[1]), float(valores[2]), float(valores[3])))
            
            elif len(valores) == 4 and valores[0] == 'f':
                v1 = converte(valores[1]) - 1
                v2 = converte(valores[2]) - 1
                v3 = converte(valores[3]) - 1
                faces_triangulares.append((v1, v2, v3))

            elif len(valores) == 5 and valores[0] == 'f':
                v1 = converte(valores[1]) - 1
                v2 = converte(valores[2]) - 1
                v3 = converte(valores[3]) - 1
                v4 = converte(valores[4]) - 1
                faces_quadriculares.append((v1, v2, v3, v4))

    vertices = tuple(vertices)
    faces_triangulares = tuple(faces_triangulares)
    faces_quadriculares = tuple(faces_quadriculares)

    glBegin(GL_TRIANGLES)
    for face in faces_triangulares:
        glColor3fv(cor)
        for vertice in face:
            glVertex3fv(vertices[vertice])
    glEnd()
    
    glBegin(GL_QUADS)
    for face in faces_quadriculares:
        glColor3fv(cor)
        for vertice in face:
            glVertex3fv(vertices[vertice])
    glEnd()
    

def Cube():
    color = (0.7, 0.7, 0.7)

    vertices = (
        (1, -1, -1),
        (1, 1, -1),
        (-1, 1, -1),
        (-1, -1, -1),
        (1, -1, 1),
        (1, 1, 1),
        (-1, -1, 1),
        (-1, 1, 1)
    )

    faces = (
        (0, 1, 2, 3),
        (3, 2, 7, 6),
        (6, 7, 5, 4),
        (4, 5, 1, 0),
        (1, 5, 7, 2),
        (4, 0, 3, 6)
    )

    glBegin(GL_QUADS)
    for face in faces:
        glColor3fv(color)
        for vertex in face:
            glVertex3fv(vertices[vertex])

    glEnd()



pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

gluPerspective(50, (display[0]/display[1]), 0.1, 100.0)

#cubo 
#speaker
glTranslatef(0.0, 0.0, -5)

#microfone
'''glTranslatef(0.0, -130, -60)
'''
#ampeg
'''glTranslatef(0.0, 0.0, -5)
glScale(0.01, 0.01, 0.01)
'''
#todos
glRotatef(20, 0, 0, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    #glRotatef(1, 3, 1, 1)

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    Cube()
    #Objeto("objetos/Microphone.obj")
    pygame.display.flip()
    pygame.time.wait(1000)