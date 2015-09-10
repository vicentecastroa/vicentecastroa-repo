__author__ = 'Vicente'

class MetaRobot(type):
    def __new__(meta, nombre, base_clases, diccionario):
        diccionario.update(dict({"creador": "vicentecastroa",
                                 "ip_inicio": "190.102.62.283",
                                 "check_creator": meta.check_creator,
                                 "cambiar_conexion": meta.cambiar_conexion,
                                 "cambiar_nodo": meta.cambiar_nodo
                                 }))
        return super().__new__(meta, nombre, base_clases, diccionario)

    def check_creator(self):
        if self.creador in self.creadores:
            return print("El creador está en la lista de programadores permitidos")
        return print("Alerta: el creador no está en la lista de programadores")

    def cambiar_conexion(self):
        if self.verificar():
            print("El hacker está en el mismo puerto. Se cortara la conexion")
            self.actual.hacker = 0

    def cambiar_nodo(self, nuevo_puerto):
        actual = self.actual
        print("cambiando nodo desde {} a {}".format(actual, nuevo_puerto))
        self.actual = nuevo_puerto
