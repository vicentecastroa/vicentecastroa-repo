__author__ = 'Vicente'

from lib.personas import Profesor as P, Alumno as A
from lib.cursos import Curso as Cur
from lib.actividades import Evaluacion as Ev

class LecturaDatos:

    def __init__(self):
        self.profesores = {}
        self.alumnos = {}
        self.lista_cursos = {}
        self.evaluaciones = {}

    def __repr__(self):
        return "datoooos"

    def crear_usuario(self):
        with open('datos/personas.txt', 'r', encoding="utf8") as f:
            datos = {}
            pid = 1  # identificador profesores: pxxxxxxxx
            aid = 1  # identificador alumnos: axxxxxxxx
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
                                          nombre=datos['nombre']
                                          )
                        self.profesores["p{}".format(pid)] = nuevo_usuario
                        pid += 1

                    else:
                        nuevo_usuario = A(ramos_pre=datos['ramos_pre'],
                                          idolos=datos['idolos'],
                                          usuario=datos['usuario'],
                                          clave=datos['clave'],
                                          nombre=datos['nombre']
                                          )
                        self.alumnos["a{}".format(aid)] = nuevo_usuario
                        aid += 1
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

                if '},' in linea: #crear curso con nombre nrc y guardar en lista de cursos
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

                    for curso in self.lista_cursos.values():  #agrego la evaluacion a los cursos
                        if nueva_ev.sigla == curso.sigla:
                            if nueva_ev.sec == curso.seccion:
                                c = curso.evaluaciones
                                curso.evaluaciones["{}".format(nueva_ev.tipo)] = nueva_ev

                    self.evaluaciones["{}".format(eid)] = nueva_ev  #agrego a una "base de datos" de evaluaciones
                    datos = {}
                eid += 1
'''
class Resquisito():
    def __init__(self):
        self.requisitos = self.agregar_requisitos()'''
'''
    def agregar_requisitos(self):
        requisitos = {}
        with open('../datos/requsitos.txt', 'r', encoding="utf8") as f:
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
                    requisitos['{}'.format(nuevo_requisito.sigla)] = nuevo_requisito

        return requisitos
'''