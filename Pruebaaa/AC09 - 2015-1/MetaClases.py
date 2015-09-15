__author__ = 'Vicente'


class MetaEmpresa(type):

    def __new__(cls, nombre, base_clases, diccionario):
        diccionario.update(dict({"verificar": cls.verificar(),
                                 "nuevo_empleado": cls.nuevo_empleado(),
                                 "subir_sueldo": cls.subir_sueldo(),
                                 }))
        super().__new__(cls, nombre, base_clases, diccionario)

    def verificar(cls):
        pass

    def nuevo_empleado(cls):
        self.empleados.update({"{}".format(self.id_empleado)})
        pass

    def subir_sueldo(cls):
        pass

    def __call__(self, *args, **kwargs):
        pass


class MetaPersona(type):

    def __new__(cls, nombre, base_clases, diccionario):
        diccionario.update(dict({"verificar": cls.verificar(),
                                 "hacer_tarea": cls.hacer_tarea()}))

    def verificar(cls):
        pass

    def hacer_tarea(cls):
        pass

