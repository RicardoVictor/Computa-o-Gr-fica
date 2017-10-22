import Objeto
import Vertice

class Aura:

    def __init__(self, obj):

        x_max = -999999
        x_min = 999999
        y_max = -999999
        y_min = 999999
        z_max = -999999
        z_min = 999999
        
        for i in range(len(obj.vertices)):
            if x_max < obj.vertices[i].x:
                x_max = obj.vertices[i].x
            if y_max < obj.vertices[i].y:
                y_max = obj.vertices[i].y
            if z_max < obj.vertices[i].z:
                z_max = obj.vertices[i].z

            if x_min > obj.vertices[i].x:
                x_min = obj.vertices[i].x
            if y_min > obj.vertices[i].y:
                y_min = obj.vertices[i].y
            if z_min > obj.vertices[i].z:
                z_min = obj.vertices[i].z

        self.centro = Vertice.Vertice((x_max + x_min) / 2, (y_max + y_min) / 2, (z_max + z_min) / 2)
        self.raio = ((x_max - self.centro.x)**2 + (y_max - self.centro.y)**2 + (z_max - self.centro.z)**2) ** 0.5