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

        iteraciones = 1
        while self.saber_cuando_parar(iteraciones):
            puerto_actual = puerto.Puerto(sis.preguntar_puerto_actual()[0])  # sis.preguntar_puerto_actual()[0]
            puerto_actual.posibles_conexiones = sis.posibles_conexiones()
            self.siguiente(puerto_actual)
            iteraciones += 1

        # return self.imprimir_red()

    def siguiente(self, actual):
        ultimo = self.lista_puertos.ultimo
        ultimo.posibles_conexiones = actual.posibles_conexiones

        id_conexion = ultimo.decidir_conexion()
        nueva_conexion = conexion.Conexion(id_conexion, actual)
        ultimo.agregar_conexion(nueva_conexion)

        sis.hacer_conexion(nueva_conexion.id)

        nuevo_puerto = puerto.Puerto(sis.preguntar_puerto_actual()[0])
        ultimo.conexiones.get(id_conexion).valor.agregar_destino(nuevo_puerto.id)  #

        self.lista_puertos.agregar_puerto(nuevo_puerto)

    def saber_cuando_parar(self, iteraciones):
        if iteraciones % 10000 == 0: #revisar cada 20.000 iteraciones
            # para cada puerto
            # revisar si se paso por todas las conexiones un minimo de x veces
            return False
        return True

    def imprimir_red(self):
        # iterar sobre el los ids de los puertos
        # iterar sobre las conexiones de cada puerto
        # crear dos partes: una con puertos otra con conexiones
        # juntar ambas y crear red.txt
        pass

    def ruta_a_bummer(self):
        # DIKJSTRA()
        # crear rutaABummer.txt con CONEXIONES realizadas
        pass

    def dikjstra(self, id_inicio, id_final):
        pass

    def rutas_doble_sentido(self):
        # crear rutasDobleSentido.txt
        pass

    def obtener_ciclos(self):
        # obtener_triangulos()
        # obtener_cuadrados()
        # juntar y crear ciclos.txt
        pass

