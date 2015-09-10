__author__ = 'Vicente'
class MiMetaClase(type):
    def __new__(meta, nombre, base_clases, diccionario):
        print ('-----------------------------------')
        print("Creando la clase.. {} ".format(nombre))
        print(meta)
        print(base_clases)
        diccionario.update(dict({'atributo_obligatorio': 10}))
        print(diccionario)
        return super().__new__(meta, nombre, base_clases, diccionario)

    def __call__(cls, *args, **kwargs):
        print("__call__ of  {}".format(str(cls)))
        print("__call__ *args= {}".format(str(args)))
        return super().__call__(*args, **kwargs)

class MiClase(metaclass = MiMetaClase):
    def __init__(self, a, b):
        print("Objeto de MiClase con a=%s, b=%s" % (a, b))

    def func(self, params):
        pass

    mi_parametro = 4

print('creare un objeto ahora...')
ob1 = MiClase(1, 2)