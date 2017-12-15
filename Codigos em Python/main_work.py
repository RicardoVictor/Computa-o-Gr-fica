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


cubo = Objeto()
cubo.addVertice(1, -1, -1)
cubo.addVertice(1, 1, -1)
cubo.addVertice(-1, 1, -1)
cubo.addVertice(-1, -1, -1)
cubo.addVertice(1, -1, 1)
cubo.addVertice(1, 1, 1)
cubo.addVertice(-1, 1, 1)
cubo.addVertice(-1, -1, 1)

T_cubo = translacao(0, 0, -10)
cubo.aplica(T_cubo)

textura_cubo = Textura(0.3, 0, 0, 0.3, 0, 0, 0.5, 0.5, 0.5, 1)
cubo.addFace(cubo.vertices[0], cubo.vertices[2], cubo.vertices[1], textura_cubo)
cubo.addFace(cubo.vertices[0], cubo.vertices[3], cubo.vertices[2], textura_cubo)
cubo.addFace(cubo.vertices[4], cubo.vertices[5], cubo.vertices[6], textura_cubo)
cubo.addFace(cubo.vertices[4], cubo.vertices[6], cubo.vertices[7], textura_cubo)
cubo.addFace(cubo.vertices[2], cubo.vertices[3], cubo.vertices[6], textura_cubo)
cubo.addFace(cubo.vertices[2], cubo.vertices[7], cubo.vertices[6], textura_cubo)
cubo.addFace(cubo.vertices[0], cubo.vertices[1], cubo.vertices[5], textura_cubo)
cubo.addFace(cubo.vertices[0], cubo.vertices[5], cubo.vertices[4], textura_cubo)
cubo.addFace(cubo.vertices[1], cubo.vertices[2], cubo.vertices[6], textura_cubo)
cubo.addFace(cubo.vertices[1], cubo.vertices[6], cubo.vertices[5], textura_cubo)
cubo.addFace(cubo.vertices[0], cubo.vertices[4], cubo.vertices[7], textura_cubo)
cubo.addFace(cubo.vertices[0], cubo.vertices[7], cubo.vertices[3], textura_cubo)

Eye = Vertice(0.1, 0.1, 0.1)
LookAt = Vertice(0.1, 0.1, -20)
Avup = Vertice(0.1, 5, -10)
camera = Camera(Eye, LookAt, Avup)

cubo.aplica(camera.matrizWC())

tamanho = 100
tela = Screen(2, 5, 5, tamanho, tamanho)
luz = Pontual(5, 5, 5, 1, 1, 1, 0.5, 0.5, 0.5)

cenario = Cenario(1, 1, 1)
cenario.addObjeto(cubo)
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
        
img = Image.new("RGB", (tamanho, tamanho))

for i in cores:
    x = int(i[0:i.find(' ')])
    y = int(i[i.find(' ')+1:])
    img.putpixel((x, y), (int(cores[i][0]), int(cores[i][1]), int(cores[i][2])))

img.save("imagem.jpg")
