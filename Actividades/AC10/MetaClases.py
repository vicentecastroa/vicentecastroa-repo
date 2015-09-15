__author__ = 'Vicente'


class RestrictedAccess(type):
    def __new__(cls, nombre, base_clases, diccionario):

        for atributo in diccionario["attributes"]:
            setattr(cls, "__{}".format(atributo), None)

        diccionario.update(dict({"__init__": cls.nuevoinit
                                 }))

        return super().__new__(cls, nombre, base_clases, diccionario)

    def nuevoinit(self, *args):
        pass

    def name(self):
        return self.__name

    def lastname(self):
        return self.__lastname

    def alias(self):
        return self.__alias

