__author__ = 'Vicente'

class InterfazBummer():
    def __init__(self):
        pass

    def menu_login(self):
        print('BIENVENIDO A BUMMER UC, POR FAVOR INGRESE SUS DATOS')
        usuario = input('Usuario:    ')
        clave = input('Clave:   ')
        return (usuario,clave)


    def menu_inicio(self):
        print("""
        BUMMER UC
        1: Inscribir Ramo
        2: Botar Ramo
        3: Generar Horario
        4: Generar Calendario Evaluaciones
        """)
        opcion = input('Elija una opcion:    ')
        return opcion

    def inscripcion_ramos(self):
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
        return preferencias

    def botar_ramo(self):
        print("""
        ___________RETIRO DE RAMOS___________

        Ingrese NRC del ramo que desee retirar
        """)
        preferencia = input('NRC:    ')
        return preferencia

    def generar_horario(self):
        pass

I = InterfazBummer()
datos = I.menu_login()
print(datos[0])
print(datos[1])