__author__ = 'Vicente'
from lib.actividades import Evaluacion as Ev


class Curso:
    def __init__(self, sigla='', seccion='', profesor='', ofr='', creditos='', nrc='', campus='', extra=''):
        self.nrc = nrc
        self.sigla = sigla
        self.seccion = seccion
        self.profesor = profesor
        self.horario = []
        self.evaluaciones = {}
        self.requisitos = None
        self.ofr = int(ofr)
        self.ocu = 0
        self.disp = self.ofr-self.ocu
        self.cred = creditos
        self.campus = campus
        self.info = extra

    def __repr__(self):
        return "{} objeto".format(self.sigla)


class Requisito:
    def __init__(self, sigla='', equiv='', prerreq=''):
        self.sigla = sigla
        self.equiv = equiv
        self.prerreq = prerreq
