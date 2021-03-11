from model.model import clientes, facturas, productos, antibioticos
from model.model import Cliente, Factura, ProductoControl, ControlFertilizante, Antibiotico

#Create

def validarCliente(cedula):

    for cliente in clientes: 
        if str(cliente.Cedula) == cedula: 
            return 1
        else: 
            return 0 

def getCliente(cedula): 
    for cliente in clientes: 
        if str(cliente.Cedula) == cedula: 
            return cliente

def crearFactura(productos, antibioticos, cliente):
    valor = 0
    for p in productos: 
        valor += p.Valor
    for a in antibioticos: 
        valor += a.Valor
    cliente.Facturas.append(Factura(valor, productos, antibioticos, cliente.Cedula))
    facturas.append(Factura(valor, productos, antibioticos, cliente.Cedula))

def crearCliente(nombre, cedula): 
    existente = 0
    for cliente in clientes: 
        if str(cliente.Cedula) == cedula: 
            existente = 1
    if existente == 0: 
        clientes.append(Cliente(nombre, str(cedula)))

def crearProducto(tipo, ICA, Nombre, Frecuencia, Valor, Data):
    if str(tipo) == "Control":
        productos.append(ProductoControl(ICA, Nombre, Frecuencia, Valor, Data))
    elif str(tipo) == "Fertilizante": 
        productos.append(ControlFertilizante(ICA, Nombre, Frecuencia, Valor, Data))

def getProducto(pos): 
    return productos[pos]

def crearAntibiotico(Nombre, Dosis, TipoAnimal, Valor):
    antibioticos.append(Antibiotico(Nombre, Dosis, TipoAnimal, Valor))

def getAntibiotico(pos): 
    return antibioticos[pos]

#Read 

def listaClientes():
    strings = []
    for cliente in clientes: 
        strings.append(cliente.__str__())
    return strings
    
def listaFacturas():
    strings = []
    for factura in facturas: 
        strings.append(factura.__str__())
    return strings

def listaProductos(): 
    strings = []
    for producto in productos: 
        strings.append(producto.__str__())
    return strings
    
def listaAntibioticos(): 
    strings = []
    for antibiotico in antibioticos: 
        strings.append(antibiotico.__str__())
    return strings
