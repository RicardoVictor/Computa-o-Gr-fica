from numpy import array
from PIL import Image
from transformacoes import *
from fontes import Pontual
from Screen import Screen
from Objeto import Objeto
from Vertice import Vertice
from Camera import Camera
from Cenario import Cenario
from Textura import Textura

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
L = A + B + C + D + E + F

o = Objeto()
o.addVertice(A+10, B+5, 0)
o.addVertice(A+10+L, B+5, 0)
o.addVertice(A+10+L/2, B+5+ (L*3**0.5)/2, 0)
o.addVertice(A+10+L/2, B+5+ (L*3**0.5)/6, (L*6**0.5)/6)
o.imprimirVertices()

#localizacao da fonte de luz
o.addVertice(A+10, B+L, 2*L)
# fonte de luz para P como look_at 44.975219  28.212050  -0.889703

#ponto P
#o.addVertice(A+10+L/2, B+5+ (L*3**0.5)/6, (L*6**0.5)/12)
#P em coodenadas de camera 5.508992   2.699248 -35.798526

'''Questao 1'''

Eye = Vertice(A - 5, B + L, (L*6**0.5)/6)
print('eye:',Eye.x, Eye.y,Eye.z)
LookAt = Vertice(A+10+L/2, B+5+ (L*3**0.5)/6, 0)
P = Vertice(A+10+L/2, B+5+ (L*3**0.5)/12, (L*3**0.5)/12)
print('P:',P.x, P.y,P.z)
print('look_at:',LookAt.x, LookAt.y,LookAt.z)
Vup = Vertice(A+10+L/2, B+5+ (L*3**0.5)/6, (L*6**0.5)/6)
print('Vup:',Vup.x, Vup.y,Vup.z)
camera = Camera(Eye, P, Vup)

print('ic: ', camera.i)
print('jc: ', camera.j)
print('kc: ', camera.k)

WC = camera.matrizWC()
print('Matriz w->c')
imprimeMatriz(WC)

CW = camera.matrizCW()

o.aplica(WC)
print('vertices em coordenada de camera')
o.imprimirVertices()

'''Questao 2'''

textura = Textura(A/50, B/50, C/50, 3*A/50, 3*B/50, 3*C/50, 3*A/50, 3*B/50, 3*C/50, 1)
print('textura: ',A/50, B/50, C/50, 3*A/50, 3*B/50, 3*C/50, 3*A/50, 3*B/50, 3*C/50, 1)
o.addFace(o.vertices[0], o.vertices[2], o.vertices[1], textura)
o.addFace(o.vertices[0], o.vertices[1], o.vertices[3], textura)
o.addFace(o.vertices[0], o.vertices[3], o.vertices[2], textura)
o.addFace(o.vertices[1], o.vertices[2], o.vertices[3], textura)

tela = Screen(10, 0.1, 0.1, 1, 1)
#tela.imprimirTela()
'''print(o.aura.centro.x)
print(o.aura.centro.y)
print(o.aura.centro.z)
print(o.aura.raio)'''

luz = Pontual(44.975219,  28.212050,  -0.889703, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7)

#ambiente
cenario = Cenario(0.4, 0.4, 0.4)
cenario.addObjeto(o)
cenario.addCamera(camera)
cenario.addScreen(tela)
cenario.addFonte(luz)
#cenario.background_color = [4, 1, 2]
cores = cenario.ray_casting()

#imprime cores nao convertidas
for i in cores:
    print(i, cores[i])

P0 = [A - 5, B + L, (L*6**0.5)/6]
P = [A+10+L/2, B+5+ (L*3**0.5)/6, (L*6**0.5)/12]


max_value = -999999
#descobre maior valor
for i in cores:
    if(max_value < max(cores[i])):
        max_value = max(cores[i])

'''Converte cores para valores entre 0 e 1'''
for i in cores:
    cores[i] = array(cores[i]) / max_value

for i in cores:
    print(i, cores[i])

'''Converte cores para valores entre 0 e 255'''
for i in cores:
    cores[i] = array(cores[i])*255

for i in cores:
    print(i, cores[i])


img = Image.new("RGB", (1, 1))

for i in cores:
    x = int(i[0:i.find(' ')])
    y = int(i[i.find(' ')+1:])
    img.putpixel((x, y), (int(cores[i][0]), int(cores[i][1]), int(cores[i][2])))

img.save("imagem.jpg")