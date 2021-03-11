#Presentado por: Luis Miguel Marulanda Torres#

#Incluir los modulos
import get_data
import print_data

#Cada registro será un objeto de la siguiente clase 
class registro: 
	paisprocedencia = None
	def __init__(self, ciudad, departamento, edad, tipo, estado, paisprocedencia = None):
		self.ciudad = str(ciudad)
		self.departamento = str(departamento)
		self.edad = int(edad) 
		self.tipo = str(tipo)
		self.estado = str(estado)
		self.paisprocedencia = str(paisprocedencia)

	def get_ciudad(self):
		return self.ciudad

	def get_departamento(self):
		return self.departamento 

	def get_edad(self):
		return self.edad

	def get_tipo(self):
		return self.tipo

	def get_estado(self):
		return self.estado

	def get_pais_procedencia(self):
		return self.paisprocedencia

class main(): 

	def __init__(self):
		#departamento, cantidad de registros y lista de registros obtenidos
		self.depto = 0
		self.cantidad = 0
		self.registros = []

	def run(self): 
	    print_data.printdeptos() #Mostrar los departamentos disponibles
	    
	    while True: 
	        #Verificar que el usuario ingrese enteros (no cadenas o espacio en blanco)
	        try: 
	            self.depto = int(input('Ingresa el codigo del departamento: ')) #Key del departamento escogido 
	            self.cantidad = int(input('Ingresa la cantidad de registros a obtener: ')) #Número de registros a visualizar
	        except: 
	            print("Debes ingresar numeros enteros !")

	        if self.depto >= 0 and self.depto < 32 and self.cantidad > 0 and self.cantidad < 1000: 
	            self.depto = str(self.depto) 
	            break
	        elif self.depto == 32: 
	            exit()
	        else: 
	            print("Revisa los valores ingresados")

	    #Obtener la lista de registros y el dataframe utilizando la API  
	    datalist, dataframe = get_data.func(print_data.deptos[self.depto], self.cantidad)

	    #Crear y almacenar cada objeto de la lista de registros como un registro
	    for i in datalist:
	    	if ('pa_s_de_procedencia' in i): 
	    		self.registros.append(registro(i['ciudad_de_ubicaci_n'],i['departamento'], i['edad'], 
	    			i['tipo'], i['estado'], i['pa_s_de_procedencia']))
	    	else:
	    		self.registros.append(registro(i['ciudad_de_ubicaci_n'],i['departamento'], i['edad'], 
	    			i['tipo'], i['estado']))

	    print_data.displaylist(self.registros)

	    #imprimir el dataframe con las columnas solicitadas
	    #print_data.displaydf(dataframe, None, cantidad)

if __name__ == "__main__":
    m = main()
    m.run() 