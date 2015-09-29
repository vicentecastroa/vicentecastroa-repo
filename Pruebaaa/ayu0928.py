__author__ = 'Vicente'

import unittest

def random_ip():
    import random
    return ".".join([str(random.randint(0, 255)) for _ in " "*4])


class RandomTester(unittest.TestCase):

    def test_random_ip(self):
        rip = random_ip()
        valores = rip.split(".")

        self.assertEqual(len(valores), 4)

        for elemento in valores:
            self.assertTrue(elemento.isdecimal())
            self.assertTrue(0 <= int(elemento) <= 255)


suite = unittest.TestLoader().loadTestsFromTestCase(RandomTester)
unittest.TextTestRunner().run(suite)