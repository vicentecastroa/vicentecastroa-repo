__author__ = 'Vicente'

import sistema

if __name__ == "__main__":


    a = sistema.preguntar_puerto_actual()
    print(str(sistema.puerto_final()))
    print(str(a))
    print(str(sistema.posibles_conexiones()))
    sistema.hacer_conexion(1)
    print(str(sistema.preguntar_puerto_actual()))
    sistema.hacer_conexion(1)
    print(str(sistema.preguntar_puerto_actual()))
    sistema.hacer_conexion(1)
    print(str(sistema.preguntar_puerto_actual()))
    sistema.hacer_conexion(1)
    print(str(sistema.preguntar_puerto_actual()))