def cabecera_de_pantalla():
	str = """
	--------- ---------------- ---------------- --------------
	Bienvenido al Sistema de Gestion de Doctores del Hospital
	--------- ---------------- ---------------- --------------
	"""
	print(str)

def menu_principal() :
	str = """
	1. Buscar Medico por DNI (id)
	2. Buscar Hospital por nombre 
	"""
	print (str)
	opcion = input()
	return opcion

def lectura_dni() :
	str = """
	Ingresa el dni a buscar: """
	print (str)
	dni = int(input())
	return dni

def lectura_nombre() : 
	str="""
	Ingresa el nombre a buscar: """
	print(str)
	nombre = input()
	return nombre 

def mostrarresultado(results) : 
	str = """
	Resultados de su busqueda:
	"""
	print(str)
	print(results)

