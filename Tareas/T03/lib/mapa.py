__author__ = 'Vicente'
 # coding=UTF-8

import string
from vehiculos import Vehiculo


class Mapa:

    def __init__(self, nombre=None):
        self.nombre = nombre.upper()
        self.dimension = 15
        self.n_mapa = 0
        self.historial = {0: list()}
        self.grilla_actual = self.grilla_default()
        self.vehiculos_actual = list()

    def grilla_default(self):
        grilla = [["_" for _ in range(self.dimension)] for _ in range(self.dimension)]
        return grilla

    def posicionar_random(self):
        return True

    def cerrar_mapa(self):
        self.n_mapa += 1
        self.historial[self.n_mapa] = self.vehiculos_actual

    def mostrar_mapa(self, turno):
        numeros = list(map(lambda x: str(x+1), range(self.dimension)))
        grilla = self.grilla_default()
        for elemento in self.historial[turno]:
            alto = elemento.size[0]
            ancho = elemento.size[1]
            try:
                cord_x = elemento.pos_actual[0]
                cord_y = elemento.pos_actual[1]
                for i in range(alto):
                        grilla[cord_y+i][cord_x] = "X"
                        for j in range(ancho):
                            grilla[cord_y+i][cord_x+j] = "X"
            except TypeError:
                pass
        self.grilla_actual = grilla
        self.encabezado()
        for i in range(len(grilla)):
            numero = numeros[i]
            if int(numero) < 10:
                numero = "0{}".format(numeros[i])
            print("{}".format(numero), grilla[i])

    def encabezado(self):
        letras = list(map(lambda x: x, string.ascii_uppercase))
        letras.insert(0, "__")
        print("________________MAPA {}_________________ \n".format(self.nombre))

        for i in range(self.dimension+1):
            if not i == self.dimension:
                print(letras[i], end="    ")
            else:
                print(letras[i])

    def ubicar_elemento(self, elemento, posicion):
        try:
            if self.check_espacio(elemento.size, posicion):
                elemento.pos_actual = posicion
                try:
                    lista_vehiculos = [elemento for elemento in self.vehiculos_actual]
                except TypeError:
                    lista_vehiculos = list()
                lista_vehiculos.append(elemento)
                self.vehiculos_actual = lista_vehiculos
                return True
        except IndexError:
            print("ERROR: Esta ubicando {} fuera del mapa".format(elemento))

    def borrar_elemento(self, elemento):
        if elemento in self.vehiculos_actual:
            lista_vehiculos = [elemento for elemento in self.vehiculos_actual]
            lista_vehiculos.remove(elemento)
            self.vehiculos_actual = lista_vehiculos
            return True

    def mover_elemento(self):
        print("Seleccione un vehículo")
        for i in range(len(self.vehiculos_actual)):
            print("[{}] {}".format(i+1, self.vehiculos_actual[i]))
        vehiculo = self.vehiculos_actual[input()-1]
        print("Ha seleccionado {}".format(vehiculo))
        direccion = input("""
        Mover en dirección:
        Q   W   E
        A   -   D
        Z   X   C
        """).upper()
        self.ubicar_elemento(vehiculo, vehiculo.mover(direccion))

    def check_espacio(self, dimension, posicion):
        alto = dimension[0]
        ancho = dimension[1]
        cord_x = posicion[0]
        cord_y = posicion[1]
        grilla = self.grilla_actual
        for i in range(alto):
            if grilla[cord_y+i][cord_x] == "X":
                return False
            for j in range(ancho):
                if grilla[cord_y+i][cord_x+j] == "X":
                    return False
        return True

    def __repr__(self):
        return "MAPA"


class MapaAire(Mapa):

    def __init__(self):
        super().__init__()


class MapaMar(Mapa):

    def __init__(self):
        super().__init__()


"""
if __name__ == '__main__':
    bote = Vehiculo()
    bote2 = Vehiculo()
    mapa = Mapa("jugador 1")
    mapa.ubicar_elemento(bote, (3, 3))
    mapa.cerrar_mapa()
    mapa.mostrar_mapa(1)
    print(mapa.vehiculos_actual)
    mapa.ubicar_elemento(bote2, (10, 10))
    mapa.cerrar_mapa()
    mapa.mostrar_mapa(2)
    print(mapa.vehiculos_actual)
    mapa.borrar_elemento(bote2)
    mapa.cerrar_mapa()
    mapa.mostrar_mapa(3)
    print(mapa.vehiculos_actual)
"""