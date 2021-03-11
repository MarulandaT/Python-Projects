from ui import mensajes
from crud import ImpCrud

mensajes.cabecera_de_pantalla()
opcion = mensajes.menu_principal()
crud = ImpCrud.Crud() 

if opcion == '1': # Buscar doctor 
	dni = mensajes.lectura_dni() 
	doctor = crud.buscar_doctor(dni)
	mensajes.mostrarresultado(doctor)

elif opcion == '2': 
	nombre = mensajes.lectura_nombre()
	hospi = crud.buscar_hospital(nombre)
	mensajes.mostrarresultado(hospi)