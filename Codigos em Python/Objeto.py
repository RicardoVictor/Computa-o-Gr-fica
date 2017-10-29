from numpy import dot
import Vertice
import Face
import Aura

class Objeto:

    def __init__(self):
        self.vertices = []
        self.faces = []

    @property
    def aura(self):
        return Aura.Aura(self)

    def addVertice(self, x, y, z):
        vertice = Vertice.Vertice(x, y, z)
        self.vertices.append(vertice)

    def addFace(self, P1, P2, P3):
        face = Face.Face(P1, P2, P3)
        self.faces.append(face)

    def imprimirVertices(self):
        for i in range(len(self.vertices)):
            print("({:10.6f} {:10.6f} {:10.6f} )".format(self.vertices[i].x, self.vertices[i].y, self.vertices[i].z))
        print()

    def aplica(self, matriz):
        for i in range(len(self.vertices)):
            vertice = [self.vertices[i].x, self.vertices[i].y, self.vertices[i].z, 1]
            vertice = dot(matriz, vertice)

            self.vertices[i].x = vertice[0]
            self.vertices[i].y = vertice[1]
            self.vertices[i].z = vertice[2]
