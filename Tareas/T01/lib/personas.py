__author__ = 'Vicente'

class Persona:

    def __init__(self, nombre:"", usuario:"", clave:""):
        self.nombre = nombre
        self.usuario = usuario
        self.clave = clave

    def log_in(self, user, password):
        if self.usuario == user and self.clave == password:
            return True
        return False

    def log_out(self):
        pass

    def __repr__(self):
        return "{} objeto".format(self.usuario)


class Profesor(Persona):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ramos = []

class Alumno(Persona):
    def __init__(self, ramos_pre:"", idolos:"", **kwargs):
        super().__init__(**kwargs)
        self.ramos_pre = ramos_pre
        self.idolos = idolos
        self.carga_academica = {}
        self.creditos_tomados = 0
        self.bacanosidad = None
        self.grupo_bummer = None
        self.max_creditos = None
