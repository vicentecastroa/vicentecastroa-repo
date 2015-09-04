__author__ = 'Vicente'


class Persona:
    def __init__(self, nombre: "", usuario: "", clave: ""):
        self.nombre = nombre
        self.usuario = usuario
        self.clave = clave

    def __repr__(self):
        return "{} objeto".format(self.usuario)


class Profesor(Persona):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return "Profesor {}".format(self.nombre)


class Alumno(Persona):
    def __init__(self, ramos_pre: "", idolos: "", **kwargs):
        super().__init__(**kwargs)
        self.ramos_pre = ramos_pre
        self.idolos = idolos
        self.carga_academica = {}
        self.creditos_tomados = 0
        self.bacanosidad = 0
        self.grupo_bummer = 0
        self.max_creditos = 55 + (6 - self.grupo_bummer) * 2

    def __repr__(self):
        return "Alumno {}".format(self.nombre)
