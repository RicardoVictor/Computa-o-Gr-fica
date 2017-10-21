import Objeto
from numpy import dot, array

def imprimirMatriz(matriz):
    for i in range(4):
        for j in range(4):
            print('{:10.6f} '.format(matriz[i][j]), end="")
        print()
'''
o = Objeto.Objeto()
o.addVertice(0, 0, 0)
o.addVertice(0, 0, 5)
o.addVertice(12, 0, 0)
o.addVertice(0, 8, 0)
o.imprimirVertices()
print()

#Questao 1
S1 = o.escala(5*2**0.5/12, 5*2**0.5/8, 2**0.5)
o.aplica(S1)
o.imprimirVertices()
print()

#Questao 2
T1 = o.translacao(-7.07106781187, 0 , 0)
R1 = o.rotacaoY(135)
R2 = o.rotacaoX(-35.264387)
R3 = o.rotacaoZ(40)
T2 = o.translacao(60, 50, 0)

o.aplica(T2 @ R3 @ R2 @ R1 @ T1)
o.imprimirVertices()
print()

#Questao 3
T3 = o.translacao(-67.660444, -56.427876, 0)
E1 = o.espelhoQualquer(-5.685790, -1.002558, 4.082483, 0, 0, 0, -9.396926, 3.420202, 0)
T4 = o.translacao(67.660439, 56.427876, 0)

o.aplica(T4 @ E1 @ T3)
o.imprimirVertices()
'''

