class Aresta():

    v1 = ''
    v2 = ''
    rotulo = ''
    peso = 1
    SEPARADOR_ARESTA = '-'

    def __init__(self, rotulo='',v1='', v2='', peso=1):
        self.setV1(v1)
        self.setV2(v2)
        self.setRotulo(rotulo)
        self.setPeso(peso)

    def getV1(self):
        return self.v1

    def getV2(self):
        return self.v2

    def setV1(self, v=''):
        self.v1 = v

    def setV2(self, v=''):
        self.v2 = v

    def getPeso(self):
        return self.peso

    def setPeso(self, p=''):
        self.peso = p

    def getRotulo(self):
        return self.rotulo

    def setRotulo(self, r=''):
        self.rotulo = r

    def ehPonta(self, v):
        return v == self.v1 or v == self.v2

    def __eq__(self, other):
        return ((self.v1 == other.getV1() and self.v2 == other.getV2()) or (self.v1 == other.getV2() and self.v2 == other.getV1())) and self.rotulo == other.getRotulo() and self.getPeso() == other.getPeso()

    def __str__(self):
        return "{}({}-{}), {}".format(self.getRotulo(), self.getV1(), self.getV2(), self.getPeso())

class ArestaDirecionada(Aresta):
    def __eq__(self, other):
        return self.v1 == other.getV1() and self.v2 == other.getV2() and self.rotulo == other.getRotulo() and self.getPeso() == other.getPeso()

    def __str__(self):
        return "{}({}->{}), {}".format(self.getRotulo(), self.getV1(), self.getV2(), self.getPeso())