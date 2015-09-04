__author__ = 'Vicente'

from lib.personas import Profesor as P, Alumno as A
from lib.cursos import Curso as Cur, Requisito as Req
from lib.actividades import Evaluacion as Ev
from math import trunc


class LecturaDatos:
    def __init__(self):
        self.profesores = {}
        self.alumnos = {}
        self.lista_cursos = {}
        self.evaluaciones = {}
        self.requisitos = {}

    def __repr__(self):
        return "datos"

    def crear_usuario(self):
        with open('datos/personas.txt', 'r', encoding="utf8") as f:
            datos = {}
            for linea in f:
                if '":' in linea:
                    a = linea.split(',')[0]
                    key = a[a.find('"') + 1:a.find('":')]
                    valor = a[a.find(': ') + 2:].replace('"', '')
                    if valor == "[\n" or valor == "[]":
                        valor = []
                        key_lista = key
                    datos.update({key: valor})

                elif '"' in linea:
                    datos[key_lista].append(linea[linea.find('"') + 1:linea.rfind('"')])

                if '}' in linea:
                    if datos['alumno'] == "NO":
                        nuevo_usuario = P(usuario=datos['usuario'],
                                          clave=datos['clave'],
                                          nombre=datos['nombre'].strip("\n")
                                          )
                        self.profesores["{}".format(datos['usuario'])] = nuevo_usuario
                    else:
                        nuevo_usuario = A(ramos_pre=datos['ramos_pre'],
                                          idolos=datos['idolos'],
                                          usuario=datos['usuario'],
                                          clave=datos['clave'],
                                          nombre=datos['nombre'].strip("\n")
                                          )
                        self.alumnos["{}".format(datos['usuario'])] = nuevo_usuario
                    key_lista = []
                    datos = {}

    def crear_cursos(self):

        with open('datos/cursos.txt', 'r', encoding="utf8") as f:
            datos = {}
            for linea in f:
                if '":' in linea:
                    a = linea.split(',')[0]
                    key = a[a.find('"') + 1:a.find('":')]
                    valor = a[a.find(': ') + 2:].replace('"', '')
                    if valor == "[\n" or valor == "[]":
                        valor = []
                        key_lista = key
                    datos.update({key: valor})

                elif '"' in linea:
                    datos[key_lista].append(linea[linea.find('"') + 1:linea.rfind('"')])

                if '},' in linea:  # crear curso con nombre nrc y guardar en lista de cursos
                    nuevo_curso = Cur(sigla=datos['sigla'],
                                      seccion=datos['sec'],
                                      profesor=datos['profesor'],
                                      ofr=datos['ofr'],
                                      creditos=datos['cred'],
                                      nrc=datos['NRC'],
                                      campus=datos['campus'],
                                      extra=datos
                                      )

                    self.lista_cursos["{}".format(datos['NRC'])] = nuevo_curso
                    datos = {}

    def crear_evaluaciones(self):

        with open('datos/evaluaciones.txt', 'r', encoding="utf8") as f:

            datos = {}
            eid = 1
            for linea in f:
                if ':' in linea:
                    l = linea
                    key = l[l.find('"') + 1:l.find(':') - 1]
                    valor = l[l.find(':') + 2:-2].replace('"', '')
                    datos.update({key: valor})
                if '}' in linea:
                    nueva_ev = Ev(sigla=datos['sigla'],
                                  sec=datos['sec'],
                                  fecha=datos['fecha'],
                                  tipo=datos['tipo']
                                  )

                    for curso in self.lista_cursos.values():  # agrego la evaluacion a los cursos
                        if nueva_ev.sigla == curso.sigla:
                            if nueva_ev.sec == curso.seccion:
                                c = curso.evaluaciones
                                curso.evaluaciones["{}".format(nueva_ev.tipo)] = nueva_ev

                    self.evaluaciones["{}".format(eid)] = nueva_ev  # agrego a una "base de datos" de evaluaciones
                    datos = {}
                eid += 1

    def obtener_horario(self):

        for curso in self.lista_cursos.values():
            if "hora_cat" in curso.info:
                a = curso.info.get("hora_cat").split(':')
                dias = a[0].split("-")
                modulos = a[1].split(",")
                for dia in dias:
                    for modulo in modulos:
                        curso.horario.append("{}:{}-CAT".format(dia, modulo))

            if "hora_ayud" in curso.info:
                b = curso.info.get("hora_ayud").split(':')
                dias = b[0].split("-")
                modulos = b[1].split(",")
                for dia in dias:
                    for modulo in modulos:
                        curso.horario.append("{}:{}-AYU".format(dia, modulo))

            if "hora_lab" in curso.info:
                c = curso.info.get("hora_lab").split(':')
                dias = c[0].split("-")
                modulos = c[1].split(",")
                for dia in dias:
                    for modulo in modulos:
                        curso.horario.append("{}:{}-LAB".format(dia, modulo))

    def calcular_bacanosidad(self):
        bacanes = {}  # ponderadores
        lista_bacanosidad = {}  # bacanosidad

        for alumno in self.alumnos.values():  # Valor de cada seguidor. 1 / maximo de seguidores.
            for idolo in alumno.idolos:
                if idolo in bacanes:
                    bacanes[idolo] += 1
                if idolo not in bacanes:
                    bacanes["{}".format(idolo)] = 1
                    lista_bacanosidad["{}".format(idolo)] = 0

        mas_seguidores = max(bacanes.values())
        valor_seguidor = 100 / mas_seguidores

        for bacan in bacanes:  # asigna un valor de que bacan siga a una persona. escala de 0 a 1
            bacanes[bacan] *= round(valor_seguidor, 3)


        # asignar bacanosidad. Sumar ponderador a alumno.bacanosidad
        for alumno in self.alumnos.values():
            for idolo in alumno.idolos:
                lista_bacanosidad[idolo] += bacanes[alumno.nombre]

        with open('./datos/bacanosidad.txt', 'w', encoding="utf8") as b:
            for bacanosidad in lista_bacanosidad:
                b.write("{} : {}\n".format(bacanosidad, trunc(lista_bacanosidad[bacanosidad])))

    def ordenar_bacanosidad(self):
        with open("./datos/bacanosidad.txt", "r", encoding="utf8") as bac:
            dict_bacanosidades = {}
            for linea in bac:
                linea = linea.strip("\n").split(' : ')
                dict_bacanosidades.update({linea[0]: linea[1]})

            ordenado = sorted(dict_bacanosidades.items(), key=lambda x: x[1])

        with open("./datos/bacanosidad.txt", "w", encoding="utf8") as bac:
            for bacan in ordenado[::-1]:
                bac.write("{} : {}\n".format(bacan[0], bacan[1]))

    def obtener_grupo(self):
        with open("./datos/bacanosidad.txt", "r", encoding="utf8") as bac:
            lines = bac.readlines()
            for alumno in self.alumnos.values():
                for linea in lines:
                    if alumno.nombre in linea:
                        indice = lines.index(linea)
                        if indice <= 434:
                            alumno.grupo_bummer = 1
                        elif indice <= (435 * 2) - 1:
                            alumno.grupo_bummer = 2
                        elif indice <= (435 * 3) - 1:
                            alumno.grupo_bummer = 3
                        elif indice <= (435 * 4) - 1:
                            alumno.grupo_bummer = 4
                        elif indice <= (435 * 5) - 1:
                            alumno.grupo_bummer = 5
                        elif indice <= (435 * 6) - 1:
                            alumno.grupo_bummer = 6
                        elif indice <= (435 * 7) - 1:
                            alumno.grupo_bummer = 7
                        elif indice <= (435 * 8) - 1:
                            alumno.grupo_bummer = 8
                        elif indice <= (435 * 9) - 1:
                            alumno.grupo_bummer = 9
                        else:
                            alumno.grupo_bummer = 10

    def agregar_requisitos(self):
        with open('./datos/requisitos.txt', 'r', encoding="utf8") as f:
            datos = {}
            for linea in f:
                if ':' in linea:
                    l = linea
                    key = l[l.find('"') + 1:l.find(':') - 1]
                    valor = l[l.find(':') + 2:-2].replace('"', '')
                    datos.update({key: valor})
                if '}' in linea:
                    nuevo_requisito = Req(sigla=datos['sigla'],
                                          equiv=datos['equiv'],
                                          prerreq=datos['prerreq']
                                          )
                    self.requisitos['{}'.format(nuevo_requisito.sigla)] = nuevo_requisito
