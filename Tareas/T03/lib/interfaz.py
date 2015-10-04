__author__ = 'Vicente'
 # coding=UTF-8

import mapa
import time
from random import randint


class Jugador:

    def __init__(self, nombre):
        self.nombre = nombre
        self.turno = 0
        self.mapas_propios = dict()
        self.mapa_ataques = None
        self.vivo = True

    def finalizar_turno(self):
        map(lambda mapa: mapa.cerrar_mapa(), self.mapas_propios.values())
        self.turno += 1
        return None

    def __repr__(self):
        return self.nombre.capitalize()


class Computador(Jugador):

    def __init__(self):
        super().__init__("computador")


def crear_mapas(jugadores):
    for jugador in jugadores:
        opcion = input("""
        {} ubique sus vehículos".format(jugador)

        """)
    return True


def sorteo(jugadores):
    for _ in range(10):
        x = randint(0, 1)
        print("COMIENZA JUGANDO {}".format(jugadores[x]), end="\r")
        time.sleep(0.4)
    return jugadores[x]



if __name__ == '__main__':
    print("    BIENVENIDO AL BATTLESHIP")

    jugadores = input("""
    Cantidad de jugadores:
    [1] 1 Jugador
    [2] 2 Jugadores
    """)
    jugador1 = Jugador(input("Nombre jugador 1: ").upper())
    if jugadores == "2":
        jugador2 = Jugador(input("Nombre jugador 1: ").upper())
    else:
        jugador2 = Computador()
    jugadores = [jugador1, jugador2]
    crear_mapas(jugadores)

    print("\n\n\n    COMIENZA EL JUEGO")
    partidor = sorteo(jugadores)
    # while True:
    # usar jugador x
    # mostrar mapa

    opcion1 = (input("""
    Elija una opción
    [V] Vehículos
    [R] Radar
    [B] Volver
    """)).upper()

    opcion2 = (input("""
    Elija una opción
    [A] Atacar
    [M] Mover
    [B] Volver
    """)).upper()

    print("Ha terminado su turno")

