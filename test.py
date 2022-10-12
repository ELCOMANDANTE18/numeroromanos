import unittest

from main import convertir_decimal_a_romano

class TestDecimalaromano(unittest.TestCase):
    def test_1(self):
        numero_romano = convertir_decimal_a_romano(1)
        self.assertEqual(numero_romano,'I')

    def test_2(self):
        numero_romano = convertir_decimal_a_romano(2)
        self.assertEqual(numero_romano,'II')

    def test_10(self):
        numero_romano = convertir_decimal_a_romano(10)
        self.assertEqual(numero_romano,'X')

if __name__ == '__main__':
    unittest.main()                