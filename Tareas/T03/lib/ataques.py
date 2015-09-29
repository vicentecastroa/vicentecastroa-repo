__author__ = 'Vicente'


class Ataque:

    def __init__(self):
        self.daño = None
        self.cobertura = None


class Trident(Ataque):

    def __init__(self):
        super().__init__()
        self.nombre = "Misil UGM-133 Trident II"


class Tomahawk(Ataque):

    def __init__(self):
        super().__init__()
        self.nombre = "Misil de crucero BGM-109 Tomahawk"


class Napalm(Ataque):

    def __init__(self):
        super().__init__()
        self.nombre = "Napalm"


class Minuteman(Ataque):

    def __init__(self):
        super().__init__()
        self.nombre = "Misil Balistico Intercontinental Minuteman III"


class Kamikaze(Ataque):

    def __init__(self):
        super().__init__()
        self.nombre = "Kamikaze IXXI"
