__author__ = 'Vicente'

import sistema as sis
import lib.estructura_datos as datos
import lib.conexion as conexion
import lib.puerto as puerto


class Red:
    def __init__(self):
        self.lista_puertos = puerto.ListaPuertos()
        self.bummer = sis.puerto_final()

    def recorrer(self):
        self.lista_puertos.agregar_puerto(puerto.Puerto(0))

        iteraciones = 1
        while self.saber_cuando_parar(iteraciones):
            if sis.preguntar_puerto_actual()[1]:
                print("cagaste")
                break
            puerto_actual = self.lista_puertos.ultimo_agregado
            puerto_actual.posibles_conexiones = sis.posibles_conexiones()
            self.siguiente(puerto_actual)
            iteraciones += 1

        # return self.imprimir_red()

    def siguiente(self, puerto_actual):
        id_conexion = puerto_actual.decidir_conexion()
        nueva_conexion = conexion.Conexion(id_conexion, puerto_actual)
        puerto_actual.agregar_conexion(nueva_conexion)
        sis.hacer_conexion(nueva_conexion.id)
        nuevo_puerto = puerto.Puerto(sis.preguntar_puerto_actual()[0])
        puerto_actual.conexiones.get_by_id(id_conexion).agregar_destino(nuevo_puerto)
        self.lista_puertos.agregar_puerto(nuevo_puerto)

    def saber_cuando_parar(self, iteraciones):
        if iteraciones % 1000 == 0: #revisar cada 20.000 iteraciones
            # para cada puerto
            # revisar si se paso por todas las conexiones un minimo de x veces
            return False
        return True

    def imprimir_red(self):
        # iterar sobre el los ids de los puertos
        # iterar sobre las conexiones de cada puerto
        # crear dos partes: una con puertos otra con conexiones
        # juntar ambas y crear red.txt
        pass

    def ruta_a_bummer(self):
        conexiones_a_bummer = datos.Lista()
        self.lista_puertos.recorrer_conexiones(conexiones_a_bummer)
        with open("rutaABummer.txt", "W") as f:
            f.write(conexiones_a_bummer)

    def dikjstra(self, id_inicio, id_final):
        pass

    def rutas_doble_sentido(self):
        with open("rutasDobleSentido.txt", "w") as f:
            f.write("hola")
        pass

    def obtener_ciclos(self):
        # obtener_triangulos()
        # obtener_cuadrados()
        # juntar y crear ciclos.txt
        pass

