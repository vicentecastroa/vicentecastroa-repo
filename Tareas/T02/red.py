__author__ = 'Vicente'

import sistema as sis
import lib.conexion as conexion
import lib.puerto as puerto
import random


class Red:
    def __init__(self):
        self.lista_puertos = puerto.ListaPuertos()
        self.bummer = sis.puerto_final()

    def recorrer(self):
        self.lista_puertos.primero = puerto.Puerto(0)
        self.lista_puertos.ultimo = self.lista_puertos.primero
        self.lista_puertos.cantidad_puertos = 1

        while sis.preguntar_puerto_actual()[0] != self.bummer:
            puerto_actual = puerto.Puerto(sis.preguntar_puerto_actual()[0])  # sis.preguntar_puerto_actual()[0]
            self.siguiente(puerto_actual)

    def siguiente(self, actual):
        id_conexion = random.randint(0, sis.posibles_conexiones())
        nueva_conexion = conexion.Conexion(id_conexion, actual)

        sis.hacer_conexion(nueva_conexion.id)

        nuevo_puerto = puerto.Puerto(sis.preguntar_puerto_actual()[0])
        nueva_conexion.agregar_destino(nuevo_puerto.id)

        actual.agregar_conexion(nueva_conexion)
        self.lista_puertos.agregar_puerto(nuevo_puerto)

        pass
