__author__ = 'Vicente'
# coding=UTF-8

from lib.mapa import MapaMar, MapaAire
from lib.ataques import Paralizer, Kamikaze, Tomahawk, Explorar
from lib.vehiculos import Explorador
from lib.jugadores import Computador
import lib.celdas as celdas
import time
from random import randint


class Interfaz:
    def __init__(self, jugador1, jugador2):
        self.jugador1 = jugador1
        self.jugador2 = jugador2

    def crear_mapas(self):
        for jugador in [self.jugador1, self.jugador2]:
            if not isinstance(jugador, Computador):
                opcion = input("""
        {} ubique sus vehículos
        [1] Random
        [2] Manual
                """.format(jugador))
                if self.opcion_valida(opcion, ["1", "2"]):
                    for mapa in jugador.mapas_propios.values():
                        if opcion == "1":
                            mapa.posicionar_random()
                        if opcion == "2":
                            mapa.posicionar_manual()

    def sorteo(self):
        jugadores = [self.jugador1, self.jugador2]
        veces = randint(8, 15)
        x = 0
        for _ in range(veces):
            if x == 0:
                x = 1
            elif x == 1:
                x = 0
            print("SORTEO: {}".format(jugadores[x]), end="\r")
            time.sleep(0.25)

        print("COMIENZA JUGANDO {}".format(jugadores[x]))
        return jugadores[x]

    def opcion_valida(self, ingresada, lista_valid):
        if ingresada not in lista_valid:
            print("Ingrese una opción válida, por favor.")
            return False
        return True

    def menu_principal(self):
        opcion = (input("""
        Elija una opción
        [V] Vehículos
        [R] Radar
        """)).upper()
        return opcion

    def radar(self, jugador):
        print("RADAR")
        for ataque in jugador.historial_ataques:
            print("Turno: {} | Ataque: {} | Coordenada: {} | Exito: {}".format(ataque[0],
                                                                               ataque[1],
                                                                               ataque[2],
                                                                               ataque[3]
                                                                               ))
        return None

    def mostrar_vehiculos(self, jugador):
        try:
            mapa = jugador.mapas_propios[input("""
            Seleccione el mapa
            [A] Aire
            [M] Mar
                """).upper()]
        except KeyError:
            print("Ingrese una opción válida")
            return None
        print("Seleccione un vehículo")
        for i in range(len(mapa.vehiculos_actual)):
            vehiculo = mapa.vehiculos_actual[i]
            print("[{}] {} [res: {}]".format(i + 1, vehiculo, vehiculo.resistencia))
        try:
            vehiculo = mapa.vehiculos_actual[int(input()) - 1]
            print("Ha seleccionado {}".format(vehiculo))
            return vehiculo, mapa
        except IndexError:
            print("Opción ingresada no válida")
        except ValueError:
            print("Opción ingresada no válida")

    def menu_vehiculo(self, jugador, pasivo, vehiculo, mapa):
        print("""
        Elija una opción
        """)
        vehiculo.menu()
        opcion = input("").upper()
        if opcion == "R":
            self.reparar(jugador, vehiculo)
        if opcion == "A":
            ataque = self.menu_ataques(vehiculo)
            self.set_ataque(jugador, pasivo, ataque)
            jugador.finalizar_turno()
        if opcion == "M":
            mapa.mover_elemento(vehiculo)
            vehiculo.mostrarse()
            jugador.finalizar_turno()
        if opcion == "E":
            self.explorar(jugador, vehiculo, pasivo)
        if opcion == "V":
            return None

    def menu_ataques(self, vehiculo):
        try:
            vehiculo.menu_ataques()
            opcion = int(input("").upper()) - 1
            return vehiculo.ataques[opcion]
        except IndexError:
            print("Opción ingresada no válida")

        except TypeError:
            print("Ingresar el número correspondiente")

    def set_ataque(self, atacante, defensor, ataque):
        ataque = ataque
        if not ataque.disponible:
            print("Este ataque no está disponible. Espere {} turnos".format(str(ataque.espera-ataque.turnos_espera)))
            return False
        if ataque.disponible:
            if not isinstance(ataque, Paralizer):
                mapa_enemigo = defensor.mapas_propios["M"]
            elif isinstance(ataque, Paralizer):
                mapa_enemigo = defensor.mapas_propios["A"]
            if not isinstance(ataque, Kamikaze):
                print("Atacará con {} [rango: {}] [daño: {}]".format(ataque, ataque.size, ataque.damage))
            if isinstance(ataque, Kamikaze):
                print("Realizará un ataque kamikaze. Su avión se destruirá si acerta al objetivo")
            coordenadas = input("Ingrese coordenadas: ")
            coordenada_ataque = None
            while not coordenada_ataque:
                coordenada_ataque = celdas.coord_to_index(coordenadas)
                ataque.coordenada_ataque = coordenada_ataque
            if isinstance(mapa_enemigo, MapaMar):
                return self.atacar_mar(atacante, ataque, mapa_enemigo)
            elif isinstance(mapa_enemigo, MapaAire):
                return self.atacar_aire(atacante, mapa_enemigo)

    def atacar_mar(self, atacante, ataque, mapa):
        exitos = list()
        exito = "No"
        for celda in celdas.celdas_ocupadas(ataque.coordenada_ataque, ataque.size):
            exito = "No"
            resultado_ataque = mapa.get_elemento(celda)
            if resultado_ataque[0] and resultado_ataque[0] not in exitos:
                vehiculo_atacado = resultado_ataque[0]
                exito = "Si"
                exitos.append(vehiculo_atacado)
                if not vehiculo_atacado.atacado(ataque):
                    mapa.borrar_elemento(vehiculo_atacado)
                if isinstance(ataque, Tomahawk) or isinstance(ataque, Explorar):
                    print("Exito: {}".format(vehiculo_atacado))
                else:
                    print("Ataque exitoso: {}".format(celdas.index_to_coord(celda)))
        ataque.usar()
        atacante.historial_ataques.append((atacante.turno,
                                           ataque,
                                           celdas.index_to_coord(ataque.coordenada_ataque),
                                           exito
                                           ))

    def atacar_aire(self, atacante, ataque, mapa):
        resultado_ataque = mapa.get_elemento(ataque.coordenada_ataque, ataque.size)
        exito = "No"
        if isinstance(resultado_ataque[0], Explorador) and resultado_ataque[1] is True:
            vehiculo = resultado_ataque[0]
            vehiculo.atacado(ataque)
            exito = "Si"
        ataque.usar()
        atacante.historial_ataques.append((atacante.turno, ataque, ataque.coordenada_ataque, exito))

    def explorar(self, jugador, vehiculo, defensor):
        ataque = vehiculo.ataques[0]
        coordenadas = input("Ingrese coordenadas: ")
        coordenada_ataque = None
        while not coordenada_ataque:
            coordenada_ataque = celdas.coord_to_index(coordenadas)
            ataque.coordenada_ataque = coordenada_ataque
        self.atacar_mar(jugador, ataque, defensor.mapas_propios["M"])

    def reparar(self, jugador, puerto):
        print("REPARACIÓN VEHÍCULO")
        resultado = self.mostrar_vehiculos(jugador)
        vehiculo_sel = resultado[0]
        vehiculo_sel.atacado(puerto.ataques[0].damage)

    def det_jugando(self, lista_jugadores):
        activo = None
        pasivo = None
        for jugador in lista_jugadores:
            if jugador.jugando:
                activo = jugador
            else:
                pasivo = jugador
        return activo, pasivo

    def det_muerto(self, lista_jugadores):
        vivo = None
        muerto = None
        for jugador in lista_jugadores:
            if jugador.vivo:
                vivo = jugador
            else:
                muerto = jugador
        return muerto, vivo


    def estadisticas(self):
        pass

