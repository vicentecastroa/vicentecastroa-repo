__author__ = 'Vicente'

def gen_id(numero):
    while True:
        yield numero
        numero +=1


def leer_linea(archivo):
    with open(archivo, 'r'):
        yield linea in archivo

linea = leer_linea('../AC06/Reporte.txt')

print(next(linea))
