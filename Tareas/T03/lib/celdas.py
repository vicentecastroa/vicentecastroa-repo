__author__ = 'Vicente'
import string
letras = string.ascii_uppercase


def coord_to_index(coordenada_ingresada):
    coordenada = coordenada_ingresada.upper()
    str_to_int = int(letras.index(coordenada[0]))
    y = str_to_int
    x = int(coordenada[1:]) - 1
    if check_index((x, y)):
        return (x, y)


def index_to_coord(posicion_tupla):
    x = letras[posicion_tupla[1]]
    y = posicion_tupla[0] + 1
    return "{}{}".format(x, y)


def check_index(coordenada):
    for value in coordenada:
        if int(value) >= 15:
            print("Coordenada incorrecta")
            return False
    return True

"""
print(coord_to_index("A3"))
print(coord_to_index("o15"))
print(coord_to_index("x1"))
print(coord_to_index("A16"))
print(coord_to_index("p16"))


print(index_to_coord((0, 0)))
print(index_to_coord((5, 1)))
print(index_to_coord((7, 9)))
"""