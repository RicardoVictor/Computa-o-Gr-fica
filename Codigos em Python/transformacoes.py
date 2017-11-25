from numpy import array
import math

def escala(Sx, Sy, Sz):
    matriz = [[0]*4 for i in range(4)]

    matriz[0][0] = Sx
    matriz[1][1] = Sy
    matriz[2][2] = Sz
    matriz[3][3] = 1
    
    return array(matriz)

def rotacaoX(ang):
    matriz = [[0]*4 for i in range(4)]

    matriz[0][0] = 1
    matriz[1][1] = math.cos(math.radians(ang))
    matriz[1][2] = -math.sin(math.radians(ang))
    matriz[2][1] = math.sin(math.radians(ang))
    matriz[2][2] = math.cos(math.radians(ang))
    matriz[3][3] = 1

    return array(matriz)

def rotacaoY(ang):
    matriz = [[0]*4 for i in range(4)]

    matriz[0][0] = math.cos(math.radians(ang))
    matriz[1][1] = 1
    matriz[0][2] = math.sin(math.radians(ang))
    matriz[2][0] = -math.sin(math.radians(ang))
    matriz[2][2] = math.cos(math.radians(ang))
    matriz[3][3] = 1

    return array(matriz)

def rotacaoZ(ang):
    matriz = [[0]*4 for i in range(4)]

    matriz[0][0] = math.cos(math.radians(ang))
    matriz[0][1] = -math.sin(math.radians(ang))
    matriz[1][0] = math.sin(math.radians(ang))
    matriz[1][1] = math.cos(math.radians(ang))
    matriz[2][2] = 1
    matriz[3][3] = 1

    return array(matriz)

def translacao(Tx, Ty, Tz):
    matriz = [[0]*4 for i in range(4)]

    matriz[0][3] = Tx
    matriz[1][3] = Ty
    matriz[2][3] = Tz
    matriz[0][0] = 1
    matriz[1][1] = 1
    matriz[2][2] = 1
    matriz[3][3] = 1

    return array(matriz)

def espelhoYZ():
    matriz = [[0]*4 for i in range(4)]

    matriz[0][0] = -1
    matriz[1][1] = 1
    matriz[2][2] = 1
    matriz[3][3] = 1

    return array(matriz)   

def espelhoXZ():
    matriz = [[0]*4 for i in range(4)]

    matriz[0][0] = 1
    matriz[1][1] = -1
    matriz[2][2] = 1
    matriz[3][3] = 1

    return array(matriz) 

def espelhoXY():
    matriz = [[0]*4 for i in range(4)]

    matriz[0][0] = 1
    matriz[1][1] = 1
    matriz[2][2] = -1
    matriz[3][3] = 1

    return array(matriz)

def cisalhamentoYX(ang):
    matriz = [[0]*4 for i in range(4)]

    matriz[0][1] = math.tan(math.radians(ang))
    matriz[0][0] = 1
    matriz[1][1] = 1
    matriz[2][2] = 1
    matriz[3][3] = 1

    return array(matriz)  

def cisalhamentoXY(ang):
    matriz = [[0]*4 for i in range(4)]

    matriz[1][0] = math.tan(math.radians(ang))
    matriz[0][0] = 1
    matriz[1][1] = 1
    matriz[2][2] = 1
    matriz[3][3] = 1

    return array(matriz)  

def cisalhamentoZY(ang):
    matriz = [[0]*4 for i in range(4)]

    matriz[1][2] = math.tan(math.radians(ang))
    matriz[0][0] = 1
    matriz[1][1] = 1
    matriz[2][2] = 1
    matriz[3][3] = 1

    return array(matriz)  

def cisalhamentoYZ(ang):
    matriz = [[0]*4 for i in range(4)]

    matriz[2][1] = math.tan(math.radians(ang))
    matriz[0][0] = 1
    matriz[1][1] = 1
    matriz[2][2] = 1
    matriz[3][3] = 1

    return array(matriz)  

def cisalhamentoZX(ang):
    matriz = [[0]*4 for i in range(4)]

    matriz[0][2] = math.tan(math.radians(ang))
    matriz[0][0] = 1
    matriz[1][1] = 1
    matriz[2][2] = 1
    matriz[3][3] = 1

    return array(matriz)  

def cisalhamentoXZ(ang):
    matriz = [[0]*4 for i in range(4)]

    matriz[2][0] = math.tan(math.radians(ang))
    matriz[0][0] = 1
    matriz[1][1] = 1
    matriz[2][2] = 1
    matriz[3][3] = 1

    return array(matriz)  

def espelhoQualquer(x1, y1, z1, x2, y2, z2, x3, y3, z3):
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

    matriz = [[0]*4 for i in range(4)]

    for i in range(4):
        for j in range(4):
            if i==j:
                matriz[i][j] = 1

    for i in range(4):
        for j in range(4):
            matriz[i][j] -= 2 * normal[i] * normal[j]
    
    return array(matriz) 

def rotacaoQualquer(ang, x1, y1, z1, x2, y2, z2):
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

    matriz = [[0]*4 for i in range(4)]

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
    
    return array(matriz)
