import numpy as np
import math
import Vertice

class Objeto:
    __vertices = []
    
    def addVertice(self, x, y, z):
        vertice = Vertice.Vertice(x, y, z)
        self.__vertices.append(vertice)

    def imprimirVertices(self):
        for i in range(len(self.__vertices)):
            print("({:10.6f} {:10.6f} {:10.6f})".format(self.__vertices[i].getX(), self.__vertices[i].getY(), self.__vertices[i].getZ()))

    def aplica(self, matriz):
        for i in range(len(self.__vertices)):
            vertice = [self.__vertices[i].getX(), self.__vertices[i].getY(), self.__vertices[i].getZ(), 1]
            vertice = np.dot(matriz, vertice)

            self.__vertices[i].setX(vertice[0])
            self.__vertices[i].setY(vertice[1])
            self.__vertices[i].setZ(vertice[2])

    def escala(self, Sx, Sy, Sz):
        matriz = []
        for i in range(4):
            matriz.append([0]*4)

        matriz[0][0] = Sx
        matriz[1][1] = Sy
        matriz[2][2] = Sz
        matriz[3][3] = 1
        
        return matriz

    def rotacaoX(self, ang):
        matriz = []
        for i in range(4):
            matriz.append([0]*4)

        matriz[0][0] = 1
        matriz[1][1] = math.cos(math.radians(ang))
        matriz[1][2] = -math.sin(math.radians(ang))
        matriz[2][1] = math.sin(math.radians(ang))
        matriz[2][2] = math.cos(math.radians(ang))
        matriz[3][3] = 1

        return matriz
    
    def rotacaoY(self, ang):
        matriz = []
        for i in range(4):
            matriz.append([0]*4)

        matriz[0][0] = math.cos(math.radians(ang))
        matriz[1][1] = 1
        matriz[0][2] = math.sin(math.radians(ang))
        matriz[2][0] = -math.sin(math.radians(ang))
        matriz[2][2] = math.cos(math.radians(ang))
        matriz[3][3] = 1

        return matriz

    def rotacaoZ(self, ang):
        matriz = []
        for i in range(4):
            matriz.append([0]*4)

        matriz[0][0] = math.cos(math.radians(ang))
        matriz[0][1] = -math.sin(math.radians(ang))
        matriz[1][0] = math.sin(math.radians(ang))
        matriz[1][1] = math.cos(math.radians(ang))
        matriz[2][2] = 1
        matriz[3][3] = 1

        return matriz
    
    def translacao(self, Tx, Ty, Tz):
        matriz = []
        for i in range(4):
            matriz.append([0]*4)

        matriz[0][3] = Tx
        matriz[1][3] = Ty
        matriz[2][3] = Tz
        matriz[0][0] = 1
        matriz[1][1] = 1
        matriz[2][2] = 1
        matriz[3][3] = 1

        return matriz

    def espelhoYZ(self):
        matriz = []
        for i in range(4):
            matriz.append([0]*4)

        matriz[0][0] = -1
        matriz[1][1] = 1
        matriz[2][2] = 1
        matriz[3][3] = 1

        return matriz   

    def espelhoXZ(self):
        matriz = []
        for i in range(4):
            matriz.append([0]*4)

        matriz[0][0] = 1
        matriz[1][1] = -1
        matriz[2][2] = 1
        matriz[3][3] = 1

        return matriz   

    def espelhoXY(self):
        matriz = []
        for i in range(4):
            matriz.append([0]*4)

        matriz[0][0] = 1
        matriz[1][1] = 1
        matriz[2][2] = -1
        matriz[3][3] = 1

        return matriz    

    def cisalhamentoYX(self, ang):
        matriz = []
        for i in range(4):
            matriz.append([0]*4)

        matriz[0][1] = math.tan(math.radians(ang))
        matriz[0][0] = 1
        matriz[1][1] = 1
        matriz[2][2] = 1
        matriz[3][3] = 1

        return matriz 

    def cisalhamentoXY(self, ang):
        matriz = []
        for i in range(4):
            matriz.append([0]*4)

        matriz[1][0] = math.tan(math.radians(ang))
        matriz[0][0] = 1
        matriz[1][1] = 1
        matriz[2][2] = 1
        matriz[3][3] = 1

        return matriz 

    def cisalhamentoZY(self, ang):
        matriz = []
        for i in range(4):
            matriz.append([0]*4)

        matriz[1][2] = math.tan(math.radians(ang))
        matriz[0][0] = 1
        matriz[1][1] = 1
        matriz[2][2] = 1
        matriz[3][3] = 1

        return matriz 

    def cisalhamentoYZ(self, ang):
        matriz = []
        for i in range(4):
            matriz.append([0]*4)

        matriz[2][1] = math.tan(math.radians(ang))
        matriz[0][0] = 1
        matriz[1][1] = 1
        matriz[2][2] = 1
        matriz[3][3] = 1

        return matriz 

    def cisalhamentoZX(self, ang):
        matriz = []
        for i in range(4):
            matriz.append([0]*4)

        matriz[0][2] = math.tan(math.radians(ang))
        matriz[0][0] = 1
        matriz[1][1] = 1
        matriz[2][2] = 1
        matriz[3][3] = 1

        return matriz 

    def cisalhamentoXZ(self, ang):
        matriz = []
        for i in range(4):
            matriz.append([0]*4)

        matriz[2][0] = math.tan(math.radians(ang))
        matriz[0][0] = 1
        matriz[1][1] = 1
        matriz[2][2] = 1
        matriz[3][3] = 1

        return matriz 

    def espelhoQualquer(self, x1, y1, z1, x2, y2, z2, x3, y3, z3):
        #normal
        normal = []
        normal.append((y2 - y1)*(z3 - z1) - (z2 - z1)*(y3 - y1))
        normal.append((z2 - z1)*(x3 - x1) - (x2 - x1)*(z3 - z1))
        normal.append((x2 - x1)*(y3 - y1) - (y2 - y1)*(x3 - x1))
        normal.append(0)

        #normaliza
        modulo = (normal[0]*normal[0] + normal[1]*normal[1] + normal[2]*normal[2]) ** (1/2)
        for i in range(4):
            normal[i] /= modulo

        matriz = []
        for i in range(4):
            matriz.append([0]*4)

        for i in range(4):
            for j in range(4):
                if i==j:
                    matriz[i][j] = 1

        for i in range(4):
            for j in range(4):
                matriz[i][j] -= 2 * normal[i] * normal[j]
        
        return matriz

    def rotacaoQualquer(self, ang, x1, y1, z1, x2, y2, z2):
        ang /= 2

        #vetor U
        qu = []
        qu.append(x2 - x1)
        qu.append(y2 - y1)
        qu.append(z2 - z1)

        #modulo de U
        modulo = (qu[0]*qu[0] + qu[1]*qu[1] + qu[2]*qu[2])**0.5

        #U/|U|
        for i in range(3):
            qu[i] /= modulo
        
        #qu
        for i in range(3):
            qu[i] *= math.sin(math.radians(ang))
        qu.append(math.cos(math.radians(ang)))

        matriz = []
        for i in range(4):
            matriz.append([0]*4)

        matriz[0][0] = qu[3]**2 + qu[0]**2 - qu[1]**2 - qu[2]**2
        matriz[0][1] = 2*(qu[0]*qu[1]) - 2*(qu[2]*qu[3])
        matriz[0][2] = 2*(qu[0]*qu[2]) + 2*(qu[1]*qu[3])
        matriz[0][3] = 0
        matriz[1][0] = 2*(qu[0]*qu[1]) + 2*(qu[2]*qu[3])
        matriz[1][1] = qu[3]**2 + qu[0]**2 + qu[1]**2 - qu[2]**2
        matriz[1][2] = 2*(qu[1]*qu[2]) - 2*(qu[0]*qu[3])
        matriz[1][3] = 0
        matriz[2][0] = 2*(qu[0]*qu[2]) - 2*(qu[1]*qu[3])
        matriz[2][1] = 2*(qu[2]*qu[1]) + 2*(qu[0]*qu[3])
        matriz[2][2] = qu[3]**2 - qu[0]**2 - qu[1]**2 + qu[2]**2
        matriz[2][3] = 0
        matriz[3][0] = 0
        matriz[3][1] = 0
        matriz[3][2] = 0
        matriz[3][3] = qu[3]**2 + qu[0]**2 + qu[1]**2 + qu[2]**2
        
        return matriz