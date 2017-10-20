class Vertice:
    __x = None
    __y = None
    __z = None

    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def getZ(self):
        return self.__z
    def setX(self, x):
        self.__x = x
    def setY(self, y):
        self.__y = y
    def setZ(self, z):
        self.__z = z
      