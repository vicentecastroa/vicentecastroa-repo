__author__ = 'Vicente'
# coding=UTF-8
import mapa
import vehiculos
import ataques
import celdas


class BaseTest:

    def setup_method(self, method):
        self.mapas = {"mapa_atack_a": mapa.MapaAire("mapa_prueba"),
                      "mapa_atack_m": mapa.MapaMar("mapa_prueba"),
                      "mapa_defensa_a": mapa.MapaAire("mapa_prueba"),
                      "mapa_defensa_m": mapa.MapaMar("mapa_prueba")
                      }

        self.vehiculos = {"barco_p": vehiculos.BarcoPequeno(),
                          "explorador": vehiculos.Explorador(),
                          "lancha": vehiculos.Lancha(),
                          "puerto": vehiculos.Puerto()
                          }

        self.ataques = {"kmz": ataques.Kamikaze(),
                        "trident": ataques.Trident(),
                        "tomahawk": ataques.Tomahawk(),
                        "minute": ataques.Minuteman(),
                        "paralizer": ataques.Paralizer(),
                        "ing": ataques.Ingenieros()
                        }

    def teardown_method(self, method):
        del self.mapas
        del self.vehiculos
        del self.ataques


class TestMapa(BaseTest):

    def test_posicion_random(self):
        mapa = self.mapas["mapa_atack_m"]
        mapa.posicionar_random()
        pass

    def test_ubicar_elemento(self):
        mapa = self.mapas["mapa_atack_m"]
        bote = self.vehiculos["barco_p"]
        puerto = self.vehiculos["puerto"]

        mapa.ubicar_elemento(bote, (5, 5))
        assert bote in mapa.vehiculos_actual
        assert bote.pos_actual == (5, 5)
        assert not mapa.ubicar_elemento(puerto, (6, 5))
        assert mapa.ubicar_elemento(bote, (10, 10))
        assert not mapa.ubicar_elemento(puerto, (14, 14))


    def test_check_espacio(self):
        mapa = self.mapas["mapa_atack_m"]
        bote = self.vehiculos["barco_p"]
        bote.pos_actual = (1, 1)
        puerto = self.vehiculos["puerto"]
        mapa.vehiculos_actual.append(bote)

        assert not mapa.check_espacio(puerto, (0, 0))
        assert mapa.check_espacio(puerto, (10, 10))
        assert not mapa.check_espacio(puerto, (13, 13))
        assert not mapa.check_espacio(puerto, (0, 1))
        assert not mapa.check_espacio(puerto, (1, 1))

    def test_celdas_ocupadas(self):
        mapa = self.mapas["mapa_atack_m"]
        bote = self.vehiculos["barco_p"]
        bote.pos_actual = (1, 1)
        mapa.vehiculos_actual.append(bote)

        assert (1, 1) in mapa.casillas_ocupadas()
        assert (2, 1) in mapa.casillas_ocupadas()
        assert not (5, 5) in mapa.casillas_ocupadas()

    def test_get_elemento(self):
        mapa = self.mapas["mapa_atack_m"]
        bote = self.vehiculos["barco_p"]
        bote.pos_actual = (1, 1)
        mapa.vehiculos_actual.append(bote)

        assert isinstance(mapa.get_elemento((1, 1))[0], vehiculos.BarcoPequeno)  # encuentra el barco
        assert mapa.get_elemento((1, 1))[1]  # lo buscado encuentra el barco
        assert not mapa.get_elemento((1, 1), (5, 5))[1]  # solo parte de lo buscado encuentra el barco
        assert not mapa.get_elemento((10, 10), (3, 3))  # no encuentra nada


class TestVehiculos(BaseTest):

    def test_atacado(self):
        barco = self.vehiculos["barco_p"]
        barco.pos_actual = (1, 1)
        assert barco.atacado(self.ataques["minute"])
        assert barco.resistencia == 15
        barco.atacado(self.ataques["ing"])
        assert barco.resistencia == 16
        assert barco.atacado(self.ataques["trident"])
        assert barco.resistencia == 11
        assert not barco.atacado(self.ataques["minute"])
        barco.resistencia = 15
        assert not barco.atacado(self.ataques["minute"])

        barco.resistencia = 200
        assert not barco.atacado(self.ataques["kmz"])

    def test_estado_explorador(self):
        explorador = self.vehiculos["explorador"]
        assert not explorador.paralizado

        explorador.atacado()
        explorador.actualizar_estado()
        assert explorador.paralizado

        explorador.paralizado = False
        explorador.atacado()
        for _ in range(5):
            explorador.actualizar_estado()
        assert not explorador.paralizado

        explorador.paralizado = False
        explorador.atacado()
        for _ in range(4):
            explorador.actualizar_estado()
        assert explorador.paralizado

    def test_mover(self):
        barco = self.vehiculos["barco_p"]
        lancha = self.vehiculos["lancha"]

        barco.pos_actual = (1, 1)
        lancha.pos_actual = (1, 1)

        assert barco.mover("D") == (1, 2)
        assert barco.mover("A") == (1, 0)
        assert barco.mover("Q") == (0, 0)
        assert barco.mover("W") == (0, 1)
        assert barco.mover("E") == (0, 2)
        assert barco.mover("Z") == (2, 0)
        assert barco.mover("X") == (2, 1)
        assert barco.mover("C") == (2, 2)
        assert not barco.mover("S")

        assert lancha.mover((5, 5)) == (5, 5)


class TestAtaques(BaseTest):

    def test_disponibilidad_ataque(self):
        ataque = self.ataques["tomahawk"]
        ataque_2 = self.ataques["trident"]
        assert ataque.disponible
        assert ataque_2.disponible
        ataque.usar()
        ataque.actualizar_disponibilidad()
        ataque_2.usar()
        ataque_2.actualizar_disponibilidad()
        assert not ataque.disponible
        assert ataque_2.disponible
        ataque.actualizar_disponibilidad()
        assert not ataque.disponible
        ataque.actualizar_disponibilidad()
        assert not ataque.disponible
        ataque.actualizar_disponibilidad()
        assert ataque.disponible


class TestCeldas(BaseTest):

    def test_celdas_ocupadas(self):
        vehiculo = self.vehiculos["barco_p"]
        vehiculo.pos_actual = (5, 5)
        celdas_ocupadas = celdas.celdas_ocupadas(vehiculo.pos_actual, vehiculo.size)

        assert not (4, 4) in celdas_ocupadas
        assert (6, 5) in celdas_ocupadas
        assert not (5, 6) in celdas_ocupadas
        assert not (8, 5) in celdas_ocupadas

    def test_coord_to_index(self):
        assert celdas.coord_to_index("A3") == (2, 0)
        assert not celdas.coord_to_index("A16")
        assert not celdas.coord_to_index("13B")
        assert not celdas.coord_to_index("AA12")
        assert not celdas.coord_to_index("X1")
        assert celdas.coord_to_index("O15")
        assert not celdas.coord_to_index("1234")

    def test_index_to_coord(self):
        assert celdas.index_to_coord((0, 0)) == "A1"
        assert not celdas.index_to_coord((-1, "a"))
        assert not celdas.index_to_coord((15, 15))
        assert celdas.index_to_coord((14, 14)) == "O15"
        assert celdas.index_to_coord((5, 1)) == "B6"