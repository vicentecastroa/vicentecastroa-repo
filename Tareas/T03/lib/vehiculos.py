__author__ = 'Vicente'
 # coding=UTF-8

from ataques import Trident, Tomahawk, Napalm, Minuteman, Kamikaze, Paralizer, Ingenieros


class Vehiculo:

    def __init__(self):
        self.size = (3, 3)
        self.pos_actual = None
        self.resistencia = None
        self.ataque = None

    def mover(self, direccion):
        direcciones = {"A": (-1, 0),
                       "D": (1, 0),
                       "W": (0, 1),
                       "X": (0, -1),
                       "Q": (-1, 1),
                       "E": (1, 1),
                       "Z": (-1, -1),
                       "C": (1, -1),
                       }
        cambio = direcciones[direccion]
        posicion_nueva = (self.pos_actual[0]+cambio[0], self.pos_actual[1]+cambio[1])
        return posicion_nueva

    def cambiar_resistencia(self, cambio):
        self.resistencia += cambio
        return True

    def atacar(self, posicion):

        return None

    def __repr__(self):
        return "Bote"


class VehiculoMar(Vehiculo):

    def __init__(self):
        super().__init__()


class VehiculoAire(Vehiculo):

    def __init__(self):
        super().__init__()


class BarcoPequeno(VehiculoMar):

    def __init__(self):
        super().__init__()
        self.size = (3, 1)
        self.resistencia = 30
        self.ataque = Minuteman()

    def __repr__(self):
        return "Barco Pequeño"


class BuqueGuerra(VehiculoMar):

    def __init__(self):
        super().__init__()
        self.resistencia = 60
        self.ataque = Tomahawk()

    def __repr__(self):
        return "Buque de Guerra"


class Lancha(VehiculoMar):

    def __init__(self):
        super().__init__()
        self.resistencia = 1

    def mover(self, posicion):
        return None

    def __repr__(self):
        return "Lancha"


class Puerto(VehiculoMar):

    def __init__(self):
        super().__init__()
        self.resistencia = 80
        self.ataque = Ingenieros()

    def mover(self, posicion):
        return None

    def __repr__(self):
        return "Puerto"


class Explorador(VehiculoAire):

    def __init__(self):
        super().__init__()

    def __repr__(self):
        return "Avión Explorador"


class KamikazeAvion(VehiculoAire):

    def __init__(self):
        super().__init__()
        self.ataque = Kamikaze()

    def __repr__(self):
        return "Kamikaze IXXI"


class Caza(VehiculoAire):

    def __init__(self):
        super().__init__()
        self.ataque = Napalm()

    def __repr__(self):
        return "Avión Caza"

