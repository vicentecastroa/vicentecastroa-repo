__author__ = 'Vicente'

from utils.parser import ApacheLogsParser
from functools import reduce

class BigAnalizador:

    def __init__(self, logs):
        self.logs = logs

    def bytes_transferidos(self):
        bytes = list(map(lambda x: x.size, self.logs))
        suma = reduce(lambda x,y: x + y, bytes)
        return print("Numero de bytes transferidos: {}".format(suma))


    def errores_servidor(self):
        tipos_errores = ['404', '500', '501']
        errores = list(filter(lambda x: x.status in tipos_errores, self.logs))
        cantidad_errores = len(errores)

        return print("Numero de solicitudes erroneas: {}".format(cantidad_errores))


    def solicitudes_exitosas(self):
        tipo_exito = ['200', '202', '304']
        exitos = list(filter(lambda x: x.status in tipo_exito, self.logs))
        cantidad_exito = len(exitos)

        return print("Numero de solicitudes exitosas: {}".format(cantidad_exito))

    def url_mas_solicitada(self):
        pass

if __name__ == '__main__':
    parser = ApacheLogsParser("./utils/nasa_logs_week.txt")
    logs = parser.get_apache_logs()
    biganalizador = BigAnalizador(logs)

    biganalizador.bytes_transferidos()
    biganalizador.errores_servidor()
    biganalizador.solicitudes_exitosas()
    biganalizador.url_mas_solicitada()
