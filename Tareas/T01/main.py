__author__ = 'Vicente'

from lib.interfaz import InterfazBummer as Interfaz
from lib.lecturadatos import LecturaDatos as Datos


if __name__ == "__main__":
    datos = Datos()
    datos.crear_usuario()
    datos.crear_cursos()
    datos.crear_evaluaciones()

    mostrar = Interfaz()

    while True:

        inputs = mostrar.menu_login()  #mensaje bienvenida log in
        usuario = inputs[0]
        clave = inputs[1]



        #input log in

        #menu
        #ejecutar segun requerimiento







        pass
