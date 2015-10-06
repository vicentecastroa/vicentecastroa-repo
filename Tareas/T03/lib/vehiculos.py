__author__ = 'Vicente'
# coding=UTF-8

from ataques import Trident, Tomahawk, Napalm, Minuteman, Kamikaze, Paralizer, Ingenieros


class Vehiculo:

    def __init__(self, size, resistencia, id):
        self.size = size
        self.id = id
        self.pos_actual = None
        self.resistencia = resistencia
        self.ataque = None
        self.vivo = True

    def celdas_ocupadas(self, posicion):
        celdas = list()
        for i in range(self.size[0]):
            x = posicion[0] + i
            for j in range(self.size[1]):
                y = posicion[1] + j
                celdas.append((x, y))
        return celdas

    def mover(self, direccion):
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

    def cambiar_resistencia(self, cambio):
        self.resistencia += cambio
        if self.resistencia <= 0:
            print("""
    {} ha sido destruido.
    Estaba ocupando las celdas {}
            """.format(self, self.celdas_ocupadas(self.pos_actual)))
            return False  # mató
        return True  # sigue vivo

    def atacar(self):
        # pedir posicion ataque
        return None


class VehiculoMar(Vehiculo):

    def __init__(self, *args):
        super().__init__(*args)


class VehiculoAire(Vehiculo):

    def __init__(self, *args):
        super().__init__(*args)


class BarcoPequeno(VehiculoMar):

    def __init__(self):
        super().__init__((3, 1), 30, "B")
        self.ataque = Minuteman()

    def __repr__(self):
        return "Barco Pequeño"


class BuqueGuerra(VehiculoMar):

    def __init__(self):
        super().__init__((2, 3), 60, "G")
        self.ataque = Tomahawk()

    def __repr__(self):
        return "Buque de Guerra"


class Lancha(VehiculoMar):

    def __init__(self):
        super().__init__((2, 1), 1, "L")
        self.resistencia = 1

    def mover(self, posicion):
        return posicion

    def __repr__(self):
        return "Lancha"


class Puerto(VehiculoMar):

    def __init__(self):
        super().__init__((4, 2), 80, "P")
        self.resistencia = 80
        self.ataque = Ingenieros()

    def mover(self, posicion):
        return None

    def __repr__(self):
        return "Puerto"


class Explorador(VehiculoAire):

    def __init__(self):
        super().__init__((2, 2), "", "E")

    def __repr__(self):
        return "Avión Explorador"


class KamikazeAvion(VehiculoAire):

    def __init__(self):
        super().__init__((1, 1), "", "K")
        self.ataque = Kamikaze()

    def __repr__(self):
        return "Kamikaze IXXI"


class Caza(VehiculoAire):

    def __init__(self):
        super().__init__((1, 1), "", "C")
        self.ataque = Napalm()

    def __repr__(self):
        return "Avión Caza"

