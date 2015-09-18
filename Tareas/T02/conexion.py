__author__ = 'Vicente'

from datos import Lista, Nodo


class Conexion:

    def __init__(self, id, inicio, lista):
        self.id = id
        self.inicio = inicio
        self.destinos = lista
        self.tipo = self.get_tipo()

    def get_tipo(self):
        tipo = ""
        destinos_unicos = Lista()
        for destino in self.destinos:
            if destino not in destinos_unicos:
                destinos_unicos.add_nodo(Nodo(destino))

        if len(destinos_unicos) == 2:
            tipo = "ALT"

        if len(destinos_unicos) > 2:
            tipo = "RAND"

        self.destinos = destinos_unicos
        return tipo

    def __repr__(self):
        retorno = ""
        for destino in self.destinos:
            retorno += "CONEXION ID{} ID{} \n".format(self.inicio, destino)
        return retorno



