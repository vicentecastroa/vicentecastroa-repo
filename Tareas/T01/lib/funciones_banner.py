__author__ = 'Vicente'
from lib.personas import Profesor as Prof, Alumno as Alum
from lib.lecturadatos import LecturaDatos as Datos



def inscribir_cursos(alumno, preferencias):
    ''''
    Recibe como argumentos un objeto alumno y una lista con los nrc de
    los cursos que alumno desea tomar.
    Revisa la existencia de cursos, máximo de créditos permitidos del alumno,
    requisitos, topes de horario y evaluaciones.
    Si todo está bien, agrega los cursos a la carga academica de la persona y
    actualiza los cupos de los cursos.
    ''''
    cursos_por_tomar = []
    '''
    requisitos
    topes de horario
    '''
    for nrc in preferencias:
        if nrc not in datos.lista_cursos:
            return "ERROR: El curso con NRC: {} no existe.".format(nrc)
        if nrc in alumno.carga_academica:
            return "ERROR: El curso NRC:{} ya se encuentra en su carga academica".format(nrc)
        cursos_por_tomar.append(datos.lista_cursos[nrc])

    if revisar_creditos(alumno, cursos_por_tomar) == False:
        return "ERROR: Excede máximo de créditos permitidos"

    if revisar_tope_evaluaciones(alumno, cursos_por_tomar) == False:
        return "ERROR: Los cursos que usted quiere inscribir tienen tope en sus evaluaciones"


    for i in range(len(cursos_por_tomar)):
        agregar_curso(alumno, cursos_por_tomar.pop(i))


def revisar_creditos(alumno, cursos_por_tomar):

    max_cred = alumno.max_creditos
    cred_tomados = alumno.creditos_tomados
    cred_por_tomar = 0
    for curso in cursos_por_tomar:
        cred_por_tomar += curso.cred

    if cred_por_tomar + cred_tomados > max_cred:
        return False
    return True


def revisar_tope_evaluaciones(alumno, cursos_por_tomar):

    fechas_evaluaciones = []
    for curso_tomado in alumno.carga_academica:
        for ev in curso_tomado.evaluaciones:
            fechas_evaluaciones.append(ev.fecha)
    for curso in cursos_por_tomar:
        for ev in curso.evaluaciones:
            if ev.fecha in fechas_evaluaciones:
                return False
            fechas_evaluaciones.append(ev.fecha)
    return True


def agregar_curso(alumno, curso):
    alumno.carga_academica["{}".format(curso.nrc)] = curso
    alumno.creditos_tomados += curso.cred
    curso.ocu +=1


def actualizar_carga_academica(alumno,accion,nrc):  # accion: tomar o botar
    if accion == "botar":
        try:
            del alumno.carga_academica[nrc]
        except KeyError:
            retur

    if accion == "tomar":
        for key in alumno.carga_academica:
            if key == nrc:
                pass #usted ya tiene este ramo. ERROR
            else:
                alumno.carga_academica[nrc] = Cursos.lista[nrc]