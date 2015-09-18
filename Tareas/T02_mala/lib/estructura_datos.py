__author__ = 'Vicente'


class Lista:
    def __init__(self):
        self.primero = None
        self.ultimo_agregado = None
        self.largo = 0

    def add(self, nodo):
        # si padres o hijos estan vacios, lo dejo como primero.
        # si no, lo agrego  en siguiente. "hermano"
        if not self.primero:
            self.primero = nodo
            self.ultimo_agregado = self.primero
        else:
            actual = self.ultimo_agregado
            actual.siguiente = nodo
            nodo.anterior = actual
            self.ultimo_agregado = nodo
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

    def get_by_id(self, id):
        for nodo in self:
            if nodo.id == id:
                return nodo
        return "No existe ese id"

    def buscar_nodo(self, id):  # si es verdad, entregar nodo.
        if self.primero:
            actual = self.primero
            if actual.id == id:
                return actual
            else:
                for hijo in actual.hijos:
                    if hijo.id == id:
                        return hijo
                    nodo = hijo.hijos.buscar_nodo(id)
                    if nodo:
                        return nodo
            return False

    def __contains__(self, id):  # if id in lista
        for nodo in self:
            if nodo.id == id:
                return True
        return False

    def __iter__(self):
        if self.primero:
            actual = self.primero
            i = 0
            while i < self.largo:
                yield actual
                if actual.siguiente:
                    actual = actual.siguiente
                i += 1
        else:
            return False

    def __repr__(self):
        retorno = ""
        for nodo in self:
            retorno = retorno + repr(nodo) + "\n"
        return retorno


class Nodo:
    def __init__(self):
        self.siguiente = None
        self.anterior = None

'''
a = Nodo(5)
b = Nodo(6)
c = Nodo(7)
d = Nodo(8)
e = Nodo(9)

lista = Lista()
lista.add(a)
lista.add(b)
lista.add(c)
lista.add(d)
lista.add(e)

for i in lista:
    print(i)'''