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

def piramide_triangular(textura):    
    piramide = Objeto()
    piramide.addVertice(0, 0, 0)
    piramide.addVertice(0, 0, 10)
    piramide.addVertice(10, 0, 0)
    piramide.addVertice(0, 10, 0)
    piramide.addFace(piramide.vertices[0], piramide.vertices[1], piramide.vertices[3], textura)
    piramide.addFace(piramide.vertices[0], piramide.vertices[3], piramide.vertices[2], textura)
    piramide.addFace(piramide.vertices[0], piramide.vertices[2], piramide.vertices[1], textura)
    piramide.addFace(piramide.vertices[1], piramide.vertices[2], piramide.vertices[3], textura)

    return piramide

def piramide_quadricular(textura):    
    piramide = Objeto()

    piramide.addVertice(0, 0, 0)
    piramide.addVertice(10, 0, 0)
    piramide.addVertice(10, 10, 0)
    piramide.addVertice(0, 10, 0)
    piramide.addVertice(5, 5, 5)

    vermelho = Textura(1, 0, 0, 1, 0, 0, 0.5, 0.5, 0.5, 1)
    verde =    Textura(0, 1, 0, 0, 1, 0, 0.5, 0.5, 0.5, 1)
    azul =     Textura(0, 0, 1, 0, 0, 1, 0.5, 0.5, 0.5, 1)
    amarelo =  Textura(1, 1, 0, 1, 1, 0, 0.5, 0.5, 0.5, 1)

    piramide.addFace(piramide.vertices[0], piramide.vertices[1], piramide.vertices[4], vermelho)
    piramide.addFace(piramide.vertices[1], piramide.vertices[2], piramide.vertices[4], verde)
    piramide.addFace(piramide.vertices[2], piramide.vertices[3], piramide.vertices[4], azul)
    piramide.addFace(piramide.vertices[0], piramide.vertices[4], piramide.vertices[3], amarelo)

    return piramide

textura = Textura(190, 120, 100, 170, 120, 100, 1, 1, 1, 2)
vermelho =  Textura(1, 0, 0, 1, 0, 0, 0.5, 0.5, 0.5, 1)
verde =     Textura(0, 1, 0, 0, 1, 0, 0.5, 0.5, 0.5, 1)
azul =      Textura(0, 0, 1, 0, 0, 1, 0.5, 0.5, 0.5, 1)
amarelo =   Textura(1, 1, 0, 1, 1, 0, 0.5, 0.5, 0.5, 1)
rosa =      Textura(1, 0, 1, 1, 0, 1, 0.5, 0.5, 0.5, 1)
ciano =     Textura(0, 1, 1, 0, 1, 1, 0.5, 0.5, 0.5, 1)

piramide1 = piramide_quadricular(textura)
piramide2 = piramide_quadricular(textura)
piramide3 = piramide_quadricular(textura)


T1 = translacao(-6, 0, 0)
piramide2.aplica(T1)

T2 = translacao(6, 0, 0)
piramide3.aplica(T2)

# visao de cima

eye = Vertice(5, 5, 10)
at =  Vertice(5, 5, 0)
up =  Vertice(5, 7, 0)

'''
eye = Vertice(5, -10, 0)
at =  Vertice(5, 0, 0)
up =  Vertice(5, -5, 5)
'''
camera = Camera(eye, at, up)

WC = camera.matrizWC()
piramide1.aplica(WC)
piramide2.aplica(WC)
piramide3.aplica(WC)

tamanho = 100
tela = Screen(1, 5, 5, tamanho, tamanho)
luz = Pontual(10, 30, 30, 1, 1, 1, 1, 1, 1)

cenario = Cenario(0.5, 0.5, 0.5)
#cenario.addObjeto(piramide2) # A DIREITA
#cenario.addObjeto(piramide3) # DA ESQUEDA
cenario.addObjeto(piramide1) # maior / meio
cenario.addCamera(camera)
cenario.addScreen(tela)
cenario.addFonte(luz)
#cenario.background_color = [100, 100, 200]
cores = renderizar(cenario)

#imprime dicionario de cores
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
    if(max_value != 0):
        cores[i] = array(cores[i])*255 / max_value
    else:
        cores[i] = [0, 0, 0]

img = Image.new("RGB", (tamanho, tamanho))

for i in cores:
    x = int(i[0:i.find(' ')])
    y = int(i[i.find(' ')+1:])
    img.putpixel((x, y), (int(cores[i][0]), int(cores[i][1]), int(cores[i][2])))

img.save("imagem.jpg")
