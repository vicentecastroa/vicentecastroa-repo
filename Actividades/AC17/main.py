__author__ = 'Vicente'
from collections import deque
from random import randint, random
from random import expovariate
import numpy as np


class Jugador:
    def __init__(self):
        self.habilidad = np.random.uniform(1, 10)
        self.veces_jugadas = 0

    def seguir_jugando(self):
        if self.veces_jugadas > 10:
            return False

    def __repr__(self):
        return "Jugador (hab: {})".format(self.habilidad)


class Mesa:
    def __init__(self, jugadores):
        self.partido_actual = None
        self.tiempo_partido = np.random.uniform(4, 6)
        self.jugadores_actuales = jugadores

    def nuevo_jugador(self, jugador):
        self.jugadores_actuales.append(jugador)
        self.tiempo_partido = np.random.uniform(4, 6)

    def det_ganador(self):
        ganar_1 = self.jugadores_actuales[0] * randint(1, 10)
        ganar_2 = self.jugadores_actuales[1] * randint(1, 10)
        if ganar_1 >= ganar_2:
            return self.jugadores_actuales[0]
        return self.jugadores_actuales[1]

class Simulacion:
    def __init__(self, t_max_simulacion, tasa_llegada_a_cola):
        self.tiempo_max_simulacion = t_max_simulacion
        self.tasa_llegada = tasa_llegada_a_cola
        self.tiempo_simulacion = 0
        self.tiempo_prox_jugador = 0
        self.cantidad_jugadores = 0
        self.t_promedio_jugado = 0
        self.t_espera_promedio = 0
        self.cola_espera = deque()
        self.mesa = None

    def proximo_jugador(self):
        self.tiempo_prox_jugador = self.tiempo_simulacion + round(expovariate(self.tasa_llegada) + 0.5)

    def run(self):
        # se parte con dos jugadores en la mesa y uno en la cola
        jug_1 = Jugador()
        jug_2 = Jugador()
        jug_3 = Jugador()
        self.mesa = Mesa([jug_1, jug_2])
        self.cola_espera.append(jug_3)
        self.cantidad_jugadores = 2
        print("Se ha iniciado la simulacion. Juegan {} y {}. Espera {}".format(jug_1, jug_2, jug_3))

        while self.tiempo_simulacion < self.tiempo_max_simulacion:
            # jugar partido y avanzar la simulacion hasta que termino el partido o llegue un nuevo jugador a la cola
            if self.tiempo_prox_jugador < self.mesa.tiempo_partido:
                self.tiempo_simulacion = self.tiempo_prox_jugador
            else:
                self.tiempo_simulacion = self.mesa.tiempo_partido

            print("[SIMULACION] Tiempo: {}".format(self.tiempo_simulacion))

            if self.tiempo_simulacion == self.tiempo_prox_jugador:
                # crear un jugador nuevo y ponerlo en la cola
                jugador_nuevo = Jugador()
                self.cola_espera.append(jugador_nuevo)
                print("[COLA] Se sumo {} a la cola en el tiempo {}".format(jugador_nuevo, self.tiempo_simulacion))


            if self.tiempo_simulacion == self.mesa.tiempo_partido:
                # Se termino el partido. Ver el ganador, el primero en la fila entra a la mesa.
                


if __name__ == '__main__':

    s = Simulacion(70, 1/15)
    s.run()
