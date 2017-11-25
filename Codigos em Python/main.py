from numpy import array
from PIL import Image
from OpenGL import OpenGL
import Objeto
import Vertice
import Camera
import Screen
import Cenario
import Textura
import Pontual
import Spot

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

textura1 = Textura.Textura(210, 120, 100, 170, 120, 100, 1, 1, 1, 2)
textura2 = Textura.Textura(190, 120, 100, 170, 120, 100, 1, 1, 1, 2)
textura3 = Textura.Textura(170, 120, 100, 170, 120, 100, 1, 1, 1, 2)
textura4 = Textura.Textura(150, 120, 100, 170, 120, 100, 1, 1, 1, 2)
o.addFace(o.vertices[0], o.vertices[1], o.vertices[3], textura2)
o.addFace(o.vertices[0], o.vertices[3], o.vertices[2], textura2)
o.addFace(o.vertices[0], o.vertices[2], o.vertices[1], textura2)
o.addFace(o.vertices[1], o.vertices[2], o.vertices[3], textura2)
#print(o.faces[3].normal)

#Questao 1
S1 = OpenGL.escala(5*2**0.5/12, 5*2**0.5/8, 2**0.5)
print('S1')
imprimeMatriz(S1)
o.aplica(S1)
print('vertices')
o.imprimirVertices()

#Questao 2
T1 = OpenGL.translacao(-7.07106781187, 0 , 0)
print('T1')
imprimeMatriz(T1)
R1 = OpenGL.rotacaoY(135)
print('R1')
imprimeMatriz(R1)
R2 = OpenGL.rotacaoX(-35.264387)
print('R2')
imprimeMatriz(R2)
R3 = OpenGL.rotacaoZ(40)
print('R3')
imprimeMatriz(R3)
'''T2 = OpenGL.translacao(60, 50, 0)
print('T2')
imprimeMatriz(T2)
'''
o.aplica(R3 @ R2 @ R1 @ T1)
print('vertices')
o.imprimirVertices()

#Questao 3
'''T3 = OpenGL.translacao(-67.660444, -56.427876, 0)
print('T3')
imprimeMatriz(T3)
E1 = OpenGL.espelhoQualquer(-5.685790, -1.002558, 4.082483, 0, 0, 0, -9.396926, 3.420202, 0)
print('E1')
imprimeMatriz(E1)
T4 = OpenGL.translacao(67.660439, 56.427876, 0)
print('T4')
imprimeMatriz(T4)

o.aplica(T4 @ E1 @ T3)
print('vertices')
o.imprimirVertices()'''

Eye = Vertice.Vertice(5, 5, 10)
LookAt = Vertice.Vertice(5, 5, 0)
Vup = Vertice.Vertice(5, 7, 2)
camera = Camera.Camera(Eye, LookAt, Vup)
#camera = Camera.Camera(0, 55, 0, 100, 55, 0, 50, 70, 0)
WC = camera.matrizWC()
print('Matriz w->c')
imprimeMatriz(WC)
o.aplica(WC)
o.imprimirVertices()

tela = Screen.Screen(3, 5, 5, 1000, 1000)
#tela.imprimirTela()
'''print(o.aura.centro.x)
print(o.aura.centro.y)
print(o.aura.centro.z)
print(o.aura.raio)'''

luz = Pontual.Pontual(10, 10, -5, 1, 1, 1, 1, 1, 1)

cenario = Cenario.Cenario(0.5, 0.5, 0.5)
cenario.addObjeto(o)
cenario.addCamera(camera)
cenario.addScreen(tela)
cenario.addFonte(luz)
#cenario.background_color = [100, 100, 200]
cores = cenario.ray_casting()

#imprime cores nao convertidas
'''for i in cores:
    print(i, cores[i])'''

'''Convertendo o RGB de cores para valores entre 0 e 255'''
max_value = -999999
#descobre maior valor
for i in cores:
    if(max_value < max(cores[i])):
        max_value = max(cores[i])
#converte cada valor com base no maior
for i in cores:
    cores[i] = array(cores[i])*255 / max_value
#imprime cores convertidas
'''for i in cores:
    print(i, cores[i])
'''
img = Image.new("RGB", (1000, 1000))

for i in cores:
    x = int(i[0:i.find(' ')])
    y = int(i[i.find(' ')+1:])
    img.putpixel((x, y), (int(cores[i][0]), int(cores[i][1]), int(cores[i][2])))

img.save("imagem.jpg")