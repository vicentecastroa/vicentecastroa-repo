__author__ = 'Vicente'

import lib.estructura_datos as datos


class Conexion:
    def __init__(self, id, desde):
        self.id = id
        self.desde = desde
        self.destinos = datos.Lista()
        self.tipo = None

    def agregar_destino(self, destino):
        destino = datos.Nodo(destino)
        self.destinos.add(destino)

    def get_tipo(self):
        for i in range(self.destinos.largo):
            pass

    def __repr__(self):
        return "CONEXION desde {}".format(self.desde)


a = Conexion(3, 6)
a.agregar_destino(9)
a.agregar_destino(10)
a.agregar_destino(11)
a.agregar_destino(12)