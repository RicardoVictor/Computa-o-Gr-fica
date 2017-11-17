class Pontual():
    def __init__(self, fx, fy, fz, IdR, IdG, IdB, IeR, IeG, IeB):
        self.fx = fx
        self.fy = fy
        self.fz = fz
        self.IdR = IdR
        self.IdG = IdG
        self.IdB = IdB
        self.IeR = IeR
        self.IeG = IeG
        self.IeB = IeB

class Spot():
    def __init__(self, fx, fy, fz, IdR, IdG, IdB, IeR, IeG, IeB, direcao, ang_abertura):
        self.fx = fx
        self.fy = fy
        self.fz = fz
        self.IdR = IdR
        self.IdG = IdG
        self.IdB = IdB
        self.IeR = IeR
        self.IeG = IeG
        self.IeB = IeB
        self.direcao = direcao
        self.ang_abertura = ang_abertura