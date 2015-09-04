__author__ = 'Vicente'

from lib.interfaz import InterfazBummer as Interfaz
from lib.lecturadatos import LecturaDatos as Datos
from lib.personas import Alumno as Alum, Profesor as Prof


def alumno_ejecutar_opcion(usuario, opcion, datos, hora):
    funciones = {"1": mostrar.inscribir_cursos,
                 "2": mostrar.eliminar_curso,
                 "3": mostrar.ver_horario,
                 "4": mostrar.descargar_evaluaciones,
                 }

    if opcion in funciones:
        return funciones[opcion](usuario, datos, hora)
    elif opcion != "s":
        return print("Elija una opcion valida")


def profesor_ejecutar_opcion(usuario, opcion, datos, hora):
    funciones = {"1": mostrar.prof_inscribir_cursos,
                 "2": mostrar.prof_eliminar_curso,
                 }

    if opcion in funciones:
        return funciones[opcion](usuario, datos, hora)
    elif opcion != "s":
        return print("Elija una opcion valida")


if __name__ == "__main__":
    print("Iniciando plataforma...")
    datos = Datos()
    datos.crear_usuario()
    datos.crear_cursos()
    datos.obtener_horario()
    datos.crear_evaluaciones()
    datos.calcular_bacanosidad()
    datos.ordenar_bacanosidad()
    datos.obtener_grupo()
    datos.agregar_requisitos()

    mostrar = Interfaz()
    hora = input("Para empezar, ingrese una hora virtual (h:mm)")

    while True:
        inputs = mostrar.menu_login()  # mensaje bienvenida log in
        usuario = log_in(inputs[0], inputs[1])
        if usuario == "error":
            print("Usuario y clave no coinciden")

        opcion = ""
        if isinstance(usuario, Alum):
            while opcion != "s":
                opcion = mostrar.menu_alumno()
                alumno_ejecutar_opcion(usuario, opcion, datos, hora)

        if isinstance(usuario, Prof):
            while opcion != "s":
                opcion = mostrar.menu_profesor()
                profesor_ejecutar_opcion(usuario, opcion, datos, hora)
