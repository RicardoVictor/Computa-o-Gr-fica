import Objeto
import Vertice
import Camera
import Janela
from numpy import dot, array

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

#Questao 1
S1 = o.escala(5*2**0.5/12, 5*2**0.5/8, 2**0.5)
o.aplica(S1)
o.imprimirVertices()

#Questao 2
T1 = o.translacao(-7.07106781187, 0 , 0)
R1 = o.rotacaoY(135)
R2 = o.rotacaoX(-35.264387)
R3 = o.rotacaoZ(40)
T2 = o.translacao(60, 50, 0)

o.aplica(T2 @ R3 @ R2 @ R1 @ T1)
o.imprimirVertices()

#Questao 3
T3 = o.translacao(-67.660444, -56.427876, 0)
E1 = o.espelhoQualquer(-5.685790, -1.002558, 4.082483, 0, 0, 0, -9.396926, 3.420202, 0)
T4 = o.translacao(67.660439, 56.427876, 0)

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

n = 8
m = 8
janela = Janela.Janela(30, 5, 5, n, m)
#janela.imprimirTela(n, m)
print(o.aura.centro.x)
print(o.aura.centro.y)
print(o.aura.centro.z)
print(o.aura.raio)

for i in range(n):    
    for j in range(m):
        A = janela.tela[i][j].x**2 + janela.tela[i][j].y**2 + janela.tela[i][j].z**2
        B = -2 * (janela.tela[i][j].x * o.aura.centro.x + janela.tela[i][j].y * o.aura.centro.y + janela.tela[i][j].z * o.aura.centro.z)
        C = o.aura.centro.x**2 + o.aura.centro.y**2 + o.aura.centro.z**2 - o.aura.raio**2
        if (B**2 - 4*A*C) >= 0:
            break
