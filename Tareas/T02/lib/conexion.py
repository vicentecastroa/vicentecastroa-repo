__author__ = 'Vicente'

import lib.estructura_datos as datos


class Conexion:
    def __init__(self, id, desde):
        self.id = id
        self.desde = desde
        self.destinos = datos.Lista()  #sobreescribir contain

        self.tipo = None
        self.visitas = 0

    def agregar_destino(self, destino):
        if destino not in self.destinos:
            destino = datos.Nodo(destino)
            self.destinos.add(destino)
            self.visitas += 1
        pass

    def get_tipo(self):
        cantidad_destinos = self.destinos.largo
        if cantidad_destinos == 1:
            self.tipo = "dirigida"
        if cantidad_destinos == 2:
            self.tipo = "alternante"
        if cantidad_destinos <=3:
            self.tipo = "aleatoria"

    def __contains__(self, id):  # if id in lista
        for nodo in self:
            if nodo.valor == id:
                return True
        return False

    def __repr__(self):
        retorno = ""
        id_desde = self.desde.id
        for destino in self.destinos:
            id_destino = destino.valor
            retorno += "CONEXION ID{} ID{}\n".format(id_desde, id_destino)

        return retorno
