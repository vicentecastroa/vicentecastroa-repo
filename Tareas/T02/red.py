__author__ = 'Vicente'

import sistema as sis
import lib.conexion as conexion
import lib.puerto as puerto
import random

class Red:
    def __init__(self):
        self.lista_puertos = puerto.ListaPuerto()
        self.bummer = sis.puerto_final()

    def recorrer(self):
        while sis.preguntar_puerto_actual()[0] != self.bummer:
            puerto_actual = self.lista_puertos.get_ultimo().valor  # sis.preguntar_puerto_actual()[0]
            self.siguiente(puerto_actual)

    def siguiente(self, actual):
        posibles = sis.posibles_conexiones()
        id_conexion = random.randint(0, posibles)
        nueva_conexion = conexion.Conexion(id_conexion, actual)
        sis.hacer_conexion(nueva_conexion.id)
        nuevo = sis.preguntar_puerto_actual()
        nuevo_puerto = puerto.Puerto(nuevo[0])
        nueva_conexion.agregar_destino(nuevo_puerto.id)
        actual.agregar_conexion(nueva_conexion)
        self.lista_puertos.agregar_puerto(nuevo_puerto)
        pass
