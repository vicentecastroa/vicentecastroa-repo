__author__ = 'Vicente'

import lib.estructura_datos as datos

class ListaPuerto(datos.Lista):  # Se inicializa con el puerto inicial 0
    def __init__(self):
        super().__init__()
        self.primero = datos.Nodo(Puerto(0))
        self.ultimo = None
        self.largo = 1

    def agregar_puerto(self, puerto):
        puerto = datos.Nodo(puerto)
        for i in range(self.largo):
            if puerto == self.get(i):
                return "ya existe"
        ultimo = self.get_ultimo().valor
        ultimo.agregar_hijo(puerto.valor)
        self.add(puerto)
        puerto.valor.agregar_padre(puerto.anterior.valor)
        return


class Puerto:
    def __init__(self, id):
        self.id = id
        self.hijos = datos.Lista()
        self.padres = datos.Lista()
        self.conexiones = datos.Lista()

    def agregar_hijo(self, puerto_hijo):
        cantidad_hijos = self.hijos.largo
        if cantidad_hijos == 0:
            puerto_hijo = datos.Nodo(puerto_hijo)
            self.hijos.add(puerto_hijo)
        else:
            for i in range(cantidad_hijos):
                if puerto_hijo == self.padres.get(i):
                    return "el puerto ya es hijo"
                else:
                    puerto_hijo = datos.Nodo(puerto_hijo)
                    self.hijos.add(puerto_hijo)

    def agregar_padre(self, puerto_padre):
        cantidad_padres = self.padres.largo
        if cantidad_padres == 0:
            puerto_padre = datos.Nodo(puerto_padre)
            self.padres.add(puerto_padre)
        else:
            for i in range(self.padres.largo):
                if puerto_padre == self.padres.get(i):
                    return "el puerto ya se encuentra en los padres"
                else:
                    puerto_padre = datos.Nodo(puerto_padre)
                    self.padres.add(puerto_padre)

    def agregar_conexion(self, conexion):
        conexion = datos.Nodo(conexion)
        self.conexiones.add(conexion)

    def __repr__(self):
        return "PUERTO ID{}".format(self.id)
