class Cenario:
   
    def __init__(self):
        self.objetos = []
        self.luz = []
        
    def addObjeto(self, obj):
        self.objetos.append(obj)

    def addCamera(self, camera):
        self.camera = camera

    def addScreen(self, screen):
        self.screen = screen

    def ray_casting(self):
        
        for i in range(self.screen.n):
            for j in range(self.screen.m):
                t_min = 9999999
                k_int = -1
                for k in range(len(self.objetos)):
                    
                    A = self.screen.screen[i][j].x**2 + self.screen.screen[i][j].y**2 + self.screen.screen[i][j].z**2
                    B = -2 * (self.screen.screen[i][j].x * self.objetos[k].aura.centro.x + self.screen.screen[i][j].y * self.objetos[k].aura.centro.y + self.screen.screen[i][j].z * self.objetos[k].aura.centro.z)
                    C = self.objetos[k].aura.centro.x**2 + self.objetos[k].aura.centro.y**2 + self.objetos[k].aura.centro.z**2 - self.objetos[k].aura.raio**2
                    delta = B**2 - 4*A*C

                    if delta >= 0:
                        t = (-B - delta**0.5) / (2*A)
                        
                        if t > 1 and t_min > t:
                            t_min = t
                            k_int = k
                            print('i:{} j:{} t:{:.6f}'.format(i, j, t))

                #valor final de t(igual a t_min) para determinado Pij e objeto k(igual a k_int)