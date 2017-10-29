from OpenGL import OpenGL
import Objeto
import Vertice
import Camera
import Screen
import Cenario

def imprimeMatriz(matriz):
    for i in range(4):
        print('[', end="")
        for j in range(4):
            print('{:10.6f} '.format(matriz[i][j]), end="")
        print(']')
    print()

o = Objeto.Objeto()
o.addVertice(0, 0, 0)
o.addVertice(0, 0, 5)
o.addVertice(12, 0, 0)
o.addVertice(0, 8, 0)
o.imprimirVertices()

o.addFace(o.vertices[0], o.vertices[1], o.vertices[3])
o.addFace(o.vertices[0], o.vertices[3], o.vertices[2])
o.addFace(o.vertices[0], o.vertices[2], o.vertices[1])
o.addFace(o.vertices[1], o.vertices[2], o.vertices[3])

print(o.faces[3].normal)

#Questao 1
S1 = OpenGL.escala(5*2**0.5/12, 5*2**0.5/8, 2**0.5)
o.aplica(S1)
o.imprimirVertices()

#Questao 2
T1 = OpenGL.translacao(-7.07106781187, 0 , 0)
R1 = OpenGL.rotacaoY(135)
R2 = OpenGL.rotacaoX(-35.264387)
R3 = OpenGL.rotacaoZ(40)
T2 = OpenGL.translacao(60, 50, 0)

o.aplica(T2 @ R3 @ R2 @ R1 @ T1)
o.imprimirVertices()

#Questao 3
T3 = OpenGL.translacao(-67.660444, -56.427876, 0)
E1 = OpenGL.espelhoQualquer(-5.685790, -1.002558, 4.082483, 0, 0, 0, -9.396926, 3.420202, 0)
T4 = OpenGL.translacao(67.660439, 56.427876, 0)

o.aplica(T4 @ E1 @ T3)
o.imprimirVertices()

#Eye = Vertice.Vertice(0, 60, 0)
#LookAt = Vertice.Vertice(100, 60, 0)
#Vup = Vertice.Vertice(50, 70, 0)
#camera = Camera.Camera(Eye, LookAt, Vup)
camera = Camera.Camera(0, 60, 0, 100, 60, 0, 50, 70, 0)
WC = camera.matrizWC()
print('Matriz w->c')
imprimeMatriz(WC)
o.aplica(WC)
o.imprimirVertices()

tela = Screen.Screen(30, 5, 5, 100, 100)
#tela.imprimirTela()
print(o.aura.centro.x)
print(o.aura.centro.y)
print(o.aura.centro.z)
print(o.aura.raio)

cenario = Cenario.Cenario()
cenario.addObjeto(o)
cenario.addCamera(camera)
cenario.addScreen(tela)
cenario.ray_casting()
