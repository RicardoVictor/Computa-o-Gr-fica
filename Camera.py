class Camera:

    def __init__(self, xEye, yEye, zEye, xLookAt, yLookAt, zLookAt, xAvup, yAvup, zAvup):
        self.i = []
        self.j = []
        self.k = []
        self.Eye = []
        self.LookAt = []
        self.Vup = []

        self.Eye.append(xEye)
        self.Eye.append(yEye)
        self.Eye.append(zEye)
        self.LookAt.append(xLookAt)
        self.LookAt.append(yLookAt)
        self.LookAt.append(zLookAt)
        self.Vup.append(xAvup - xEye)
        self.Vup.append(yAvup - yEye)
        self.Vup.append(zAvup - zEye)

        self.calcula_k()
        self.calcula_i()
        self.calcula_j()

    def calcula_k(self):
        self.k.append(self.Eye[0] - self.LookAt[0])
        self.k.append(self.Eye[1] - self.LookAt[1])
        self.k.append(self.Eye[2] - self.LookAt[2])

        mod = (self.k[0]**2 + self.k[1]**2 + self.k[2]**2)**0.5

        for n in range(3):
            self.k[n] /= mod
        
    def calcula_i(self):
        self.i.append(self.Vup[1] * self.k[2] - self.Vup[2] * self.k[1]) 
        self.i.append(self.Vup[2] * self.k[0] - self.Vup[0] * self.k[2])
        self.i.append(self.Vup[0] * self.k[1] - self.Vup[1] * self.k[0])

        mod = (self.i[0]**2 + self.i[1]**2 + self.i[2]**2)**0.5

        for n in range(3):
            self.i[n] /= mod

    def calcula_j(self):
        self.j.append(self.k[1] * self.i[2] - self.k[2] * self.i[1]) 
        self.j.append(self.k[2] * self.i[0] - self.k[0] * self.i[2])
        self.j.append(self.k[0] * self.i[1] - self.k[1] * self.i[0])

    def matrizWC(self):
        matriz = []
        for i in range(4):
            matriz.append([0]*4)

        matriz[0][0] = self.i[0]
        matriz[0][1] = self.i[1]
        matriz[0][2] = self.i[2]
        matriz[0][3] = -(self.i[0] * self.Eye[0] + self.i[1] * self.Eye[1] + self.i[2] * self.Eye[2])
        matriz[1][0] = self.j[0]
        matriz[1][1] = self.j[1]
        matriz[1][2] = self.j[2]
        matriz[1][3] = -(self.j[0] * self.Eye[0] + self.j[1] * self.Eye[1] + self.j[2] * self.Eye[2])
        matriz[2][0] = self.k[0]
        matriz[2][1] = self.k[1]
        matriz[2][2] = self.k[2]
        matriz[2][3] = -(self.k[0] * self.Eye[0] + self.k[1] * self.Eye[1] + self.k[2] * self.Eye[2])
        matriz[3][0] = 0
        matriz[3][1] = 0
        matriz[3][2] = 0
        matriz[3][3] = 1

        return matriz

    def matrizCW(self):
        matriz = []
        for i in range(4):
            matriz.append([0]*4)

        matriz[0][0] = self.i[0]
        matriz[0][1] = self.j[0]
        matriz[0][2] = self.k[0]
        matriz[0][3] = self.Eye[0]
        matriz[1][0] = self.i[1]
        matriz[1][1] = self.j[1]
        matriz[1][2] = self.k[1]
        matriz[1][3] = self.Eye[1]
        matriz[2][0] = self.i[2]
        matriz[2][1] = self.j[2]
        matriz[2][2] = self.k[2]
        matriz[2][3] = self.Eye[2]
        matriz[3][0] = 0
        matriz[3][1] = 0
        matriz[3][2] = 0
        matriz[3][3] = 1

        return matriz