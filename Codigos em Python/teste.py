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

o = Objeto()
o.addVertice(0, 0, 0)
o.addVertice(0, 0, 5)
o.addVertice(12, 0, 0)
o.addVertice(0, 8, 0)
o.imprimirVertices()

textura = Textura(210, 120, 100, 170, 120, 100, 1, 1, 1, 2)

o.addFace(o.vertices[0], o.vertices[1], o.vertices[3], textura)
o.addFace(o.vertices[0], o.vertices[3], o.vertices[2], textura)
o.addFace(o.vertices[0], o.vertices[2], o.vertices[1], textura)
o.addFace(o.vertices[1], o.vertices[2], o.vertices[3], textura)

S1 = escala(5*2**0.5/12, 5*2**0.5/8, 2**0.5)
T1 = translacao(-7.07106781187, 0 , 0)
R1 = rotacaoY(135)
R2 = rotacaoX(-35.264387)
R3 = rotacaoZ(40)

o.aplica(R3 @ R2 @ R1 @ T1 @ S1)


Eye = Vertice(5, 5, 10)
LookAt = Vertice(5, 5, 0)
Vup = Vertice(5, 7, 2)
camera = Camera(Eye, LookAt, Vup)

WC = camera.matrizWC()

o.aplica(WC)

tamanho = 100
tela = Screen(3, 5, 5, tamanho, tamanho)

luz = Pontual(10, 10, -5, 1, 1, 1, 1, 1, 1)
cenario = Cenario(0.5, 0.5, 0.5)
cenario.addObjeto(o)
cenario.addCamera(camera)
cenario.addScreen(tela)
cenario.addFonte(luz)
cenario.background_color = [0, 0, 0]
cores = cenario.ray_casting()

'''Convertendo o RGB de cores para valores entre 0 e 255'''
max_value = -999999
#descobre maior valor
for i in cores:
    if(max_value < max(cores[i])):
        max_value = max(cores[i])

#converte cada valor com base no maior
for i in cores:
    cores[i] = array(cores[i])*255 / max_value


#Setar cor em uma tela do Qt ou pygame
for cor in cores:
    #posicao
    x = int(i[0:i.find(' ')])
    y = int(i[i.find(' ')+1:])
    
    #RGB da cor
    r = int(cores[cor][0])
    g = int(cores[cor][1])
    b = int(cores[cor][2])

    rgb_color = (r, g, b)
    
