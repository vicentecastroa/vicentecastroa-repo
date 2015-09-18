__author__ = 'Vicente'

from datos import Lista


class Puerto:

    def __init__(self, id):
        self.id = id
        self.hijos = Lista()
        self.padres = Lista()
        self.conexiones = Lista()
        self.conexiones_posibles = 0
        self.futura_conexion = self.iter_conexiones()
        pass

    def iter_conexiones(self):
        while True:
            for i in range(self.conexiones_posibles):
                yield i

    def decidir_conexion(self):
        return next(self.futura_conexion)

    def __repr__(self):
        return "PUERTO ID{}".format(self.id)

