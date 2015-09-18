__author__ = 'Vicente'

from datos import Nodo, Lista
from puertos import Puerto
import sistema as sis


def saber_cuando_parar(iteraciones):
    if iteraciones % 5000 == 0:
        #revisar si recorrio todas las conexiones
        return False
    return True

def imprimir_red(lista_puertos):
    with open("red.txt", "w") as f:
        for puerto in lista_puertos:
            f.write(puerto.valor)

        for puerto in lista_puertos:
            for conexion in puerto.valor.conexiones:
                f.write(conexion)
    pass

def ruta_a_bummer(lista_puertos):
    lista_conexiones = None
    return lista_conexiones


if __name__ == "__main__":

    lista_puertos = Lista()

    ultimo_puerto = None
    iteraciones = 1

    while saber_cuando_parar(iteraciones):
        puerto_actual = Puerto(sis.preguntar_puerto_actual()[0])
        puerto_actual.conexiones_posibles = sis.posibles_conexiones()

        if puerto_actual.id not in lista_puertos:
            if len(lista_puertos) == 0:  # agregar el primer puerto
                nodo_actual = Nodo(puerto_actual)
                lista_puertos.add_nodo(nodo_actual)
            else:
                nodo_actual = Nodo(puerto_actual)
                nodo_anterior = lista_puertos.ultimo
                nodo_anterior.valor.hijos.add_nodo(Nodo(puerto_actual.id))
                nodo_actual.valor.padres.add_nodo(Nodo(nodo_anterior.valor.id))
                lista_puertos.add_nodo(nodo_actual)

        else:
            nodo_actual = lista_puertos.get_nodo(puerto_actual.id)  # obener nodo
            nodo_padre = lista_puertos.get_nodo(ultimo_puerto)
            nodo_actual.valor.padres.add_nodo(nodo_padre)  # agregar el padre
            nodo_padre.valor.hijos.add_nodo(nodo_actual.valor)  # agregar hijo

        id_conexion = puerto_actual.decidir_conexion()
        puerto_actual.conexiones.add_nodo(Nodo(Lista()))
        sis.hacer_conexion(id_conexion)

        puerto_nuevo = Puerto(sis.preguntar_puerto_actual()[0])
        ultimo_puerto = puerto_nuevo.id

        puerto_actual.conexiones[id_conexion].add_nodo(Nodo(puerto_nuevo.id))
        iteraciones += 1






