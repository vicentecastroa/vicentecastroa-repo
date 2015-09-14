__author__ = 'Vicente'


class Lista:
    def __init__(self):
        self.primero = None
        self.largo = 0

    def add(self, nodo):
        if not self.primero:
            self.primero = nodo
        else:
            actual = self.get_ultimo()
            actual.siguiente = nodo
            nodo.anterior = actual
        self.largo += 1

    def remove(self, nodo):
        if not self.primero:
            return "la lista esta vacia"
        if self.largo == 1:
            self.primero = None
        else:
            actual = self.primero
            while True:
                if actual == nodo:
                    if not actual.anterior:  # si se quiere eliminar el primero
                        self.primero = actual.siguiente
                        self.largo -= 1
                        break
                    b = actual.siguiente  # al anterior, se le asigna el siguiente
                    anterior = actual.anterior
                    anterior.siguiente = b
                    self.largo -= 1
                    break
                else:
                    actual = actual.siguiente

    def get(self, posicion):
        actual = self.primero
        for i in range(posicion):
            actual = actual.siguiente
        if not actual:
            return "La lista no tiene la posicion pedida"
        else:
            return actual

    def get_ultimo(self):
        if self.largo >= 1:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            return actual
        return None

    def __repr__(self):
        return "Lista/ Primero {}".format(self.primero)


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

    def __repr__(self):
        return "Nodo: {}".format(self.valor)

