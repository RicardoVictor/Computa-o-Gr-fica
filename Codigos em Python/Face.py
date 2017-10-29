class Face:
    def __init__(self, P1, P2, P3):
        self.P1 = P1
        self.P2 = P2
        self.P3 = P3

    @property
    def normal(self):
        P1_P2 = []
        P1_P2.append(self.P2.x - self.P1.x)
        P1_P2.append(self.P2.y - self.P1.y)
        P1_P2.append(self.P2.z - self.P1.z)

        P1_P3 = []        
        P1_P3.append(self.P3.x - self.P1.x)
        P1_P3.append(self.P3.y - self.P1.y)
        P1_P3.append(self.P3.z - self.P1.z)

        normal = []
        normal.append(P1_P2[1] * P1_P3[2] - P1_P2[2] * P1_P3[1]) 
        normal.append(P1_P2[2] * P1_P3[0] - P1_P2[0] * P1_P3[2])
        normal.append(P1_P2[0] * P1_P3[1] - P1_P2[1] * P1_P3[0])

        mod_n = (normal[0]**2 + normal[1]**2 + normal[2]**2)**0.5

        for i in range(3):
            normal[i] /= mod_n

        return normal