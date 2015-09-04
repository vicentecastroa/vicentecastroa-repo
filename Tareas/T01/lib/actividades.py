__author__ = 'Vicente'

class Evaluacion:

    def __init__(self, sigla='', sec='',fecha='',tipo=''):
        self.sigla = sigla
        self.sec = sec
        self.fecha = fecha
        self.tipo = tipo

    def __repr__(self):
        return "Dia: {}  |  {}-{}".format(self.fecha, self.tipo, self.sigla)
