def suma(arg1, arg2):
	return arg1 + arg2
	
def resta(arg1, arg2):
	return arg1 - arg2

def multiplicacion(arg1, arg2):
	return arg1 * arg2

def division(arg1, arg2):
	return arg1 / arg2

def raiz_cuadrada(arg1):
	cociente = arg1 / 2.0
	promedio = (2.0 + cociente) / 2.0

	while cociente != promedio:
		cociente = arg1 / promedio
		promedio = (promedio + cociente) / 2.0

	return promedio
