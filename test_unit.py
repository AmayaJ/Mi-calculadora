import unittest
from calculadora import suma

class TestCalculadora(unittest.TestCase):

	def test_suma(self):
		#arrange
		valor1 = 2
		valor2 = 3
		resultadoEsperado = 5
		#act
		resultado = suma(valor1, valor2)
		self.assertEqual(resultado, resultadoEsperado)

	def test_suma2(self):
		#arrange
		valor1 = -5
		valor2 = 3
		resultadoEsperado = -2
		#act
		resultado = suma(valor1, valor2)
		self.assertEqual(resultado, resultadoEsperado)

if __name__ == "__main__":
	unittest.main()