__author__ = 'Vicente'

import lib.estructura_datos as datos


class Conexion(datos.Nodo):
    def __init__(self, id, desde):
        super().__init__()
        self.id = id
        self.desde = desde
        self.destinos = datos.Lista()

        self.tipo = None
        self.visitas = 0

    def agregar_destino(self, destino):
        if destino not in self.destinos:
            self.destinos.add(destino)
        self.visitas += 1

    def get_tipo(self):
        cantidad_destinos = self.destinos.largo
        if cantidad_destinos == 1:
            self.tipo = ""
        if cantidad_destinos == 2:
            self.tipo = "ALT"
        if cantidad_destinos <=3:
            self.tipo = "RAND"

    def __contains__(self, id):  # if id in lista
        for nodo in self:
            if nodo.id == id:
                return True
        return False

    def __repr__(self):
        retorno = "CONEXION ID{} ID{}".format(self.desde, self.destino)
        return retorno