__author__ = 'Vicente'

def gen_id(numero):
    while True:
        yield numero
        numero +=1


def leer_linea(archivo):
    with open(archivo, 'r') as a:
        while True:
            yield a.readline()



linea = leer_linea('Reporte.txt')

print(next(linea))
print(next(linea))
print(next(linea))
print(next(linea))
print(next(linea))
print(next(linea))
