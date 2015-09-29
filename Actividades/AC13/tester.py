__author__ = 'Vicente'

import unittest
import os
from main import Corrector

class TestearArchivo(unittest.TestCase):

    def setUp(self):
        self.nombres = ["5435466-5_lucas_hidalgo.txt",
                        "6968271-5_Andrea_valdes.ttxtt",
                        "18936676-0_antonio_lopez.txt",
                        "18936677-k_rodrigo_lave.txt"
                        ]

        self.correctores = [Corrector(self.nombres[0]),
                            Corrector(self.nombres[1]),
                            Corrector(self.nombres[2]),
                            Corrector(self.nombres[3]),
                            ]

    def tearDown(self):
        del self.nombres, self.correctores

    def test_revisar_nombre(self):
        # tiene formato malo
        self.assertFalse(self.correctores[1].revisar_nombre())

        pass

    def test_revisar_formato(self):
        self.assertFalse(self.correctores[1].revisar_formato("ttstt"))
        self.assertTrue(self.correctores[0].revisar_formato("txt"))

    def test_revisar_verificador(self):
        self.assertFalse(self.correctores[0].revisar_verificador("18642141-3"))
        self.assertTrue(self.correctores[0].revisar_verificador("18642141-8"))
        pass

    def test_revisar_orden(self):
        self.assertFalse(self.correctores[0].revisar_orden("valdes_andrea"))
        self.assertFalse(self.correctores[0].revisar_orden("lucas_hidalgo"))
        pass

    def test_descontar(self):
        pass

    def test_get_palabras(self):
        pass

    def test_get_descuento(self):
        pass



suite = unittest.TestLoader().loadTestsFromTestCase(TestearArchivo)
unittest.TextTestRunner().run(suite)
