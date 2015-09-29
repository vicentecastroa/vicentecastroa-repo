__author__ = 'Vicente'

import numpy as np
import string


class Mapa:

    def __init__(self):
        self.dimension = 15
        self.lista_vehiculos = dict()
        self.historial = dict()
        self.n_mapa = 0
        self.grilla_actual = self.grilla_default()

    def grilla_default(self):
        grilla = [["_" for x in range(self.dimension)] for i in range(self.dimension)]
        self.historial["{}".format(self.n_mapa)] = grilla

        return grilla

    def mostrar_mapa(self, turno):
        letras = list(map(lambda x: x, string.ascii_uppercase))
        letras.insert(0, "__")
        numeros = list(map(lambda x: str(x+1), range(self.dimension)))
        print("________________MAPA_________________ \n")

        for i in range(self.dimension+1):
            if not i == self.dimension:
                print(letras[i], end="    ")
            else:
                print(letras[i])
        for i in range(len(self.grilla_actual)):
            fila = self.historial["{}".format(turno)][i]
            numero = numeros[i]
            if int(numero) < 10:
                numero = "0{}".format(numeros[i])
            print("{}".format(numero), fila)

    def ubicar_elemento(self, elemento, posicion):  # posicion:tupla
        # alto = elemento.tamano[0]
        # ancho = elemento.tamano[1]
        alto = elemento[0]
        ancho = elemento[1]
        cord_x = posicion[0]
        cord_y = posicion[1]
        try:
            for i in range(alto):
                self.grilla_actual[cord_y+i][cord_x] = "X"
                for j in range(ancho):
                    self.grilla_actual[cord_y+i][cord_x+j] = "X"

            self.n_mapa += 1
            self.historial["{}".format(self.n_mapa)] = self.grilla_actual
        except IndexError:
            print("El vehiculo tiene partes fuera del mapa")
            self.mostrar_mapa(0)

    def __repr__(self):
        return "MAPA"

class MapaAire(Mapa):

    def __init__(self):
        super().__init__()


class MapaMar(Mapa):

    def __init__(self):
        super().__init__()




mapa = Mapa()
mapa.mostrar_mapa(0)
mapa.ubicar_elemento((3, 2), (13, 13))

