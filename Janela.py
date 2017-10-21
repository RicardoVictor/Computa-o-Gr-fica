import Vertice

class Janela:

    def __init__(self, d, H, W, n, m):
        self.tela = []
        for i in range(n):
            self.tela.append([0]*m)
        
        Delta_x = W/m
        Delta_y = H/n
        
        for i in range(n):
            y = H/2 - Delta_y/2 - i * Delta_y
            for j in range(m):
                x = -(W/2) + Delta_x/2 + j * Delta_x
                self.tela[i][j] = Vertice.Vertice(x, y, -d)

    def imprimirTela(self, n, m):
        for i in range(n):    
            for j in range(m):
                print("[{:10.6f} {:10.6f} {:10.6f} ] ".format(self.tela[i][j].x, self.tela[i][j].y, self.tela[i][j].z))
            print()
