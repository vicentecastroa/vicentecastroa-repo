__author__ = 'Vicente'
# coding=UTF-8

from mapa import MapaMar, MapaAire
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
                vehiculo.ataque.actualizar_disponibilidad()
            mapa.mostrar_mapa(mapa.n_mapa)
        self.turno += 1
        # self.jugando = False

        print("Su turno ha finalizado")
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
        for _ in range(10):
            x = randint(0, 1)
            print("COMIENZA JUGANDO {}".format(jugadores[x]), end="\r")
            time.sleep(0.4)
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
        if not isinstance(vehiculo, Puerto):
            opcion = input("""
            Elija una opción
            [A] Atacar
            [M] Mover
            [V] Volver
            """).upper()
        if isinstance(vehiculo, Puerto):
            opcion = input("""
            Elija una opción
            [R] Reparar vehiculos
            [V] Volver
            """).upper()
        if isinstance(vehiculo, Lancha):
            opcion = input("""
            Elija una opción
            [M] Mover
            [V] Volver
            """).upper()
        if opcion == "R":
            self.reparar(jugador, vehiculo)
        if opcion == "A":
            self.atacar(jugador, pasivo, vehiculo)
        if opcion == "M":
            mapa.mover_elemento(vehiculo)
        if opcion == "V":
            return None

    def atacar(self, atacante, defensor, vehiculo):
        ataque = vehiculo.ataque
        mapa_enemigo = defensor.mapas_propios["M"]
        if ataque.disponible:
            print("Atacará con {} [rango: {}] [daño: {}]".format(ataque, ataque.cobertura, ataque.damage))
            coordenadas = input("Ingrese coordenadas: ")
            coordenada_ataque = None
            while not coordenada_ataque:
                coordenada_ataque = celdas.coord_to_index(coordenadas)
                ataque.coordenada_ataque = coordenada_ataque
            exitos = list()
            exito = "No"
            for celda in ataque.celdas_ocupadas(ataque.coordenada_ataque):
                vehiculo_atacado = mapa_enemigo.get_elemento(celda)
                if vehiculo_atacado and vehiculo_atacado not in exitos:
                    exito = "Si"
                    exitos.append(vehiculo_atacado)
                    if not vehiculo_atacado.cambiar_resistencia(ataque.damage):  # si mato
                        mapa_enemigo.borrar_elemento(vehiculo_atacado)
                    print("Ataque exitoso: {}".format(celdas.index_to_coord(celda)))
            ataque.usar()
            atacante.historial_ataques.append((atacante.turno, ataque, coordenada_ataque, exito))
        atacante.finalizar_turno()
        return None

    def reparar(self, jugador, puerto):
        print("REPARACIÓN VEHÍCULO")
        resultado = self.mostrar_vehiculos(jugador)
        vehiculo_sel = resultado[0]
        vehiculo_sel.cambiar_resistencia(puerto.ataque.damage)

    def det_jugando(self, lista_jugadores):
        activo = filter(lambda x: x.jugando is True, lista_jugadores)
        pasivo = filter(lambda x: x.jugando is False, lista_jugadores)
        return activo, pasivo

    def det_muerto(self, lista_jugadores):
        vivo = filter(lambda x: x.vivo is True, lista_jugadores)
        muerto = filter(lambda x: x.vivo is False, lista_jugadores)
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

    print("\n\n\n    COMIENZA EL JUEGO")
    jugador = interfaz.sorteo()
    jugador.jugando = True
    lista_jugadores = [jugador_1, jugador_2]

    while jugador_1.vivo and jugador_2.vivo:
        jugadores = interfaz.det_jugando(lista_jugadores)
        activo = jugadores[0]
        pasivo = jugadores[1]
        print("Es el turno de {}".format(activo))
        opcion = interfaz.menu_principal()
        if opcion == "V":
            seleccion = interfaz.mostrar_vehiculos(jugador_1)
            vehiculo_sel = seleccion[0]
            mapa_sel = seleccion[1]
            interfaz.menu_vehiculo(jugador_1, jugador_2, vehiculo_sel, mapa_sel)
        if opcion == "R":
            interfaz.radar(jugador_1)

        activo.jugando = False
        pasivo.jugando = True

    veredicto = interfaz.det_muerto(lista_jugadores)
    print("Enhorabuena {}! A derrotado a {}".format(veredicto[1], veredicto[2]))
    print("Estadísticas del juego")


