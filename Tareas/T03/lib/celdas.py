__author__ = 'Vicente'
# coding=UTF-8
import string
letras = string.ascii_uppercase


def coord_to_index(coordenada_ingresada):
    try:
        coordenada = coordenada_ingresada.upper()
        str_to_int = int(letras.index(coordenada[0]))
        y = str_to_int
        x = int(coordenada[1:]) - 1
        if check_index((x, y)):
            return (x, y)
    except ValueError as err:
        print("Error {} | Ingrese coordenadas en el orden LetraNumero".format(err))
        return False


def index_to_coord(posicion_tupla):
    try:
        if check_index(posicion_tupla):
            x = letras[posicion_tupla[1]]
            y = posicion_tupla[0] + 1
            return "{}{}".format(x, y)
    except ValueError:
        print("Esta malo. Hay un no numero metido por ahí. Quedó la grande.")
    return False


def check_index(coordenada):
    for value in coordenada:
        if int(value) >= 15:
            print("Coordenada incorrecta")
            return False
    return True


def celdas_ocupadas(posicion, size):
    celdas = list()
    for i in range(size[0]):
        x = posicion[0] + i
        for j in range(size[1]):
            y = posicion[1] + j
            celdas.append((x, y))
    return celdas