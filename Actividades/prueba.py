__author__ = 'Vicente'


def saludar_con_amor(accion, intensidad):
    def agregar_amor(f):
        print('agregamos amor')

        def nuevo_saludo(*args):
            print("voy a saludar con amor")
            f(*args)
            print("{} {}".format(accion, intensidad))
            print("")
            return nuevo_saludo

    print("test")
    return agregar_amor


@saludar_con_amor("te quiero", "mucho")
def saludar(objeto, sujeto):
    print("hola {}, soy {}").format(objeto, sujeto)

saludar('perro', 'vicente')
