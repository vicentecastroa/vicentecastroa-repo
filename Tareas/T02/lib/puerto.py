__author__ = 'Vicente'

import lib.estructura_datos as datos


class ListaPuertos:  # Se inicializa con el puerto inicial 0
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.cantidad_puertos = 0

    def agregar_puerto(self, puerto):
        if not self.buscar_puerto(puerto.id):
            a = self.ultimo
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
            for i in range(actual.hijos.cantidad_puertos):
                hijo = actual.hijos.get(i)
                hijo.hijos.buscar_puerto(id)
        return False


class Puerto:
    def __init__(self, id):
        self.id = id
        self.visitas = 0
        self.hijos = ListaPuertos()
        self.padres = ListaPuertos()
        self.conexiones = datos.Lista()

    def agregar_hijo(self, puerto_hijo):
        cantidad_hijos = self.hijos.cantidad_puertos
        if cantidad_hijos == 0:
            self.hijos.primero = puerto_hijo
            self.hijos.cantidad_puertos = 1
        else:
            self.hijos.agregar_puerto(puerto_hijo)

    def agregar_padre(self, puerto_padre):
        cantidad_padres = self.padres.cantidad_puertos
        if cantidad_padres == 0:
            self.padres.primero = puerto_padre
            self.hijos.cantidad_puertos = puerto_padre
        else:
            self.padres.agregar_puerto(puerto_padre)

    def agregar_conexion(self, conexion):
        conexion = datos.Nodo(conexion)
        self.conexiones.add(conexion)
        self.visitas += 1

    def __repr__(self):
        return "PUERTO ID{}".format(self.id)
