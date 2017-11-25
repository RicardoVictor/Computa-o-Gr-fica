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

def converte(valor):
    return int(valor[0:valor.find('/')])

obj = Objeto()
textura = Textura(210, 120, 100, 170, 120, 100, 1, 1, 1, 2)
arquivo = "objetos/Microphone.obj"

#Cria objeto a partide de um arquivo .obj
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


Eye = Vertice(0, 150, 20)
LookAt = Vertice(0, 150, -20)
Vup = Vertice(0, 170, 0)
camera = Camera(Eye, LookAt, Vup)

WC = camera.matrizWC()
obj.aplica(WC)

tamanho = 100
tela = Screen(10, 100, 100, tamanho, tamanho)
luz = Pontual(-10, 10, 50, 1, 1, 1, 1, 1, 1)

cenario = Cenario(0.5, 0.5, 0.5)
cenario.addObjeto(obj)
cenario.addCamera(camera)
cenario.addScreen(tela)
cenario.addFonte(luz)
#cenario.background_color = [100, 100, 200]
cores = cenario.ray_casting()

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
    cores[i] = array(cores[i])*255 / max_value
#imprime dicionario de cores convertidas
'''for i in cores:
    print(i, cores[i])
'''

img = Image.new("RGB", (tamanho, tamanho))

for i in cores:
    x = int(i[0:i.find(' ')])
    y = int(i[i.find(' ')+1:])
    img.putpixel((x, y), (int(cores[i][0]), int(cores[i][1]), int(cores[i][2])))

img.save("imagem.jpg")