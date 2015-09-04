__author__ = 'Vicente'
from lib.funciones_banner import (inscribir_cursos as inscribir,
                                  eliminar_curso as botar,
                                  ver_horario as horario,
                                  descargar_evaluaciones as evaluaciones,
                                  revisar_hora,
                                  revisar_profesor
                                  )
from lib.personas import Alumno as Alum


class InterfazBummer():
    def __init__(self):
        pass

    def menu_login(self):
        print('BIENVENIDO A BUMMER UC, POR FAVOR INGRESE SUS DATOS')
        usuario = input('Usuario:    ')
        clave = input('Clave:   ')
        return (usuario, clave)


    def menu_alumno(self):
        print(""" BUMMER UC
            1. Inscribir curso
            2. Eliminar curso
            3. Ver horario
            4. Descargar calendario de evaluaciones

            s. Salir

            Opcion:  """)

        user_entry = input()
        return user_entry

    def inscribir_cursos(self, usuario, datos, hora):

        if not revisar_hora(usuario, hora):
            return print("ERROR: Este horario no le corresponde para inscribir cursos")
        print("""
        _____INSRCIPCION RAMOS_____

        Puede ingresar hasta 6 ramos
        """)
        preferencias = []
        for i in range(6):
            preferencia = input('Ingrese [NRC del ramo]/[ok]:    ')
            if preferencia == 'ok':
                break
            preferencias.append(preferencia)

        inscribir(usuario, preferencias, datos)

    def eliminar_curso(self, usuario, datos, hora):
        if not revisar_hora(usuario, hora):
            return print("ERROR: Este horario no le corresponde para inscribir cursos")

        print("""
        ___________RETIRO DE RAMOS___________

        Ingrese NRC del ramo que desee retirar
        """)
        preferencia = input('NRC:    ')

        botar(usuario, preferencia, datos)

    def menu_profesor(self):
        print(""" BUMMER UC
            1. Agregar alumno a curso
            2. Eliminar alumno de curso

            s. Salir

            Opcion:  """)

        user_entry = input()
        return user_entry

    def prof_inscribir_cursos(self, usuario, datos, hora):


        print("""
        _______INGRESO EXCEPCIONAL ________

        """)
        alumno = datos.alumnos.get([input("Ingrese usuario de alumno:   ")], "El usuario no existe")
        nrc = [input("Ingrese NRC del curso:    ")]
        if not isinstance(alumno, Alum):
            return print(alumno)

        if not revisar_hora(alumno, hora):
            return print("ERROR: Este horario no le corresponde al usuario para inscribir cursos")

        if not revisar_profesor(usuario, nrc, datos):
            return print("ERROR: Usted no tiene acceso a este curso")

        inscribir(alumno, nrc, datos, excepcion=True)

    def prof_eliminar_curso(self, usuario, datos, hora):

        print("""
        _______ELIMINAR ALUMNO________

        """)
        alumno = datos.alumnos.get([input("Ingrese usuario de alumno:   ")], "El usuario no existe")
        nrc = [input("Ingrese NRC del curso:    ")]
        if not isinstance(alumno, Alum):
            return print(alumno)

        if not revisar_hora(alumno, hora):
            return print("ERROR: Este horario no le corresponde al usuario para inscribir cursos")

        botar(alumno, nrc, datos)

    def ver_horario(self, usuario):
        clases = horario(usuario)
        if len(clases) == 0:
            print("No tiene cursos para mostrar")

        print("""
        _______HORARIO 2016-1___________
        """)
        horario_mostrar = [['  L ', ' M  ', ' W  ', ' J  ', ' V  ', ' S  '],
                           ['   ', '    ', '    ', '    ', '    ', '    '],
                           ['   ', '    ', '    ', '    ', '    ', '    '],
                           ['   ', '    ', '    ', '    ', '    ', '    '],
                           ['   ', '    ', '    ', '    ', '    ', '    '],
                           ['   ', '    ', '    ', '    ', '    ', '    '],
                           ['   ', '    ', '    ', '    ', '    ', '    '],
                           ['   ', '    ', '    ', '    ', '    ', '    '],
                           ['   ', '    ', '    ', '    ', '    ', '    ']]

        for clase in clases:
            a = clase.split("-")
            dia_hora = a[0].split(":")
            dia = dia_hora[0]
            if dia == "L":
                dia_index = 0
            if dia == "M":
                dia_index = 1
            if dia == "W":
                dia_index = 2
            if dia == "J":
                dia_index = 3
            if dia == "V":
                dia_index = 4
            if dia == "S":
                dia_index = 5

            hora = dia_hora[1]
            output = a[1] + "|"
            horario_mostrar[int(hora)][dia_index] = output

        print('\n'.join([' '.join(["{:10}  |".format(clase) for clase in modulo])
                         for modulo in horario_mostrar]))

        with open("./horario.txt", "w", encoding="utf8") as f:
            f.write('\n'.join([' '.join(["{:10}  |".format(clase) for clase in modulo])
                               for modulo in horario_mostrar]))

    def descargar_evaluaciones(self, usuario):
        lista_evaluaciones = evaluaciones(usuario)

        with open("./evaluaciones", "w", encoding="utf8") as f:
            for ev in lista_evaluaciones:
                f.write("{}".format(ev))
