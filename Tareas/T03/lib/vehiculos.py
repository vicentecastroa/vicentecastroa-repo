__author__ = 'Vicente'


class Vehiculo:

    def __init__(self):
        self.tama�o = None
        self.resistencia = None
        self.ataques = dict()

    def mover(self, direccion):
        return None

    def cambiar_resistencia(self, cambio):
        return None

    def atacar(self, ataque, posicion):
        return None


class VehiculoMar(Vehiculo):

    def __init__(self):
        super().__init__()


class VehiculoAire(Vehiculo):

    def __init__(self):
        super().__init__()


class BarcoPeque�o(VehiculoMar):

    def __init__(self):
        super().__init__()


class BuqueGuerra(VehiculoMar):

    def __init__(self):
        super().__init__()


class Lancha(VehiculoMar):

    def __init__(self):
        super().__init__()

    def mover(self, posicion):
        return None


class Puerto(VehiculoMar):

    def __init__(self):
        super().__init__()


class Explorador(VehiculoAire):

    def __init__(self):
        super().__init__()


class Kamikaze(VehiculoAire):

    def __init__(self):
        super().__init__()


class Caza(VehiculoAire):

    def __init__(self):
        super().__init__()

