__author__ = 'Vicente'
# coding=UTF-8

from random import randint
from ataques import Trident, Tomahawk, Napalm, Minuteman, Kamikaze, Paralizer, Ingenieros, Explorar
from celdas import celdas_ocupadas


class Vehiculo:

    def __init__(self, size, resistencia, id):
        self.size = size
        self.id = id
        self.pos_actual = tuple()
        self.resistencia = resistencia
        self.ataques = list()
        self.vivo = True

    def mover(self, direccion):
        try:
            direcciones = {"A": (0, -1),
                           "D": (0, 1),
                           "W": (-1, 0),
                           "X": (1, 0),
                           "Q": (-1, -1),
                           "E": (-1, 1),
                           "Z": (1, -1),
                           "C": (1, 1),
                           }
            cambio = direcciones[direccion]
            posicion_nueva = (self.pos_actual[0]+cambio[0], self.pos_actual[1]+cambio[1])
            return posicion_nueva
        except KeyError as err:
            print("{} no es una dirección válida".format(err))
            return False

    def atacado(self, ataque):
        if not isinstance(ataque, Paralizer):
            self.resistencia += ataque.damage
            if self.resistencia <= 0:
                print("""
    {} ha sido destruido.
    Estaba ocupando las celdas {}
            """.format(self, celdas_ocupadas(self.pos_actual, self.size)))
                return False  # mató
        return True  # sigue vivo

    def atacar(self):
        # pedir posicion ataque
        return None

    def menu(self):
        print("""
    [A] Atacar
    [M] Mover
    [V] Volver
        """)

    def menu_ataques(self):
        print("Elija un ataque")
        for i in range(len(self.ataques)):
            print("[{}] {}".format(i+1, self.ataques[i]))

    def mostrarse(self):
        pass


class VehiculoMar(Vehiculo):

    def __init__(self, *args):
        super().__init__(*args)


class VehiculoAire(Vehiculo):

    def __init__(self, *args):
        super().__init__(*args)


class BarcoPequeno(VehiculoMar):

    def __init__(self):
        super().__init__((3, 1), 30, "B")
        self.ataques = [Minuteman(), Paralizer()]

    def __repr__(self):
        return "Barco Pequeño"


class BuqueGuerra(VehiculoMar):

    def __init__(self):
        super().__init__((2, 3), 60, "G")
        self.ataques = [Tomahawk(), Paralizer()]

    def __repr__(self):
        return "Buque de Guerra"


class Lancha(VehiculoMar):

    def __init__(self):
        super().__init__((2, 1), 1, "L")
        self.resistencia = 1

    def mover(self, posicion):
        return posicion

    def menu(self):
        print("""
    [M] Mover
    [V] Volver
        """)

    def __repr__(self):
        return "Lancha"


class Puerto(VehiculoMar):

    def __init__(self):
        super().__init__((4, 2), 80, "P")
        self.resistencia = 80
        self.ataques = [Ingenieros()]

    def mover(self, posicion):
        return None

    def menu_ataques(self):
        return None

    def menu(self):
        print("""
    [R] Reparar vehículo
    [V] Volver
        """)

    def __repr__(self):
        return "Puerto"


class Explorador(VehiculoAire):

    def __init__(self):
        super().__init__((2, 2), "", "E")
        self.paralizado = False
        self.turnos_paralizado = 0
        self.ataques = Explorar()

    def atacado(self, ataque=None):
        self.paralizado = True

    def actualizar_estado(self):
        self.turnos_paralizado += 1
        if self.turnos_paralizado > 5:
            self.turnos_paralizado = 0
            self.paralizado = False

    def mostrarse(self):
        x = randint(0, 1)
        if x == 1:
            print("SOY EL EXPLRORADOR Y ESTOY EN {}".format(self.pos_actual))

    def menu(self):
        if not self.paralizado:
            print("""
    [M] Mover
    [E] Explorar
    [V] Volver
            """)
        else:
            print("""
    Su avión se encuentra paralizado. No puede hacer nada
    [V] Volver
            """)

    def __repr__(self):
        return "Avión Explorador"


class KamikazeAvion(VehiculoAire):

    def __init__(self):
        super().__init__((1, 1), "", "K")
        self.ataques = [Kamikaze()]

    def __repr__(self):
        return "Kamikaze IXXI"


class Caza(VehiculoAire):

    def __init__(self):
        super().__init__((1, 1), "", "C")
        self.ataque = Napalm()

    def __repr__(self):
        return "Avión Caza"

