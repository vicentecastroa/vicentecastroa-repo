__author__ = 'Vicente'
class Carro():
    ''' Un carro de compras lo representaremos como un diccionario
        donde el key es el nombre del producto y el value es la cantidad
        Ej: {'pan' : 3, 'leche' : 2, 'agua' : 6}
    '''
    def __init__(self, lista_productos):
        self.lista_productos = lista_productos

    def __add__(self, otro_carro):
        lista_sumada = self.lista_productos
        for p in otro_carro.lista_productos.keys():
            if p in self.lista_productos.keys():
                lista_sumada.update({ p : otro_carro.lista_productos[p] + self.lista_productos[p]})
            else:
                lista_sumada.update({ p : otro_carro.lista_productos[p]})

        return Carro(lista_sumada)

    def __repr__(self):
        return "\n".join("Producto: {} | Cantidad: {}".format(p, self.lista_productos[p]) for p in self.lista_productos.keys())


carro_1 = Carro({'pan' : 3, 'leche' : 2, 'agua' : 6, 'cerveza':20})
carro_2 = Carro({'leche' : 5, 'bebida' : 2, 'cerveza' : 12})
carro_3 = carro_1 + carro_2
print(carro_3.lista_productos)
print(carro_3.__repr__())