__author__ = 'Vicente'

from main import Base, Ramo, Alumno


class BaseTest:

    def setup_method(self, method):
        self.base = Base()
        self.base.db.append(Ramo("RAMOSINVACANTES", "0", "10"))
        self.alumnos = [Alumno(self.base, 0, "vicente"),
                        Alumno(self.base, 50, "jose")
                        ]

    def teardown_method(self, method):
        del self.base
        del self.alumnos


class TestSistema(BaseTest):

    def test_vacantes(self):
        assert self.alumnos[0].tomar_ramo("ICT2443")
        assert not self.alumnos[0].tomar_ramo("RAMOSINVACANTES")

    def test_maximocreditos(self):
        assert self.alumnos[0].tomar_ramo("IIC1237")

        self.alumnos[0].tomar_ramo("IIC1134")
        self.alumnos[0].tomar_ramo("MAT1620")
        self.alumnos[0].tomar_ramo("ICS1112")

        assert not self.alumnos[0].tomar_ramo("IIC1237")  # ya tomo muchos ramos
        assert not self.alumnos[1].tomar_ramo("MAT1620")  # ya tiene 50 creditos
        assert not self.alumnos[0].tomar_ramo("IIC2233")  # excede maximo creditos. ramo 55

    def test_ramo_repetido(self):
        self.alumnos[0].tomar_ramo("IIC1237")
        assert not self.alumnos[0].tomar_ramo("IIC1237")

    def test_eliminar_ramo(self):
        self.alumnos[0].tomar_ramo("MAT1630")
        assert self.alumnos[0].botar_ramo("MAT1630")  # eliminar ramo tomado
        assert not self.alumnos[0].botar_ramo("MAT1630")  # eliminar de nuevo el ramo que una vez tomo
        assert not self.alumnos[0].botar_ramo("ICM1003")  # eliminar el ramo que no tiene




