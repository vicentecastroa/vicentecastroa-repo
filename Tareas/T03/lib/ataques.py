__author__ = 'Vicente'
# coding=UTF-8


class Ataque:

    def __init__(self, damage=None):
        self.cobertura = (1, 1)
        self.damage = damage
        self.disponible = True
        self.usado = False
        self.turnos_espera = 0
        self.espera = 1
        self.coordenada_ataque = None
        pass

    def usar(self):
        self.usado = True
        self.disponible = False

    def actualizar_disponibilidad(self):
        if self.usado:
            self.turnos_espera += 1
            if self.turnos_espera >= self.turnos_espera:
                self.usado = False
                self.disponible = True
                self.turnos_espera = 0

    def celdas_ocupadas(self, posicion):
            celdas = list()
            for i in range(self.cobertura[0]):
                x = posicion[0] + i
                for j in range(self.cobertura[1]):
                    y = posicion[1] + j
                    celdas.append((x, y))
            return celdas


class Trident(Ataque):

    def __init__(self):
        super().__init__(-5)
        self.nombre = "Misil UGM-133 Trident II"


class Tomahawk(Ataque):

    def __init__(self):
        super().__init__(-5)
        self.cobertura = (1, 15)
        self.espera = 3
        self.nombre = "Misil de crucero BGM-109 Tomahawk"

    def __repr__(self):
        return "{}".format(self.nombre)


class Napalm(Ataque):

    def __init__(self):
        super().__init__(-5)
        self.espera = 8
        self.nombre = "Napalm"

    def __repr__(self):
        return "{}".format(self.nombre)


class Minuteman(Ataque):

    def __init__(self):
        super().__init__(-5)
        self.espera = 3
        self.nombre = "Misil Balistico Intercontinental Minuteman III"

    def __repr__(self):
        return "{}".format(self.nombre)


class Kamikaze(Ataque):

    def __init__(self):
        super().__init__(-10000)
        self.nombre = "Kamikaze IXXI"

    def __repr__(self):
        return "{}".format(self.nombre)


class Paralizer(Ataque):

    def __init__(self):
        super().__init__()
        self.nombre = "Massive Ordnance Air Blas Paralizer"

    def __repr__(self):
        return "{}".format(self.nombre)


class Ingenieros(Ataque):

    def __init__(self):
        super().__init__(1)
        self.nombre = "Kit Ingenieros"

    def __repr__(self):
        return "{}".format(self.nombre)
