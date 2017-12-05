class Cenario:
   
    def __init__(self, IaR, IaG, IaB):
        #iluminação ambiente
        self.IaR = IaR
        self.IaG = IaG
        self.IaB = IaB
        self.objetos = []
        self.fontes = []
        self.background_color = [0, 0, 0]

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