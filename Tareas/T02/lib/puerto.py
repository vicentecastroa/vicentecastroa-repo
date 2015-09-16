__author__ = 'Vicente'

import lib.estructura_datos as datos


class ListaPuertos:  # Se inicializa con el puerto inicial 0
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.cantidad_puertos = 0

    def agregar_puerto(self, puerto):
        if not self.buscar_puerto(puerto.id):
            self.ultimo.agregar_hijo(puerto)
            puerto.agregar_padre(self.ultimo)
            self.ultimo = puerto
            self.cantidad_puertos += 1

        else:
            id_puerto = puerto.id
            puerto = self.buscar_puerto(id_puerto)
            puerto.agregar_hijo(puerto)
            puerto.agregar_padre(puerto)
            self.ultimo = puerto
            self.cantidad_puertos += 1

    def buscar_puerto(self, id):
        actual = self.primero
        if actual.id == id:
            return actual
        else:
            for hijo in actual.hijos:
                hijo.hijos.buscar_puerto(id)
        return False


class Puerto:
    def __init__(self, id):
        self.id = id
        self.visitas = 0
        self.hijos = datos.Lista()
        self.padres = datos.Lista()
        self.posibles_conexiones = 0
        self.futura_conexion = self.iter_conexiones()
        self.conexiones = datos.Lista()

    def agregar_hijo(self, puerto_hijo):
        puerto_hijo = datos.Nodo(puerto_hijo)
        if self.hijos.largo == 0:
            self.hijos.primero = puerto_hijo
            self.hijos.cantidad_puertos = 1
        elif puerto_hijo.valor.id not in self.hijos:
            self.hijos.add(puerto_hijo)

    def agregar_padre(self, puerto_padre):
        puerto_padre = datos.Nodo(puerto_padre)
        if self.padres.largo == 0:
            self.padres.primero = puerto_padre
            self.hijos.cantidad_puertos = puerto_padre
        elif puerto_padre.valor.id not in self.padres:
            self.padres.add(puerto_padre)

    def agregar_conexion(self, conexion):
        if conexion.id not in self.conexiones:
            conexion = datos.Nodo(conexion)
            self.conexiones.add(conexion)
            self.visitas += 1

    def iter_conexiones(self):
        conexiones = self.posibles_conexiones
        while True:
            for i in range(conexiones):
                yield i

    def decidir_conexion(self):  # hacer mas eficiente revisando el tipo de la conexion
        return next(self.futura_conexion)

    def __repr__(self):
        return "PUERTO ID{}".format(self.id)