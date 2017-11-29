from Vertice import Vertice

class Camera:

    def __init__(self, xEye, yEye, zEye, xLookAt = None, yLookAt = None, zLookAt = None, xAvup = None, yAvup = None, zAvup = None):
        if xLookAt is None:
            self.i = []
            self.j = []
            self.k = []
            self.Eye = xEye
            self.LookAt = yEye
            self.Avup = zEye
            self.Vup = Vertice(self.Avup.x - self.Eye.x, self.Avup.y - self.Eye.y, self.Avup.z - self.Eye.z)
        else:        
            self.i = []
            self.j = []
            self.k = []
            self.Eye = Vertice(xEye, yEye, zEye)
            self.LookAt = Vertice(xLookAt, yLookAt, zLookAt)
            self.Vup = Vertice(xAvup - xEye, yAvup - yEye, zAvup - zEye)

        self.calcula_k()
        self.calcula_i()
        self.calcula_j()

    def calcula_k(self):
        self.k.append(self.Eye.x - self.LookAt.x)
        self.k.append(self.Eye.y - self.LookAt.y)
        self.k.append(self.Eye.z - self.LookAt.z)

        mod = (self.k[0]**2 + self.k[1]**2 + self.k[2]**2)**0.5

        for n in range(3):
            self.k[n] /= mod
        
    def calcula_i(self):
        self.i.append(self.Vup.y * self.k[2] - self.Vup.z * self.k[1]) 
        self.i.append(self.Vup.z * self.k[0] - self.Vup.x * self.k[2])
        self.i.append(self.Vup.x * self.k[1] - self.Vup.y * self.k[0])

        mod = (self.i[0]**2 + self.i[1]**2 + self.i[2]**2)**0.5

        for n in range(3):
            self.i[n] /= mod

    def calcula_j(self):
        self.j.append(self.k[1] * self.i[2] - self.k[2] * self.i[1]) 
        self.j.append(self.k[2] * self.i[0] - self.k[0] * self.i[2])
        self.j.append(self.k[0] * self.i[1] - self.k[1] * self.i[0])

    def matrizWC(self):
        matriz = [[0]*4 for i in range(4)]

        matriz[0][0] = self.i[0]
        matriz[0][1] = self.i[1]
        matriz[0][2] = self.i[2]
        matriz[0][3] = -(self.i[0] * self.Eye.x + self.i[1] * self.Eye.y + self.i[2] * self.Eye.z)
        matriz[1][0] = self.j[0]
        matriz[1][1] = self.j[1]
        matriz[1][2] = self.j[2]
        matriz[1][3] = -(self.j[0] * self.Eye.x + self.j[1] * self.Eye.y + self.j[2] * self.Eye.z)
        matriz[2][0] = self.k[0]
        matriz[2][1] = self.k[1]
        matriz[2][2] = self.k[2]
        matriz[2][3] = -(self.k[0] * self.Eye.x + self.k[1] * self.Eye.y + self.k[2] * self.Eye.z)
        matriz[3][0] = 0
        matriz[3][1] = 0
        matriz[3][2] = 0
        matriz[3][3] = 1

        return matriz

    def matrizCW(self):
        matriz = [[0]*4 for i in range(4)]

        matriz[0][0] = self.i[0]
        matriz[0][1] = self.j[0]
        matriz[0][2] = self.k[0]
        matriz[0][3] = self.Eye.x
        matriz[1][0] = self.i[1]
        matriz[1][1] = self.j[1]
        matriz[1][2] = self.k[1]
        matriz[1][3] = self.Eye.y
        matriz[2][0] = self.i[2]
        matriz[2][1] = self.j[2]
        matriz[2][2] = self.k[2]
        matriz[2][3] = self.Eye.z
        matriz[3][0] = 0
        matriz[3][1] = 0
        matriz[3][2] = 0
        matriz[3][3] = 1

        return matriz