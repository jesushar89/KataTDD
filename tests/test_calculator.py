import unittest
from src.calculator import media, desviacion_estandar, NoSePuedeCalcular

class TestCalculator(unittest.TestCase):

    def test_media_lista_vacia(self):
        with self.assertRaises(NoSePuedeCalcular):
            media([])

    def test_media_un_elemento(self):
        self.assertEqual(media([10]), 10)

    def test_media_dos_elementos(self):
        self.assertEqual(media([10, 20]), 15)

    def test_media_varios_elementos_positivos(self):
        self.assertEqual(media([10, 20, 30]), 20)

    def test_media_varios_elementos_ceros(self):
        self.assertEqual(media([0, 0, 0]), 0)

    def test_media_elementos_no_numericos(self):
        with self.assertRaises(TypeError):
            media([10, "a", 30])

    def test_desviacion_estandar_lista_vacia(self):
        with self.assertRaises(NoSePuedeCalcular):
            desviacion_estandar([])

    def test_desviacion_estandar_un_elemento(self):
        self.assertEqual(desviacion_estandar([10]), 0)

    def test_desviacion_estandar_dos_elementos(self):
        self.assertAlmostEqual(desviacion_estandar([10, 20]), 5)

    def test_desviacion_estandar_varios_elementos(self):
        self.assertAlmostEqual(desviacion_estandar([10, 20, 30]), 8.16, places=2)

    def test_desviacion_estandar_no_numericos(self):
        with self.assertRaises(TypeError):
            desviacion_estandar([10, "a", 30])

if __name__ == '__main__':
    unittest.main()
