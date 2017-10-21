class Camera:
    __i = []
    __j = []
    __k = []
    __Eye = []
    __LookAt = []
    __Avup = []

    def __init__(self, xEye, yEye, zEye, xLookAt, yLookAt, zLookAt, xAvup, yAvup, zAvup):
        self.__Eye.append(xEye)
        self.__Eye.append(yEye)
        self.__Eye.append(zEye)
        self.__LookAt.append(xLookAt)
        self.__LookAt.append(yLookAt)
        self.__LookAt.append(zLookAt)
        self.__Avup.append(xAvup)
        self.__Avup.append(yAvup)
        self.__Avup.append(zAvup)

        self.calculak()
        self.calculai()
        self.calculaj()

    def calculak(self):
        k = []
        Eye = self.__Eye
        LookAt = self.__LookAt

        k.append(Eye[0] - LookAt[0])
        k.append(Eye[1] - LookAt[1])
        k.append(Eye[2] - LookAt[2])

        mod = (k[0]**2 + k[1]**2 + k[2]**2)**0.5

        for n in range(3):
            k[n] /= mod
        
        self.__k = k

    def calculai(self):
        Avup = self.__Avup
        k = self.__k
        i = []

        i.append(Avup[1] * k[2] - Avup[2] * k[1]) 
        i.append(Avup[2] * k[0] - Avup[0] * k[2])
        i.append(Avup[0] * k[1] - Avup[1] * k[0])

        mod = (i[0]**2 + i[1]**2 + i[2]**2)**0.5

        for n in range(3):
            i[n] /= mod

        self.__i = i

    def calculaj(self):
        i = self.__i
        k = self.__k

        self.__j.append(k[1] * i[2] - k[2] * i[1]) 
        self.__j.append(k[2] * i[0] - k[0] * i[2])
        self.__j.append(k[0] * i[1] - k[1] * i[0])

    def matrizWC(self):
        matriz = []
        for i in range(4):
            matriz.append([0]*4)
        
        i = self.__i
        j = self.__j
        k = self.__k
        Eye = self.__Eye

        matriz[0][0] = i[0]
        matriz[0][1] = i[1]
        matriz[0][2] = i[2]
        matriz[0][3] = -(i[0]*Eye[0] + i[1]*Eye[1] + i[2]*Eye[2])
        matriz[1][0] = j[0]
        matriz[1][1] = j[0]
        matriz[1][2] = j[0]
        matriz[1][3] = -(j[0]*Eye[0] + j[1]*Eye[1] + j[2]*Eye[2])
        matriz[2][0] = k[0]
        matriz[2][1] = k[0]
        matriz[2][2] = k[0]
        matriz[2][3] = -(k[0]*Eye[0] + k[1]*Eye[1] + k[2]*Eye[2])
        matriz[3][0] = 0
        matriz[3][1] = 0
        matriz[3][2] = 0
        matriz[3][3] = 1

        return matriz

    def matrizCW(self):
        matriz = []
        for i in range(4):
            matriz.append([0]*4)
        
        i = self.__i
        j = self.__j
        k = self.__k
        Eye = self.__Eye

        matriz[0][0] = i[0]
        matriz[0][1] = j[0]
        matriz[0][2] = k[0]
        matriz[0][3] = Eye[0]
        matriz[1][0] = i[1]
        matriz[1][1] = j[1]
        matriz[1][2] = k[1]
        matriz[1][3] = Eye[1]
        matriz[2][0] = i[2]
        matriz[2][1] = j[2]
        matriz[2][2] = k[2]
        matriz[2][3] = Eye[2]
        matriz[3][0] = 0
        matriz[3][1] = 0
        matriz[3][2] = 0
        matriz[3][3] = 1

        return matriz