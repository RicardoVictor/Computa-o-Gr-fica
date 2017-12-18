import pygame
from numpy import array
from PIL import Image
from transformacoes import *
from fontes import Pontual
from screen import Screen
from objeto import Objeto
from vertice import Vertice
from camera import Camera
from cenario import Cenario
from textura import Textura
from ray_casting import renderizar


def imprimeMatriz(matriz):
    for i in range(4):
        print('[', end="")
        for j in range(4):
            print('{:10.6f} '.format(matriz[i][j]), end="")
        print(']')
    print()
    
def converte(valor):
    return int(valor[0:valor.find('/')])

#Cria objeto a partide de um arquivo .obj
def objeto(arquivo, textura):
    obj = Objeto()
    with open(arquivo) as meu_arquivo:
        for linha in meu_arquivo:
            valores = linha.split()
            
            if len(valores) == 4 and valores[0] == 'v':
                obj.addVertice(float(valores[1]), float(valores[2]), float(valores[3]))
            
            elif len(valores) == 4 and valores[0] == 'f':
                P1 = converte(valores[1]) - 1
                P2 = converte(valores[2]) - 1
                P3 = converte(valores[3]) - 1
                obj.addFace(obj.vertices[P1], obj.vertices[P2], obj.vertices[P3], textura)
            
            elif len(valores) == 5 and valores[0] == 'f':
                P1 = converte(valores[1]) - 1
                P2 = converte(valores[2]) - 1
                P3 = converte(valores[3]) - 1
                P4 = converte(valores[4]) - 1
                obj.addFace(obj.vertices[P1], obj.vertices[P2], obj.vertices[P3], textura)
                obj.addFace(obj.vertices[P1], obj.vertices[P3], obj.vertices[P4], textura)
    
    return obj


piramide = Objeto()
piramide.addVertice(0, 0, 0)
piramide.addVertice(0, 0, 5)
piramide.addVertice(12, 0, 0)
piramide.addVertice(0, 8, 0)

marron =  Textura(190, 120, 100, 170, 120, 100, 1, 1, 1, 2)
vermelho = Textura(1, 0, 0, 1, 0, 0, 0.5, 0.5, 0.5, 1)
verde =    Textura(0, 1, 0, 0, 1, 0, 0.5, 0.5, 0.5, 1)
azul =     Textura(0, 0, 1, 0, 0, 1, 0.5, 0.5, 0.5, 1)
amarelo =  Textura(1, 1, 0, 1, 1, 0, 0.5, 0.5, 0.5, 1)
rosa =     Textura(1, 0, 1, 1, 0, 1, 0.5, 0.5, 0.5, 1)
ciano =    Textura(0, 1, 1, 0, 1, 1, 0.5, 0.5, 0.5, 1)
branco =    Textura(0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.5, 0.5, 0.5, 1)
preto =    Textura(0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.5, 0.5, 0.5, 1)
piramide.addFace(piramide.vertices[0], piramide.vertices[1], piramide.vertices[3], marron)
piramide.addFace(piramide.vertices[0], piramide.vertices[3], piramide.vertices[2], marron)
piramide.addFace(piramide.vertices[0], piramide.vertices[2], piramide.vertices[1], marron)
piramide.addFace(piramide.vertices[1], piramide.vertices[2], piramide.vertices[3], marron)

S1 = escala(5*2**0.5/12, 5*2**0.5/8, 2**0.5)
T1 = translacao(-7.07106781187, 0 , 0)
R1 = rotacaoY(135)
R2 = rotacaoX(-35.264387)
R3 = rotacaoZ(40)

piramide.aplica(R3 @ R2 @ R1 @ T1 @ S1)

Eye = Vertice(5, 5, 10)
LookAt = Vertice(5, 5, 0)
Avup = Vertice(5, 7, 2)
camera = Camera(Eye, LookAt, Avup)

piramide.aplica(camera.matrizWC())

tamanho = 200
tela = Screen(3, 5, 5, tamanho, tamanho)
luz = Pontual(10, 10, 5, 1, 1, 1, 0.5, 0.5, 0.5)

cenario = Cenario(1, 1, 1)
cenario.addObjeto(piramide)
cenario.addCamera(camera)
cenario.addScreen(tela)
cenario.addFonte(luz)
#cenario.background_color = [100, 100, 200]
cores = renderizar(cenario)

'''Convertendo o RGB de cores para valores entre 0 e 255'''
max_value = -999999
#descobre maior valor
for i in cores:
    if(max_value < max(cores[i])):
        max_value = max(cores[i])

#converte cada valor com base no maior
for i in cores:
    if(max_value != 0):
        cores[i] = array(cores[i])*255 / max_value
    else:
        cores[i] = [0, 0, 0]


''' IMAGEM '''

img = Image.new("RGB", (tamanho, tamanho))

for i in cores:
    x = int(i[0:i.find(' ')])
    y = int(i[i.find(' ')+1:])
    img.putpixel((x, y), (int(cores[i][0]), int(cores[i][1]), int(cores[i][2])))
  
img.save("imagem.jpg")


''' PYGAME '''

width = tamanho
height = tamanho
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

while True:
    for i in cores:
        x = int(i[0:i.find(' ')])
        y = int(i[i.find(' ')+1:])
        screen.set_at((x, y), (int(cores[i][0]), int(cores[i][1]), int(cores[i][2])))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.flip()
    clock.tick(240)