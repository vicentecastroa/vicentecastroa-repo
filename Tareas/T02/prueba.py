__author__ = 'Vicente'


class Hola:
    def saludar(self):
        print("hola como estas")

a = Hola()
def saludo_nuevo():
    print("el pasto es pa las vacas")
a.saludar()
a.saludar = saludo_nuevo
a.saludar()
