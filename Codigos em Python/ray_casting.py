from algebra import *

def renderizar(cenario):
        cores = {}
        for i in range(cenario.screen.n):
            for j in range(cenario.screen.m):
                t_min = 9999999
                obj_int = -1
                for obj in range(len(cenario.objetos)):
                    
                    A = cenario.screen.screen[i][j].x**2 + cenario.screen.screen[i][j].y**2 + cenario.screen.screen[i][j].z**2
                    B = -2 * (cenario.screen.screen[i][j].x * cenario.objetos[obj].aura.centro.x + cenario.screen.screen[i][j].y * cenario.objetos[obj].aura.centro.y + cenario.screen.screen[i][j].z * cenario.objetos[obj].aura.centro.z)
                    C = cenario.objetos[obj].aura.centro.x**2 + cenario.objetos[obj].aura.centro.y**2 + cenario.objetos[obj].aura.centro.z**2 - cenario.objetos[obj].aura.raio**2
                    delta = B**2 - 4*A*C

                    if delta >= 0:
                        t = (-B - delta**0.5) / (2*A)
                        
                        if t > 1:
                        #if t > 1 or t_min > t:
                            t_min = t
                            obj_int = obj
                            #print('i:{} j:{} t:{:.6f}'.format(i, j, t))

                #---valor final de t(igual a t_min) para determinado Pij e objeto obj(igual a obj_int)
                
                Pij = []
                Pij.append(cenario.screen.screen[i][j].x)
                Pij.append(cenario.screen.screen[i][j].y)
                Pij.append(cenario.screen.screen[i][j].z)
                
                v = Pij
                v = normalizar(v)

                for face in range(len(cenario.objetos[obj_int].faces)):
                    #v_prod_esc_n = produto_escalar(v, cenario.objetos[obj_int].faces[face].normal)
                    v_prod_esc_n = v[0] * cenario.objetos[obj_int].faces[face].normal[0] + v[1] * cenario.objetos[obj_int].faces[face].normal[1] + v[2] * cenario.objetos[obj_int].faces[face].normal[2]
                    #backface culling
                    if v_prod_esc_n < 0:
                        #P1_prod_esc_n = produto_escalar(cenario.objetos[obj_int].faces[face].P1, cenario.objetos[obj_int].faces[face].normal)
                        P1_prod_esc_n = cenario.objetos[obj_int].faces[face].P1.x * cenario.objetos[obj_int].faces[face].normal[0] + cenario.objetos[obj_int].faces[face].P1.y * cenario.objetos[obj_int].faces[face].normal[1] + cenario.objetos[obj_int].faces[face].P1.z * cenario.objetos[obj_int].faces[face].normal[2]
                        #Pij_prod_esc_n = produto_escalar(Pij, cenario.objetos[obj_int].faces[face].normal)
                        Pij_prod_esc_n = Pij[0] * cenario.objetos[obj_int].faces[face].normal[0] + Pij[1] * cenario.objetos[obj_int].faces[face].normal[1] + Pij[2] * cenario.objetos[obj_int].faces[face].normal[2]         
                        t_int = P1_prod_esc_n / Pij_prod_esc_n

                        # P_int = ponto de intercecao do raio com o plano de determinada face
                        P_int = []
                        P_int.append(Pij[0] * t_int)
                        P_int.append(Pij[1] * t_int)
                        P_int.append(Pij[2] * t_int)

                        # testar se Pij esta na face
                        w1 = []
                        w1.append(cenario.objetos[obj_int].faces[face].P1.x - P_int[0])
                        w1.append(cenario.objetos[obj_int].faces[face].P1.y - P_int[1])
                        w1.append(cenario.objetos[obj_int].faces[face].P1.z - P_int[2])

                        w2 = []
                        w2.append(cenario.objetos[obj_int].faces[face].P2.x - P_int[0])
                        w2.append(cenario.objetos[obj_int].faces[face].P2.y - P_int[1])
                        w2.append(cenario.objetos[obj_int].faces[face].P2.z - P_int[2])
                        
                        w3 = []
                        w3.append(cenario.objetos[obj_int].faces[face].P3.x - P_int[0])
                        w3.append(cenario.objetos[obj_int].faces[face].P3.y - P_int[1])
                        w3.append(cenario.objetos[obj_int].faces[face].P3.z - P_int[2])

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

                        if (cenario.objetos[obj_int].faces[face].normal[0] * v1[0] > 0) and (cenario.objetos[obj_int].faces[face].normal[0] * v2[0] > 0)  and (cenario.objetos[obj_int].faces[face].normal[0] * v3[0] > 0):
                            #print('face:', face)
                            #print(Pij)
                            #print(P_int)
                            #print('t_int:', t_int)
                            #print('normal:', cenario.objetos[obj_int].faces[face].normal[0], cenario.objetos[obj_int].faces[face].normal[1], cenario.objetos[obj_int].faces[face].normal[2])
                            #print('v1:', v1[0], v1[1], v1[2], 'v2:', v2[0], v2[1], v2[2], 'v3:', v3[0], v3[1], v3[2]))
                            I_fontes = []
                            I_fontes.append(0)
                            I_fontes.append(0)
                            I_fontes.append(0)
                            for fonte in range(len(cenario.fontes)):
                                #v2: -P_int unitario
                                v2 = []
                                v2.append(-P_int[0])
                                v2.append(-P_int[1])
                                v2.append(-P_int[2])
                                v2 = normalizar(v2)
                                
                                #l: vetor (Fonte - P_int) unitario
                                l = []
                                l.append(cenario.fontes[fonte].fx - P_int[0])
                                l.append(cenario.fontes[fonte].fy - P_int[1])
                                l.append(cenario.fontes[fonte].fz - P_int[2])
                                l = normalizar(l)
                                
                                #r: 2*n*(l . n) - l
                                r = []
                                #l_prod_esc_n = produto_escalar(l, cenario.objetos[obj_int].faces[face].normal)
                                l_prod_esc_n = l[0] * cenario.objetos[obj_int].faces[face].normal[0] + l[1] * cenario.objetos[obj_int].faces[face].normal[1] + l[2] + cenario.objetos[obj_int].faces[face].normal[2]
                                r.append(2 * cenario.objetos[obj_int].faces[face].normal[0] * l_prod_esc_n - l[0])
                                r.append(2 * cenario.objetos[obj_int].faces[face].normal[1] * l_prod_esc_n - l[1])
                                r.append(2 * cenario.objetos[obj_int].faces[face].normal[2] * l_prod_esc_n - l[2])
                            
                                #n_prod_esc_l = produto_escalar(cenario.objetos[obj_int].faces[face].normal, l)
                                n_prod_esc_l = cenario.objetos[obj_int].faces[face].normal[0] * l[0] + cenario.objetos[obj_int].faces[face].normal[1] * l[1] + cenario.objetos[obj_int].faces[face].normal[2] * l[2]
                                #v2_prod_esc_r = produto_escalar(v2, r)
                                v2_prod_esc_r = v2[0] * r[0] + v2[1] * r[1] + v2[2] * r[2]

                                #print(cenario.objetos[obj_int].faces[face].normal)
                                #print(l)
                                #print(v2)
                                #print(r)
                                if n_prod_esc_l >=0 and v2_prod_esc_r >=0:
                                    I_fontes[0] += (cenario.objetos[obj_int].faces[face].textura.kdR * cenario.fontes[fonte].IdR * n_prod_esc_l + cenario.objetos[obj_int].faces[face].textura.keR * cenario.fontes[fonte].IeR * (v2_prod_esc_r**cenario.objetos[obj_int].faces[face].textura.m))
                                    I_fontes[1] += (cenario.objetos[obj_int].faces[face].textura.kdG * cenario.fontes[fonte].IdG * n_prod_esc_l + cenario.objetos[obj_int].faces[face].textura.keG * cenario.fontes[fonte].IeG * (v2_prod_esc_r**cenario.objetos[obj_int].faces[face].textura.m))
                                    I_fontes[2] += (cenario.objetos[obj_int].faces[face].textura.kdB * cenario.fontes[fonte].IdB * n_prod_esc_l + cenario.objetos[obj_int].faces[face].textura.keB * cenario.fontes[fonte].IeB * (v2_prod_esc_r**cenario.objetos[obj_int].faces[face].textura.m))
                            
                            #end_for

                            Iobs = []
                            Iobs.append(cenario.objetos[obj_int].faces[face].textura.kaR * cenario.IaR + I_fontes[0])
                            Iobs.append(cenario.objetos[obj_int].faces[face].textura.kaG * cenario.IaG + I_fontes[1])
                            Iobs.append(cenario.objetos[obj_int].faces[face].textura.kaB * cenario.IaB + I_fontes[2])
                            #print(I_fontes)
                            
                            cores.update({str(i) +' '+ str(j) : Iobs})
                            #print(i, j)
                            #print(Iobs)

        for i in range(cenario.screen.n):
            for j in range(cenario.screen.m):
                if(str(i) +' '+ str(j) not in cores):
                    cores.update({str(i) +' '+ str(j) : cenario.background_color})
        return cores