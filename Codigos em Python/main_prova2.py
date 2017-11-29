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
#P1
o.addVertice(A+10, B+5, 0)
#P2
o.addVertice(A+10+L, B+5, 0)
#P3
o.addVertice(A+10+L/2, B+5+ (L*3**0.5)/2, 0)
#P4
o.addVertice(A+10+L/2, B+5+ (L*3**0.5)/6, (L*6**0.5)/6)
#localizacao da fonte de luz
#o.addVertice(A+10, B+L, 2*L)
#ponto P
P = Vertice(A+10+L/2, B+5+ (L*3**0.5)/12, (L*3**0.5)/12)
#o.addVertice(A+10+L/2, B+5+ (L*3**0.5)/12, (L*3**0.5)/12)

o.imprimirVertices()

'''Questao 1'''

Eye = Vertice(A - 5, B + L, (L*6**0.5)/6)
print('eye:',Eye.x, Eye.y,Eye.z)
LookAt = Vertice(A+10+L/2, B+5+ (L*3**0.5)/6, 0)
print('look_at:',LookAt.x, LookAt.y,LookAt.z)
Avup = Vertice(A+10+L/2, B+5+ (L*3**0.5)/6, (L*6**0.5)/6)
print('Avup:',Avup.x, Avup.y, Avup.z)
camera = Camera(Eye, LookAt, Avup)

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

luz_x = 15.099987
luz_y = 50.898728
luz_z = -0.889703
luz = Pontual(luz_x, luz_y, luz_z, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7)

#ambiente
cenario = Cenario(0.4, 0.4, 0.4)
cenario.addObjeto(o)
cenario.addCamera(camera)
cenario.addScreen(tela)
cenario.addFonte(luz)
#cenario.background_color = [4, 1, 2]
cores = cenario.ray_casting()

#Cores nao convertidas
for i in cores:
    print(cores[i])

#descobre maior valor
max_value = -999999
for i in cores:
    if(max_value < max(cores[i])):
        max_value = max(cores[i])

#Cores em valores entre 0 e 1
for i in cores:
    cores[i] = array(cores[i]) / max_value
for i in cores:
    print(cores[i])

#Cores em valores entre 0 e 255
for i in cores:
    cores[i] = array(cores[i])*255
for i in cores:
    print(cores[i])


img = Image.new("RGB", (1, 1))

for i in cores:
    x = int(i[0:i.find(' ')])
    y = int(i[i.find(' ')+1:])
    img.putpixel((x, y), (int(cores[i][0]), int(cores[i][1]), int(cores[i][2])))

img.save("imagem.jpg")

print('\nQuestao 2')

P1_prod_esc_n = o.faces[2].P1.x * o.faces[2].normal[0] + o.faces[2].P1.y * o.faces[2].normal[1] + o.faces[2].P1.z * o.faces[2].normal[2]
Eye_prod_esc_n = Eye.x * o.faces[2].normal[0] + Eye.y * o.faces[2].normal[1] + Eye.z * o.faces[2].normal[2]
t_int = P1_prod_esc_n / Eye_prod_esc_n
P_int = Vertice(t_int * Eye.x, t_int * Eye.y, t_int * Eye.z)

l = [luz_x - P_int.x, luz_y - P_int.y, luz_z - P_int.z]
mod_l = (l[0]**2 + l[1]**2 + l[2]**2)**0.5
l[0] /= mod_l
l[1] /= mod_l
l[2] /= mod_l

r = []
l_prod_esc_n = l[0] * o.faces[2].normal[0] + l[1] * o.faces[2].normal[1] + l[2] * o.faces[2].normal[2]
r.append(2 * l_prod_esc_n * o.faces[2].normal[0] - l[0])
r.append(2 * l_prod_esc_n * o.faces[2].normal[1] - l[1])
r.append(2 * l_prod_esc_n * o.faces[2].normal[2] - l[2])

v = [Eye.x - P_int.x, Eye.y - P_int.y, Eye.z - P_int.z]
mod_v = (v[0]**2 + v[1]**2 + v[2]**2)**0.5
v[0] /= mod_l
v[1] /= mod_l
v[2] /= mod_l

m = 1

Iambiente_R = 0.4 * A/50
Iambiente_G = 0.4 * B/50
Iambiente_B = 0.4 * C/50

Idifusa_R = 0.7 * 3*A/50 * l_prod_esc_n
Idifusa_G = 0.7 * 3*B/50 * l_prod_esc_n
Idifusa_B = 0.7 * 3*C/50 * l_prod_esc_n

v_prod_esc_r = v[0] * r[0] + v[1] * r[1] + v[2] * r[2]
Iespecular_R = 0.7 * 3*A/50 * v_prod_esc_r ** m
Iespecular_G = 0.7 * 3*B/50 * v_prod_esc_r ** m
Iespecular_B = 0.7 * 3*C/50 * v_prod_esc_r ** m

I_R = Iambiente_R + Idifusa_R + Iespecular_R
I_G = Iambiente_G + Idifusa_G + Iespecular_G
I_B = Iambiente_B + Idifusa_B + Iespecular_B

print('cor(0/1):', I_R, I_G, I_B)
print('RGB:', I_R * 255, I_G * 255, I_B * 255)