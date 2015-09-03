__author__ = 'Vicente'
from lib.actividades import Evaluacion as Ev
class Curso:

    def __init__(self, sigla='', seccion='', profesor='', ofr='', creditos='', nrc='', campus='',extra=''):
        self.nrc = nrc
        self.sigla = sigla
        self.seccion = seccion
        self.profesor = profesor
        self.horario = {}  # 'L-1' : [sigla , tipo]
        self.evaluaciones = {}
        self.requisitos = None
        self.ofr = ofr
        self.ocu = 0
        self.disp = ofr
        self.cred = creditos
        self.campus = campus
        self.info = extra

    def __repr__(self):
        return "{} objeto".format(self.sigla)

    def get_requisitos(self, requisito):
        self.requisitos = requisito.prerreq

    def horario(self):  # usar info
        for key in self.info:
            pass

    def actualizar_cupos(self, accion):  # tomar o botar
        if accion == 'tomar':
            self.disp -= 1
            self.ocu += 1
        if accion == 'botar':
            self.disp += 1
            self.ocu -= 1


    def revisar_tope_pruebas(self, otro_curso):
        for prueba_self in self.evaluaciones.values():
            for prueba_other in otro_curso.evaluaciones.values():
                if prueba_self.fecha == prueba_other.fecha:
                    return True
        return False

class Requisito:

    def __init__(self, sigla='',equiv='',prerreq=''):
        self.sigla = sigla
        self.equiv = equiv
        self.prerreq = prerreq

