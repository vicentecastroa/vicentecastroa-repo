
BUMMER VERSION YO

I. **ESTRUCTURA DEL PROGRAMA**
    El programa tiene el main que se debe ejecutar.

    (i) **lecturadatos.py**: contiene las funciones para iniciar el programa. Lee los archivos de la carpeta
        datos y los carga en diccionarios para alumnos, profesores, cursos, evaluaciones y requisitos. También tiene
        las funciones para determinar la bacanosidad de los alumnos y agregarlas como atributo.

    (ii) **interfaz_bummer**: se define en interfaz.py. Ejecuta los prints en consola y las funciones que permite
        realizar el programa, definidas en funciones_banner.py

    (iii) **Alumno, Profesor, Persona**: los primeros heredan de la clase Persona. se definen en personas.py
        Contienen los inicializadores con los respectivos atributos de cada uno.

    (iv)

II. **METODOS**

    01. LECTURADATOS

        (i) crear_usuario(): lee el archivo personas.txt y agrega las personas creadas como objeto a la lista
            de profesores o alumnos según corresponda.

        (ii) crear_cursos(): lee el archivo cursos.txt. Agrega al diccionario de cursos cada curso instanciado como objeto

        (iii) crear_evaluaciones(): lee el archivo evaluaciones.txt. Agrega a cada curso y a un diccionario de evaluaciones, cada evaluacion
                instanciada como objeto.

        (iv) obtener_horario(): retorna una lista con las horas de clases de la forma DIA:MODULO-TIPO

        (v) calcular_bacanosidad(): calcula la bacanosidad de cada alumno. Primero se obtiene el máximo de seguidores. Se asigna un peso a cada persona segun cantidad de seguidores.
            La bacanosidad es la suma de los pesos de los seguidores que tiene cada persona. Retorna un archivo .txt con los nombres:bacanosidad

        (vi) ordenar_bacanosidad(): ordena el archivo bacanosidad.txt según bacanosidad descendente.

        (v) obtener_grupo(): según posición en el ranking de bacanosidad, el alumno es asignado a un grupo. Se agrega como atributo al alumno.


    02. FUNCIONES_BANNER

        (i) inscribir_curso(alumno, preferencias, datos, excepcion=None): recibe un objeto alumno, una lista con nrc preferentes, la base de datos.
            Corrobora los requisitos para inscribir un curso. Excepto prerrequisitos (sorry). Lo agrega a la carga academica del alumno, y modifica los cupos del curso.
            Exepción por default es None. Si un profesor llama este metodo, excepcion = True y se salta los requisitos según enunciado.

        (ii) eliminar_curso(alumno, nrc): revisa si el curso que desea botar está en la carga academica del alumno y luego lo borra. Aumenta las vacantes del curso.

        (iii) ver_horario(alumno): recorre los ramos de la carga academica del alumno y los horarios de sus ramos. retorna una lista con DIA:MODULO-TIPO-SIGLA



    DEFICITS:
    - no controla tope de campus
    - no controla prerrequisitos



