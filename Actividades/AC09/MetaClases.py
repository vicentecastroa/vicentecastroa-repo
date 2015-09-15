__author__ = 'Vicente'

class MetaRobot(type):
    def __new__(meta, nombre, base_clases, diccionario):
        diccionario.update(dict({"creador": "vicentecastroa",
                                 "ip_inicio": "190.102.62.283",
                                 "check_creator": meta.check_creator,
                                 "cortar_conexion": meta.cortar_conexion,
                                 "cambiar_nodo": meta.cambiar_nodo
                                 }))
        return super().__new__(meta, nombre, base_clases, diccionario)

    def check_creator(self):
        if self.creador in self.creadores:
            return print("El creador esta en la lista de programadores permitidos")
        return print("Alerta: el creador no esta en la lista de programadores")

    def cortar_conexion(self):
        if self.Verificar():
            print("El hacker esta en el mismo puerto. Se cortara la conexion")
            self.actual.hacker = 0

    def cambiar_nodo(self, nuevo_puerto):
        actual = self.actual
        print("cambiando nodo desde {} a {}".format(actual, nuevo_puerto))
        self.actual = nuevo_puerto
