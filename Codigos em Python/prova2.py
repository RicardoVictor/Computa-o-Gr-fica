from OpenGL import OpenGL
import Objeto
import Vertice
import Camera
import Screen
import Cenario
import Textura
import Pontual
import Spot
from numpy import array

def imprimeMatriz(matriz):
    for i in range(4):
        print('[', end="")
        for j in range(4):
            print('{:10.6f} '.format(matriz[i][j]), end="")
        print(']')
    print()

A = 3
B = 9
C = 7
D = 1
E = 9
F = 3

o = Objeto.Objeto()
o.addVertice(0, 0, 0)
o.addVertice(0, 0, 5)
o.addVertice(12, 0, 0)
o.addVertice(0, 8, 0)
o.imprimirVertices()

textura = Textura.Textura(0.8, 0.3, 0.2, 0.8, 0.3, 0.2, 0.8, 0.3, 0.2, 2)

o.addFace(o.vertices[0], o.vertices[1], o.vertices[3], textura)
o.addFace(o.vertices[0], o.vertices[3], o.vertices[2], textura)
o.addFace(o.vertices[0], o.vertices[2], o.vertices[1], textura)
o.addFace(o.vertices[1], o.vertices[2], o.vertices[3], textura)


'''Questao 1'''
Eye = Vertice.Vertice(0, 60, 0)
LookAt = Vertice.Vertice(D, E, F)
Vup = Vertice.Vertice(A, B, C)
camera = Camera.Camera(Eye, LookAt, Vup)
#camera = Camera.Camera(0, 55, 0, 100, 55, 0, 50, 70, 0)
print('i: ', camera.i)
print('j: ', camera.j)
print('k: ', camera.k)

WC = camera.matrizWC()
print('Matriz w->c')
imprimeMatriz(WC)

CW = camera.matrizCW()
print('Matriz c->w')
imprimeMatriz(CW)


'''Questao 2'''

'''o.aplica(WC)
o.imprimirVertices()'''

tela = Screen.Screen(3, 8, 8, 80, 80)
#tela.imprimirTela()
'''print(o.aura.centro.x)
print(o.aura.centro.y)
print(o.aura.centro.z)
print(o.aura.raio)'''

luz = Pontual.Pontual(-4, 6, -3, 0.9, 0.8, 1, 0.9, 0.8, 1)

cenario = Cenario.Cenario(0.5, 0.5, 0.5)
cenario.addObjeto(o)
cenario.addCamera(camera)
cenario.addScreen(tela)
cenario.addFonte(luz)
cenario.background_color = [4, 1, 2]
cores = cenario.ray_casting()

#imprime cores nao convertidas
'''for i in cores:
    print(i, cores[i])'''

'''Convertendo o RGB de cores para valores entre 0 e 1'''
max_value = -999999
#descobre maior valor
for i in cores:
    if(max_value < max(cores[i])):
        max_value = max(cores[i])
#converte cada valor com base no maior
for i in cores:
    cores[i] = array(cores[i]) * 255 / max_value
#imprime cores convertidas

for i in cores:
    print(i, cores[i])