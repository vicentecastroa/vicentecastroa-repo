__author__ = 'Vicente'
# coding=UTF-8

from lib.interfaz import Interfaz
from lib.jugadores import Jugador, Computador


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
        jugador_2 = Computador(jugador_1)

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
        if not isinstance(activo, Computador):
            while activo.jugando:
                opcion = interfaz.menu_principal()
                if opcion == "V":
                    seleccion = interfaz.mostrar_vehiculos(activo)
                    try:
                        vehiculo_sel = seleccion[0]
                        mapa_sel = seleccion[1]
                        interfaz.menu_vehiculo(activo, pasivo, vehiculo_sel, mapa_sel)
    
                    except TypeError:
                        pass

                if opcion == "R":
                    interfaz.radar(activo)

        elif isinstance(activo, Computador):
            activo.jugar()

        activo.jugando = False
        pasivo.jugando = True

    veredicto = interfaz.det_muerto(lista_jugadores)
    print("Enhorabuena {}! A derrotado a {}".format(veredicto[1], veredicto[2]))
    print("\nEstadísticas del juego")
    interfaz.estadisticas()
