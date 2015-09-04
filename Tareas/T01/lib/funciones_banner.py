__author__ = 'Vicente'
# coding=utf8

from datetime import    time, date


def inscribir_cursos(alumno, preferencias, datos, excepcion=False):
    cursos_por_tomar = []

    for nrc in preferencias:
        if nrc not in datos.lista_cursos:
            return print("ERROR: El curso con NRC: {} no existe.".format(nrc))
        if nrc in alumno.carga_academica:
            return print("ERROR: El curso NRC:{} ya se encuentra en su carga academica".format(nrc))
        cursos_por_tomar.append(datos.lista_cursos[nrc])

    if not excepcion:
        if not revisar_creditos(alumno, cursos_por_tomar):
            return print("ERROR: Los creditos por tomar están fuera del rango permitido")

        if not revisar_tope_evaluaciones(alumno, cursos_por_tomar):
            return print("ERROR: Los cursos que usted quiere inscribir tienen tope en sus evaluaciones")

        if not revisar_tope_horario(alumno, cursos_por_tomar):
            return print("ERROR: Los cursos que usted quiere inscribir presentan tope de horario")

        excepcion = True

    if excepcion:  # si es profesor, se salta la parte de las restricciones
        for i in range(len(cursos_por_tomar)):
            curso = cursos_por_tomar.pop(i)
            if not revisar_cupos(curso, datos):
                return print("El curso NRC: {} no tiene cupos".format(curso.nrc))
            agregar_curso(alumno, curso, datos)

    return print("Su operación ha sido exitosa")


def revisar_hora(alumno, hora_ingresada):
    grupo = alumno.grupo_bummer
    """hora_actual = time(hour=datetime.now().hour, minute=datetime.now().minute)"""
    hora_actual = hora_ingresada
    if grupo == 1:
        if hora_actual >= time(hour=8, minute=30) and hora_actual <= time(hour=10, minute=30):
            return True
    if grupo == 2:
        if hora_actual > time(hour=9, minute=30) and hora_actual <= time(hour=11, minute=30):
            return True
    if grupo == 3:
        if hora_actual >= time(hour=10, minute=30) and hora_actual <= time(hour=12, minute=30):
            return True
    if grupo == 4:
        if hora_actual >= time(hour=11, minute=30) and hora_actual <= time(hour=13, minute=30):
            return True
    if grupo == 5:
        if hora_actual >= time(hour=12, minute=30) and hora_actual <= time(hour=14, minute=30):
            return True
    if grupo == 6:
        if hora_actual >= time(hour=13, minute=30) and hora_actual <= time(hour=15, minute=30):
            return True
    if grupo == 7:
        if hora_actual >= time(hour=14, minute=30) and hora_actual <= time(hour=16, minute=30):
            return True
    if grupo == 8:
        if hora_actual >= time(hour=15, minute=30) and hora_actual <= time(hour=17, minute=30):
            return True
    if grupo == 9:
        if hora_actual >= time(hour=16, minute=30) and hora_actual <= time(hour=18, minute=30):
            return True
    if grupo == 10:
        if hora_actual >= time(hour=17, minute=30) and hora_actual <= time(hour=19, minute=30):
            return True

    return False


def revisar_creditos(alumno, cursos_por_tomar):
    max_cred = alumno.max_creditos
    cred_tomados = alumno.creditos_tomados
    cred_por_tomar = 0
    for curso in cursos_por_tomar:
        cred_por_tomar += curso.cred

    if cred_por_tomar + cred_tomados > max_cred or cred_por_tomar + cred_tomados < 30:
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


def revisar_tope_horario(alumno, cursos_por_tomar):
    clases = []
    for curso in alumno.carga_academica:
        for clase in curso.horario:
            clases.append(clase)
    for curso in cursos_por_tomar:
        for clase in curso.horario:
            if clase in clases:
                return False
    return True


def revisar_requisitos(alumno, cursos_por_tomar):
    pass


def revisar_cupos(curso, datos):
    a = datos.lista_cursos[curso.nrc]
    if a.disp == 0:
        return False
    return True


def agregar_curso(alumno, curso, datos):
    alumno.carga_academica["{}".format(curso.nrc)] = curso
    alumno.creditos_tomados += curso.cred
    datos.lista_curso[curso.nrc].ocu += 1


def eliminar_curso(alumno, nrc, datos):
    if nrc not in alumno.carga_academica:
        return print("ERROR: El curso que quiere eliminar no se encuentra en su lista de cursos")

    alumno.creditos_tomados -= alumno.carga_academica[nrc].cred
    curso = datos.lista_cursos[nrc]
    curso.ocu -= 1
    del alumno.carga_academica[nrc]
    return print("Su operación ha sido exitosa")


def ver_horario(alumno):
    horario = []
    for curso in alumno.carga_academica.values():
        for clase in curso.horario:
            horario.append("{}-{}/{}".format(clase, curso.sigla, curso.seccion))
    return horario


def descargar_evaluaciones(alumno):
    ev = []
    for curso in alumno.carga_academica.values():
        for evaluacion in curso.evaluaciones.values():
            ev.append(evaluacion)

    def get_fecha(fecha):
        fecha = fecha.split(" - ")
        dia = int((fecha[0].split("/"))[0])
        mes = int((fecha[0].split("/"))[1])
        fecha = date(2015, month=mes, day=dia)
        return fecha

    ev = sorted(ev, key=lambda x: get_fecha(x.fecha))

    return ev


def revisar_profesor(usuario, nrc, datos):
    curso = datos.lista_cursos[nrc]
    nombre = usuario.nombre
    if nombre in curso.profesor:
        return True
    return False
