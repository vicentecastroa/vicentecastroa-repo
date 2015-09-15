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
        self.conexiones = datos.Lista()

    def agregar_hijo(self, puerto_hijo):
        if self.hijos.largo == 0:
            self.hijos.primero = puerto_hijo
            self.hijos.cantidad_puertos = 1
        else:
            self.hijos.add(puerto_hijo)

    def agregar_padre(self, puerto_padre):
        if self.padres.largo == 0:
            self.padres.primero = puerto_padre
            self.hijos.cantidad_puertos = puerto_padre
        else:
            self.padres.add(puerto_padre)

    def agregar_conexion(self, conexion):
        conexion = datos.Nodo(conexion)
        self.conexiones.add(conexion)
        self.visitas += 1

    def __repr__(self):
        return "PUERTO ID{}".format(self.id)
