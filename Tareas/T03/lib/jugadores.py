__author__ = 'Vicente'
# coding=UTF-8
from lib.mapa import MapaMar, MapaAire
from lib.celdas import celdas_ocupadas
from lib.vehiculos import Lancha
import random


class Jugador:

    def __init__(self, nombre):
        self.nombre = nombre
        self.turno = 0
        self.mapas_propios = {"A": MapaAire(self.nombre),
                              "M": MapaMar(self.nombre)
                              }
        self.historial_ataques = list()
        self.vivo = True
        self.jugando = False

    def finalizar_turno(self):
        for mapa in self.mapas_propios.values():
            mapa.cerrar_mapa()
            for vehiculo in mapa.vehiculos_actual:
                vehiculo.actualizar_ataques()
            mapa.mostrar_mapa(mapa.n_mapa)
        self.turno += 1
        self.jugando = False

        print("Su turno ha finalizado \n\n\n")
        return None

    def volver_menu_principal(self):
        return None

    def __repr__(self):
        return self.nombre.capitalize()


class Computador(Jugador):

    def __init__(self, enemigo):
        super().__init__("computador")
        self.enemigo = enemigo
        self.crear_mapas()
        self.celda_exito = None

    def crear_mapas(self):
        for mapa in self.mapas_propios.values():
            mapa.posicionar_random()

    def jugar(self):
        if not self.celda_exito:
            opciones = {"buscar": self.buscar_algo,
                        "atacar": self.atacar_random,
                        "mover": self.mover_random
                        }
            a = random.choice(["buscar", "atacar", "mover"])
            opciones[a]()

        elif self.celda_exito:
            self.atacar_dirigido(self.celda_exito)
        self.finalizar_turno()

    def buscar_algo(self):
        celda = (random.randint(0, 14), random.randint(0, 14))
        for celda in celdas_ocupadas(celda, (3, 3)):
            resultado = self.enemigo.mapas_propios["M"].get_elemento(celda)
            if resultado[0]:
                self.celda_exito = celda

    def atacar_dirigido(self, celda):
        vehiculo = random.choice(self.mapas_propios["M"].vehiculos_actual)
        for ataque in vehiculo.ataques:
            if ataque.disponible:
                resultado_ataque = self.enemigo.mapas_propios["M"].get_elemento(celda)
                if resultado_ataque[0]:
                    if not resultado_ataque[0].atacado(ataque):
                        self.enemigo.mapas_propios["M"].borrar_elemento(resultado_ataque[0])
                        self.celda_exito = None
                else:
                    self.celda_exito = None
            ataque.usar()
            return None

    def atacar_random(self):
        celda = (random.randint(0, 14), random.randint(0, 14))
        self.atacar_dirigido(celda)

    def mover_random(self):
        mapa = self.mapas_propios[random.choice(["M", "A"])]
        direcciones = ["A", "Q", "W", "E", "Z", "X", "C", "D"]
        vehiculo = random.choice(mapa.vehiculos_actual)
        if isinstance(vehiculo, Lancha):
            a = vehiculo.mover((random.randint(0, 14), random.randint(0, 14)))
        else:
            a = vehiculo.mover(random.choice(direcciones))
        mapa.ubicar_elemento(vehiculo, a)