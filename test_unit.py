import unittest
from calculadora import suma, resta, multiplicacion, division, raiz_cuadrada

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

	def test_resta(self):
		#arrange
		valor1 = 2
		valor2 = 3
		resultadoEsperado = -1
		#act
		resultado = resta(valor1, valor2)
		self.assertEqual(resultado, resultadoEsperado)

	def test_resta2(self):
		#arrange
		valor1 = -5
		valor2 = 3
		resultadoEsperado = -8
		#act
		resultado = resta(valor1, valor2)
		self.assertEqual(resultado, resultadoEsperado)

	def test_multiplicacion(self):
		#arrange
		valor1 = 2
		valor2 = 3
		resultadoEsperado = 6
		#act
		resultado = multiplicacion(valor1, valor2)
		self.assertEqual(resultado, resultadoEsperado)

	def test_multiplicacion2(self):
		#arrange
		valor1 = -5
		valor2 = 3
		resultadoEsperado = -15
		#act
		resultado = multiplicacion(valor1, valor2)
		self.assertEqual(resultado, resultadoEsperado)

	def test_division(self):
		#arrange
		valor1 = -6
		valor2 = 3
		resultadoEsperado = -2
		#act
		resultado = division(valor1, valor2)
		self.assertEqual(resultado, resultadoEsperado)

	def test_division2(self):
		#arrange
		valor1 = 20
		valor2 = 3
		resultadoEsperado = 6.666667
		#act
		resultado = division(valor1, valor2)
		self.assertEqual("%.6f" % resultado, "%.6f" % resultadoEsperado)

	def test_raiz_cuadrada(self):
		#arrange
		valor1 = 81
		resultadoEsperado = 9
		#act
		resultado = raiz_cuadrada(valor1)
		self.assertEqual(resultado, resultadoEsperado)

	def test_raiz_cuadrada2(self):
		#arrange
		valor1 = 20
		resultadoEsperado = 4.4721359
		#act
		resultado = raiz_cuadrada(valor1)
		self.assertEqual("%.6f" % resultado, "%.6f" % resultadoEsperado)

if __name__ == "__main__":
	unittest.main()