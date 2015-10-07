__author__ = 'Vicente'
# coding=UTF-8

from mapa import MapaMar, MapaAire
from ataques import Paralizer, Kamikaze, Tomahawk, Explorar
from vehiculos import Explorador
import time
from random import randint
import celdas


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
        map(lambda mapa: mapa.cerrar_mapa(), self.mapas_propios.values())
        for mapa in self.mapas_propios.values():
            for vehiculo in mapa.vehiculos_actual:
                for ataque in vehiculo.ataques:
                    ataque.actualizar_disponibilidad()
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

    def __init__(self):
        super().__init__("computador")


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
        vehiculo = mapa.vehiculos_actual[int(input()) - 1]
        print("Ha seleccionado {}".format(vehiculo))
        return vehiculo, mapa

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
        vehiculo.menu_ataques()
        opcion = int(input("").upper()) - 1
        return vehiculo.ataques[opcion]

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
                print("Realizará un ataque kamikaze. Su avión se destruirá luego de atacar")
            coordenadas = input("Ingrese coordenadas: ")
            coordenada_ataque = None
            while not coordenada_ataque:
                coordenada_ataque = celdas.coord_to_index(coordenadas)
                ataque.coordenada_ataque = coordenada_ataque
            if isinstance(mapa_enemigo, MapaMar):
                return self.atacar_mar(atacante, defensor, ataque, mapa_enemigo)
            elif isinstance(mapa_enemigo, MapaAire):
                return self.atacar_aire(atacante, ataque, mapa_enemigo)

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
        atacante.historial_ataques.append((atacante.turno, ataque, ataque.coordenada_ataque, exito))

    def atacar_aire(self, atacante, ataque, mapa):
        resultado_ataque = mapa.get_elemento(ataque.coordenada_ataque, ataque.size)
        exito = "No"
        if isinstance(resultado_ataque[0], Explorador) and resultado_ataque[1] is True:
            vehiculo = resultado_ataque[0]
            vehiculo.atacado(ataque)
            exito = "Si"
        ataque.usar()
        atacante.historial_ataques.append((atacante.turno, ataque, ataque.coordenada_ataque, exito))
        pass

    def explorar(self,jugador, vehiculo, defensor):
        ataque = vehiculo.ataques
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
        vehiculo_sel.cambiar_resistencia(puerto.ataque.damage)

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


if __name__ == '__main__':
    print("    BIENVENIDO AL BATTLESHIP")

    cant_jugadores = input("""
    Cantidad de jugadores:
    [1] 1 Jugador
    [2] 2 Jugadores
    """)
    jugador_1 = Jugador(input("Nombre jugador 1: ").upper())
    if cant_jugadores == "2":
        jugador_2 = Jugador(input("Nombre jugador 2: ").upper())
    else:
        jugador_2 = Computador()

    interfaz = Interfaz(jugador_1, jugador_2)
    interfaz.crear_mapas()

    print("\n\n\n    COMIENZA EL JUEGO\n")
    jugador = interfaz.sorteo()
    jugador.jugando = True
    lista_jugadores = [jugador_1, jugador_2]

    while jugador_1.vivo and jugador_2.vivo:
        jugadores = interfaz.det_jugando(lista_jugadores)
        activo = jugadores[0]
        pasivo = jugadores[1]
        print("Es el turno de {}".format(activo))
        while activo.jugando:
            opcion = interfaz.menu_principal()
            if opcion == "V":
                seleccion = interfaz.mostrar_vehiculos(jugador_1)
                vehiculo_sel = seleccion[0]
                mapa_sel = seleccion[1]
                interfaz.menu_vehiculo(jugador_1, jugador_2, vehiculo_sel, mapa_sel)
            if opcion == "R":
                interfaz.radar(activo)

        activo.jugando = False
        pasivo.jugando = True

    veredicto = interfaz.det_muerto(lista_jugadores)
    print("Enhorabuena {}! A derrotado a {}".format(veredicto[1], veredicto[2]))
    print("Estadísticas del juego")


