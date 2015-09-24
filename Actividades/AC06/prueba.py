__author__ = 'Vicente'


def gen_id():
    actual = 0
    while True:
        yield actual
        actual += 1


class Paciente:
    def __init__(self, atributos):
        self.id = next(gen_id())
        self.atributos = atributos
        self.variables = ["ano", "mes", "dia", "color", "hora", "motivo"]
        self.atributos_dict = self.set_atributos()

    def set_atributos(self):
        atributos = dict()
        atributos["id"] = str(self.id)
        for i in range(len(self.variables)):
            atributos[self.variables[i]] = self.atributos[i]
        return atributos

    def __repr__(self):
        return "\t".join(self.atributos_dict.values())


class Reporte:
    def __init__(self):
        self.pacientes = {"amarillo": [],
                          "azul": [],
                          "naranja": [],
                          "rojo": [],
                          "verde": [],
                          }

    def leer_linea(self):
        with open("Reporte.txt", "r") as f:
            while True:
                yield f.readline().split("\t")

    def leer_reporte(self):
        while self.check():
            paciente = Paciente(next(self.leer_linea()))
            lista_color = self.pacientes[paciente.atributos_dict["color"]]
            if len(lista_color) < 10 and paciente.atributos_dict["ano"] == "2013":
                lista_color.append(paciente)

    def check(self):
        for lista_color in self.pacientes.values():
            if len(lista_color) == 10:
                return False
        return True

    def print_color(self, color):
        return print(self.pacientes[color])

    def __repr__(self):
        lista_pacientes = []
        for lista in self.pacientes.values():
            for paciente in lista:
                lista_pacientes.append(paciente)

        return lista_pacientes

reporte = Reporte()
reporte.leer_reporte()
reporte.print_color("amarillo")