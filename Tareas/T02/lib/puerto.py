__author__ = 'Vicente'

import lib.estructura_datos as datos


class ListaPuertos(datos.Lista):
    def __init__(self):
        super().__init__()
        self.ultimo_agregado = None
        self.cantidad_puertos = 0

    def agregar_puerto(self, puerto):
        nuevo_puerto = puerto
        nodo_puerto = self.buscar_nodo(puerto.id)

        if not self.primero:
            self.primero = nuevo_puerto
            self.ultimo_agregado = self.primero
            self.cantidad_puertos += 1

        elif not nodo_puerto:
            self.ultimo_agregado.hijos.add(nuevo_puerto)  # agregar nuevo puerto como hijo del ultimo.
            nuevo_puerto.padres.add(self.ultimo_agregado)  # agregar ultimo como padre del nuevo.
            self.ultimo_agregado = nuevo_puerto
            self.cantidad_puertos += 1

        else:
            self.ultimo_agregado.hijos.add(nodo_puerto)
            nodo_puerto.padres.add(self.ultimo_agregado)
            self.ultimo_agregado = nodo_puerto
            self.cantidad_puertos += 1

    def recorrer_conexiones(self, conexiones_a_bummer):
        pass


class Puerto(datos.Nodo):
    def __init__(self, id):
        super().__init__()
        self.padres = datos.Lista()
        self.hijos = datos.Lista()
        self.id = id
        self.posibles_conexiones = 0
        self.futura_conexion = self.iter_conexiones()
        self.conexiones = datos.Lista()

    def agregar_conexion(self, conexion):
        if conexion.id not in self.conexiones:
            self.conexiones.add(conexion)

    def iter_conexiones(self):
        conexiones = self.posibles_conexiones
        while True:
            for i in range(conexiones):
                yield i

    def decidir_conexion(self):
        return next(self.futura_conexion)

    def __repr__(self):
        return "PUERTO ID{}".format(self.id)
