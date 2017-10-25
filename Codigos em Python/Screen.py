import Vertice

class Screen:

    def __init__(self, d, H, W, n, m):
        self.n = n
        self.m = m
        self.screen = []
        for i in range(n):
            self.screen.append([0]*m)
        
        Delta_x = W/m
        Delta_y = H/n
        
        for i in range(n):
            y = H/2 - Delta_y/2 - i * Delta_y
            for j in range(m):
                x = -(W/2) + Delta_x/2 + j * Delta_x
                self.screen[i][j] = Vertice.Vertice(x, y, -d)

    def imprimirTela(self):
        for i in range(self.n):    
            for j in range(self.m):
                print("[{:10.6f} {:10.6f} {:10.6f} ] ".format(self.screen[i][j].x, self.screen[i][j].y, self.screen[i][j].z))
            print()
