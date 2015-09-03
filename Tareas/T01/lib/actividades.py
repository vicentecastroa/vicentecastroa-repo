__author__ = 'Vicente'

class Clase:
    pass

class Evaluacion:

    def __init__(self, sigla='', sec='',fecha='',tipo=''):
        self.sigla = sigla
        self.sec = sec
        self.fecha = fecha
        self.tipo = tipo

    def __repr__(self):
        return "evaluacion {} {}".format(self.sigla, self.tipo)
