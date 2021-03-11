from datetime import datetime

clientes = []
facturas = []
productos = []
antibioticos = []

class Cliente: 
    
    def __init__(self, Nombre, Cedula):
        self.Facturas = []
        self.Nombre = Nombre
        self.Cedula = Cedula 
    def __str__(self): 
        return "Nombre: " + self.Nombre + " Cedula: " + self.Cedula

class Factura: 
   
    def __init__(self, Valor, productos, antibioticos, cliente):
        self.Productos = []
        self.Antibioticos = []
        self.Fecha = datetime.now()
        self.Valor = Valor
        self.Cliente = cliente
        for p in productos: 
            self.Productos.append(p)
        for a in antibioticos: 
            self.Antibioticos.append(a)
    def __str__(self): 
        stringpr = ""
        stringan = ""
        for producto in self.Productos: 
            stringpr += "\t\n " + producto.__str__()
        for antibiotico in self.Antibioticos: 
            stringan += "\t\n " + antibiotico.__str__()
       
        return ("Fecha: " + str(self.Fecha) + "\n"
        "Cedula Cliente: " + str(self.Cliente) + "\n"
        "Valor Total: " + str(self.Valor) + "\n"
        "Productos: " + stringpr + "\n"
        "Antibioticos: " + stringan)

class Producto:
    def __init__(self, RegistroICA, Nombre, Frecuencia, Valor): 
        self.RegistroICA = RegistroICA
        self.Nombre = Nombre 
        self.Frecuencia = Frecuencia 
        self.Valor = Valor
    def __str__(self): 
        return "ICA: " + self.RegistroICA + " Nombre: " + self.Nombre + " Frecuencia: " + self.Frecuencia + " Valor: " + str(self.Valor)

class ProductoControl(Producto):
    def __init__(self, RegistroICA, Nombre, Frecuencia, Valor, PeriodoCarencia):
        Producto.__init__(self, RegistroICA, Nombre, Frecuencia, Valor)
        self.PeriodoCarencia =  PeriodoCarencia
    
class ControlFertilizante(Producto): 
    def __init__(self, RegistroICA, Nombre, Frecuencia, Valor, Fecha_Ultima_Aplicacion):
        Producto.__init__(self, RegistroICA, Nombre, Frecuencia, Valor)
        self.Fecha_Ultima_Aplicacion = Fecha_Ultima_Aplicacion

class Antibiotico: 
    def __init__(self, Nombre, Dosis, Tipo_Animal, Valor): 
        self.Nombre = Nombre 
        self.Dosis = Dosis
        self.Tipo_Animal = Tipo_Animal
        self.Valor = Valor 
    def __str__(self): 
        return "Nombre: " + self.Nombre + " Dosis: " + str(self.Dosis) + " Tipo_Animal: " + str(self.Tipo_Animal) + " Valor: " + str(self.Valor)
