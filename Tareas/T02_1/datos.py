__author__ = 'Vicente'


class Nodo:

    def __init__(self, valor):
        self.valor = valor
        self.anterior = None
        self.siguiente = None

    def __repr__(self):
        return self.valor


class Lista:

    def __init__(self):
        self.primero = None
        self.ultimo = None

    def add_nodo(self, nodo):
        if len(self) == 0:
            self.primero = nodo
            self.ultimo = nodo
        else:
            nodo.anterior = self.ultimo
            self.ultimo.siguiente = nodo
            self.ultimo = nodo

    def get_nodo(self, id):
        for nodo in self:
            if nodo.valor.id == id:
                return nodo
        raise ValueError

    def __contains__(self, id):
        if len(self) == 0:
            return False
        for nodo in self:
            if nodo.valor.id == id:
                return True
        return False

    def __len__(self):
        contador = 0
        for nodo in self:
            contador += 1
        return contador

    def __getitem__(self, numero):
        if numero > len(self) - 1:
            raise IndexError
        actual = self.primero
        for i in range(numero):
            actual = actual.siguiente
        return actual.valor

    def __repr__(self):
        retorno = "["
        for nodo in self:
            retorno += repr(nodo)
            retorno += ", "
        retorno += "]"
        return retorno

    def __iter__(self):
        actual = self.primero
        while actual:
            yield actual
            actual = actual.siguiente

        return False