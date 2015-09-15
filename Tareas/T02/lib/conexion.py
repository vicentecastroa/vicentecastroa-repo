__author__ = 'Vicente'

import lib.estructura_datos as datos


class Conexion:
    def __init__(self, id, desde):
        self.id = id
        self.desde = desde
        self.destinos = datos.Lista()
        self.tipo = None
        self.visitas = 0

    def agregar_destino(self, destino):
        destino = datos.Nodo(destino)
        self.destinos.add(destino)
        self.visitas = 0

    def get_tipo(self):
        for i in range(self.destinos.largo):
            pass

    def __repr__(self):
        return "CONEXION desde {}".format(self.desde)