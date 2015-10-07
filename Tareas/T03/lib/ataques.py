__author__ = 'Vicente'
# coding=UTF-8


class Ataque:

    def __init__(self, nombre, damage=None):
        self.nombre = nombre
        self.size = (1, 1)
        self.damage = damage
        self.disponible = True
        self.usado = False
        self.turnos_espera = 0
        self.espera = 0
        self.coordenada_ataque = None
        pass

    def usar(self):
        self.usado = True
        self.disponible = False

    def actualizar_disponibilidad(self):
        if self.usado:
            self.turnos_espera += 1
            if self.turnos_espera > self.espera:
                self.usado = False
                self.disponible = True
                self.turnos_espera = 0

    def __repr__(self):
        return "{}".format(self.nombre)


class Trident(Ataque):

    def __init__(self):
        super().__init__("Misil UGM-133 Trident II", -5)


class Tomahawk(Ataque):

    def __init__(self):
        super().__init__("Misil de crucero BGM-109 Tomahawk", -5)
        self.size = (1, 15)
        self.espera = 3


class Napalm(Ataque):

    def __init__(self):
        super().__init__("Napalm", -5)
        self.espera = 8

class Minuteman(Ataque):

    def __init__(self):
        super().__init__("Misil Balistico Intercontinental Minuteman III", -15)
        self.espera = 3


class Kamikaze(Ataque):

    def __init__(self):
        super().__init__("Kamikaze IXXI", -10000000)


class Paralizer(Ataque):

    def __init__(self):
        super().__init__("Massive Ordnance Air Blas Paralizer")
        self.size = (2, 1)


class Ingenieros(Ataque):

    def __init__(self):
        super().__init__("Kit Ingenieros", 1)


class Explorar(Ataque):

    def __init__(self):
        super().__init__("Explorar")
        self.size = (3, 3)

    def usar(self):
        pass
