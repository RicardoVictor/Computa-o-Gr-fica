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
                obj_int = -1
                for obj in range(len(self.objetos)):
                    
                    A = self.screen.screen[i][j].x**2 + self.screen.screen[i][j].y**2 + self.screen.screen[i][j].z**2
                    B = -2 * (self.screen.screen[i][j].x * self.objetos[obj].aura.centro.x + self.screen.screen[i][j].y * self.objetos[obj].aura.centro.y + self.screen.screen[i][j].z * self.objetos[obj].aura.centro.z)
                    C = self.objetos[obj].aura.centro.x**2 + self.objetos[obj].aura.centro.y**2 + self.objetos[obj].aura.centro.z**2 - self.objetos[obj].aura.raio**2
                    delta = B**2 - 4*A*C

                    if delta >= 0:
                        t = (-B - delta**0.5) / (2*A)
                        
                        if t > 1 and t_min > t:
                            t_min = t
                            obj_int = obj
                            #print('i:{} j:{} t:{:.6f}'.format(i, j, t))

                #---valor final de t(igual a t_min) para determinado Pij e objeto obj(igual a obj_int)
                
                Pij = []
                Pij.append(self.screen.screen[i][j].x)
                Pij.append(self.screen.screen[i][j].y)
                Pij.append(self.screen.screen[i][j].z)
                
                v = Pij
                mod_v = (v[0]**2 + v[1]**2 + v[2]**2)**0.5
                v[0] /= mod_v
                v[1] /= mod_v
                v[2] /= mod_v

                for face in range(len(self.objetos[obj_int].faces)):
                    v_prod_esc_n = v[0] * self.objetos[obj_int].faces[face].normal[0] + v[1] * self.objetos[obj_int].faces[face].normal[1] + v[2] * self.objetos[obj_int].faces[face].normal[2]
                    if v_prod_esc_n > 0:
                        P1_prod_esc_n = self.objetos[obj_int].faces[face].P1.x * self.objetos[obj_int].faces[face].normal[0] + self.objetos[obj_int].faces[face].P1.y * self.objetos[obj_int].faces[face].normal[1] + self.objetos[obj_int].faces[face].P1.z * self.objetos[obj_int].faces[face].normal[2]

                        Pij_prod_esc_n =Pij[0] * self.objetos[obj_int].faces[face].normal[0] + Pij[1] * self.objetos[obj_int].faces[face].normal[1] + Pij[2] * self.objetos[obj_int].faces[face].normal[2]
              
                        t_int = P1_prod_esc_n / Pij_prod_esc_n

                        # P_int = ponto de intercecao do raio com o plano de determinada face
                        P_int = []
                        P_int.append(Pij[0] * t_int)
                        P_int.append(Pij[1] * t_int)
                        P_int.append(Pij[2] * t_int)

                        # testar se Pij esta na face
                        w1 = []
                        w1.append(self.objetos[obj_int].faces[face].P1.x - P_int[0])
                        w1.append(self.objetos[obj_int].faces[face].P1.y - P_int[1])
                        w1.append(self.objetos[obj_int].faces[face].P1.z - P_int[2])

                        w2 = []
                        w2.append(self.objetos[obj_int].faces[face].P2.x - P_int[0])
                        w2.append(self.objetos[obj_int].faces[face].P2.y - P_int[1])
                        w2.append(self.objetos[obj_int].faces[face].P2.z - P_int[2])
                        
                        w3 = []
                        w3.append(self.objetos[obj_int].faces[face].P3.x - P_int[0])
                        w3.append(self.objetos[obj_int].faces[face].P3.y - P_int[1])
                        w3.append(self.objetos[obj_int].faces[face].P3.z - P_int[2])

                        v1 = []
                        v1.append(w1[1] * w2[2] - w1[2] * w2[1]) 
                        v1.append(w1[2] * w2[0] - w1[0] * w2[2])
                        v1.append(w1[0] * w2[1] - w1[1] * w2[0])

                        v2 = []
                        v2.append(w2[1] * w3[2] - w2[2] * w3[1]) 
                        v2.append(w2[2] * w3[0] - w2[0] * w3[2])
                        v2.append(w2[0] * w3[1] - w2[1] * w3[0])

                        v3 = []
                        v3.append(w3[1] * w1[2] - w3[2] * w1[1]) 
                        v3.append(w3[2] * w1[0] - w3[0] * w1[2])
                        v3.append(w3[0] * w1[1] - w3[1] * w1[0])

                        if (self.objetos[obj_int].faces[face].normal[0] * v1[0]) > 0 and (self.objetos[obj_int].faces[face].normal[1] * v1[1]) > 0 and (self.objetos[obj_int].faces[face].normal[2] * v1[2]) > 0 and (self.objetos[obj_int].faces[face].normal[0] * v2[0]) > 0 and (self.objetos[obj_int].faces[face].normal[1] * v2[1]) > 0 and (self.objetos[obj_int].faces[face].normal[2] * v2[2]) > 0 and (self.objetos[obj_int].faces[face].normal[0] * v3[0]) > 0 and (self.objetos[obj_int].faces[face].normal[1] * v3[1]) > 0 and (self.objetos[obj_int].faces[face].normal[2] * v3[2]) > 0:
                            pass # "pintar"