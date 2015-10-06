__author__ = 'Vicente'
# coding=UTF-8

import string
from random import randint
from vehiculos import BarcoPequeno, BuqueGuerra, Lancha, Puerto, Explorador, KamikazeAvion, Caza
import celdas


class Mapa:
    def __init__(self):
        self.dimension = 15
        self.n_mapa = 0
        self.historial = {0: list()}
        self.grilla_actual = self.grilla_default()
        self.vehiculos_actual = list()
        self.vehiculos_disponibles = None

    def grilla_default(self):
        grilla = [["_" for _ in range(self.dimension)] for _ in range(self.dimension)]
        return grilla

    def posicionar_random(self):
        vehiculos = self.vehiculos_disponibles
        for vehiculo in vehiculos.values():
            while not vehiculo.pos_actual:
                posicion = (randint(0, 14 - vehiculo.size[0]), randint(0, 14 - vehiculo.size[1]))
                self.ubicar_elemento(vehiculo, posicion)
        self.cerrar_mapa()
        self.mostrar_mapa(1)

    def posicionar_manual(self):
        vehiculos = self.vehiculos_disponibles
        for vehiculo in vehiculos.values():
            while not vehiculo.pos_actual:
                celda = None
                while not celda:
                    coordenada_ingresada = input("Ingrese coordenada para {}: ".format(vehiculo))
                    celda = celdas.coord_to_index(coordenada_ingresada)
                self.ubicar_elemento(vehiculo, celda)
        self.cerrar_mapa()
        self.mostrar_mapa(1)
        return True

    def cerrar_mapa(self):
        self.n_mapa += 1
        self.historial[self.n_mapa] = self.vehiculos_actual

    def mostrar_mapa(self, turno):
        numeros = list(map(lambda x: str(x + 1), range(self.dimension)))
        grilla = self.grilla_default()
        for elemento in self.historial[turno]:
            celdas_ocupadas = elemento.celdas_ocupadas(elemento.pos_actual)
            for celda in celdas_ocupadas:
                grilla[celda[0]][celda[1]] = elemento.id
        self.grilla_actual = grilla
        self.encabezado()
        for i in range(len(grilla)):
            numero = numeros[i]
            if int(numero) < 10:
                numero = "0{}".format(numeros[i])
            print("{}".format(numero), grilla[i])

    def encabezado(self):
        letras = list(map(lambda x: x, string.ascii_uppercase))
        letras.insert(0, "__")
        print("________________MAPA {}_________________ \n".format(self.nombre))

        for i in range(self.dimension + 1):
            if not i == self.dimension:
                print(letras[i], end="    ")
            else:
                print(letras[i])

    def ubicar_elemento(self, elemento, posicion):
        if self.check_espacio(elemento, posicion):
            elemento.pos_actual = posicion
            try:
                lista_vehiculos = [elemento for elemento in self.vehiculos_actual]
            except TypeError:
                lista_vehiculos = list()
            if elemento not in lista_vehiculos:
                lista_vehiculos.append(elemento)
            self.vehiculos_actual = lista_vehiculos
            return True

    def borrar_elemento(self, elemento):
        if elemento in self.vehiculos_actual:
            lista_vehiculos = [elemento for elemento in self.vehiculos_actual]
            lista_vehiculos.remove(elemento)
            self.vehiculos_actual = lista_vehiculos
            return True

    def mover_elemento(self, vehiculo):
        if not isinstance(vehiculo, Lancha):
            direccion = input("""
            Mover en dirección:
            Q   W   E
            A   -   D
            Z   X   C
            """).upper()
        if isinstance(vehiculo, Lancha):
            direccion = None
            while not direccion:
                direccion = celdas.coord_to_index(input("     Ingrese coordenadas de destino:"))

        self.ubicar_elemento(vehiculo, vehiculo.mover(direccion))

    def check_espacio(self, elemento, posicion):
        celdas_ocupadas = self.casillas_ocupadas()
        celdas_nuevas = elemento.celdas_ocupadas(posicion)
        for casilla in celdas_nuevas:
            if casilla in celdas_ocupadas:
                return False
            if casilla[0] >= 15 or casilla[1] >= 15:
                return False
        return True

    def casillas_ocupadas(self):
        vehiculos_puestos = self.vehiculos_actual
        celdas_ocupadas = list()
        for vehiculo in vehiculos_puestos:
            for celda in vehiculo.celdas_ocupadas(vehiculo.pos_actual):
                celdas_ocupadas.append(celda)
        return celdas_ocupadas

    def get_elemento(self, coordenada):
        for vehiculo in self.vehiculos_actual:
            for celda in vehiculo.celdas_ocupadas(vehiculo.pos_actual):
                if coordenada == celda:
                    return vehiculo
        return None

    def __repr__(self):
        return "MAPA"


class MapaAire(Mapa):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = "AIRE jugador: {}".format(nombre)
        self.vehiculos_disponibles = {"explorador": Explorador(),
                                      "kamikaze": KamikazeAvion(),
                                      "caza": Caza()
                                      }


class MapaMar(Mapa):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = "MAR jugador: {}".format(nombre)
        self.vehiculos_disponibles = {"barco": BarcoPequeno(),
                                      "buque": BuqueGuerra(),
                                      "lancha": Lancha(),
                                      "puerto": Puerto()
                                      }
