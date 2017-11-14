class Cenario:
   
    def __init__(self, IaR, IaG, IaB):
        #iluminação ambiente
        self.IaR = IaR
        self.IaG = IaG
        self.IaB = IaB
        self.objetos = []
        self.fontes = []
        self.background_color = [1, 1, 1]

    @property
    def background_color(self):
        return self.__background_color

    @background_color.setter
    def background_color(self, background_color):
        self.__background_color = background_color

    def addObjeto(self, obj):
        self.objetos.append(obj)

    def addCamera(self, camera):
        self.camera = camera

    def addScreen(self, screen):
        self.screen = screen

    def addFonte(self, fonte):
        self.fontes.append(fonte)

    def ray_casting(self):
        cores = {}
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
                    #backface culling
                    if v_prod_esc_n < 0:
                        P1_prod_esc_n = self.objetos[obj_int].faces[face].P1.x * self.objetos[obj_int].faces[face].normal[0] + self.objetos[obj_int].faces[face].P1.y * self.objetos[obj_int].faces[face].normal[1] + self.objetos[obj_int].faces[face].P1.z * self.objetos[obj_int].faces[face].normal[2]
                        Pij_prod_esc_n = Pij[0] * self.objetos[obj_int].faces[face].normal[0] + Pij[1] * self.objetos[obj_int].faces[face].normal[1] + Pij[2] * self.objetos[obj_int].faces[face].normal[2]         
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

                        if (self.objetos[obj_int].faces[face].normal[0] * v1[0] > 0) and (self.objetos[obj_int].faces[face].normal[0] * v2[0] > 0)  and (self.objetos[obj_int].faces[face].normal[0] * v3[0] > 0):
                            #print('face:', face)
                            #print(Pij)
                            #print(P_int)
                            #print('t_int:', t_int)
                            #print('normal:', self.objetos[obj_int].faces[face].normal[0], self.objetos[obj_int].faces[face].normal[1], self.objetos[obj_int].faces[face].normal[2])
                            #print('v1:', v1[0], v1[1], v1[2], 'v2:', v2[0], v2[1], v2[2], 'v3:', v3[0], v3[1], v3[2]))
                            I_fontes = []
                            I_fontes.append(0)
                            I_fontes.append(0)
                            I_fontes.append(0)
                            for fonte in range(len(self.fontes)):
                                #v2: -P_int unitario
                                v2 = []
                                v2.append(-P_int[0])
                                v2.append(-P_int[1])
                                v2.append(-P_int[2])
                                mod_v2 = (v2[0]**2 + v2[1]**2 + v2[2]**2)**0.5
                                v2[0] /= mod_v2
                                v2[1] /= mod_v2
                                v2[2] /= mod_v2

                                #l: vetor (Fonte - P_int) unitario
                                l = []
                                l.append(self.fontes[fonte].fx - P_int[0])
                                l.append(self.fontes[fonte].fy - P_int[1])
                                l.append(self.fontes[fonte].fz - P_int[2])
                                mod_l = (l[0]**2 + l[1]**2 + l[2]**2)**0.5
                                l[0] /= mod_l
                                l[1] /= mod_l
                                l[2] /= mod_l

                                #r: 2*n*(l . n) - l
                                r = []
                                l_prod_esc_n = l[0] * self.objetos[obj_int].faces[face].normal[0] + l[1] * self.objetos[obj_int].faces[face].normal[1] + l[2] + self.objetos[obj_int].faces[face].normal[2]
                                r.append(2 * self.objetos[obj_int].faces[face].normal[0] * l_prod_esc_n - l[0])
                                r.append(2 * self.objetos[obj_int].faces[face].normal[1] * l_prod_esc_n - l[1])
                                r.append(2 * self.objetos[obj_int].faces[face].normal[2] * l_prod_esc_n - l[2])
                            
                                n_prod_esc_l = self.objetos[obj_int].faces[face].normal[0] * l[0] + self.objetos[obj_int].faces[face].normal[1] * l[1] + self.objetos[obj_int].faces[face].normal[2] * l[2]
                                v2_prod_esc_r = v2[0] * r[0] + v2[1] * r[1] + v2[2] * r[2]

                                '''print(self.objetos[obj_int].faces[face].normal)
                                print(l)
                                print(v2)
                                print(r)'''
                                if n_prod_esc_l >=0 and v2_prod_esc_r >=0:
                                    I_fontes[0] += (self.objetos[obj_int].faces[face].textura.kdR * self.fontes[fonte].IdR * n_prod_esc_l + self.objetos[obj_int].faces[face].textura.keR * self.fontes[fonte].IeR * (v2_prod_esc_r**self.objetos[obj_int].faces[face].textura.m))
                                    I_fontes[1] += (self.objetos[obj_int].faces[face].textura.kdG * self.fontes[fonte].IdG * n_prod_esc_l + self.objetos[obj_int].faces[face].textura.keG * self.fontes[fonte].IeG * (v2_prod_esc_r**self.objetos[obj_int].faces[face].textura.m))
                                    I_fontes[2] += (self.objetos[obj_int].faces[face].textura.kdB * self.fontes[fonte].IdB * n_prod_esc_l + self.objetos[obj_int].faces[face].textura.keB * self.fontes[fonte].IeB * (v2_prod_esc_r**self.objetos[obj_int].faces[face].textura.m))
                            
                                #end_for

                            Iobs = []

                            Iobs.append(self.objetos[obj_int].faces[face].textura.kaR * self.IaR + I_fontes[0])
                            Iobs.append(self.objetos[obj_int].faces[face].textura.kaG * self.IaG + I_fontes[1])
                            Iobs.append(self.objetos[obj_int].faces[face].textura.kaB * self.IaB + I_fontes[2])
                            #print(I_fontes)
                            
                            cores.update({str(i) +' '+ str(j) : Iobs})
                            #print(i, j)
                            #print(Iobs)
        
        for i in range(self.screen.n):
            for j in range(self.screen.m):
                if(str(i) +' '+ str(j) not in cores):
                    cores.update({str(i) +' '+ str(j) : self.background_color})
        return cores