from transformacoes import *
from objeto import Objeto

def imprimeMatriz(matriz):
    for i in range(4):
        print('[', end="")
        for j in range(4):
            print('{:10.6f} '.format(matriz[i][j]), end="")
        print(']')
    print()


o = Objeto()
o.addVertice(0, 0, 0)
o.addVertice(0, 0, 5)
o.addVertice(12, 0, 0)
o.addVertice(0, 8, 0)
o.imprimirVertices()

#Questao 1
S1 = escala(5*2**0.5/12, 5*2**0.5/8, 2**0.5)
print('S1')
imprimeMatriz(S1)
o.aplica(S1)
print('vertices')
o.imprimirVertices()

#Questao 2
T1 = translacao(-7.07106781187, 0 , 0)
print('T1')
imprimeMatriz(T1)
R1 = rotacaoY(135)
print('R1')
imprimeMatriz(R1)
R2 = rotacaoX(-35.264387)
print('R2')
imprimeMatriz(R2)
R3 = rotacaoZ(40)
print('R3')
imprimeMatriz(R3)
T2 = translacao(60, 50, 0)
print('T2')
imprimeMatriz(T2)

o.aplica(R3 @ R2 @ R1 @ T1)
print('vertices')
o.imprimirVertices()

#Questao 3
T3 = translacao(-67.660444, -56.427876, 0)
print('T3')
imprimeMatriz(T3)
E1 = espelhoQualquer(-5.685790, -1.002558, 4.082483, 0, 0, 0, -9.396926, 3.420202, 0)
print('E1')
imprimeMatriz(E1)
T4 = translacao(67.660439, 56.427876, 0)
print('T4')
imprimeMatriz(T4)

o.aplica(T4 @ E1 @ T3)
print('vertices')
o.imprimirVertices()
