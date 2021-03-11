
def menuPpal(): 
    print("\nMENU PRINCIPAL")
    print("1. Menu Clientes")
    print("2. Menu Facturas")
    print("3. Menu Productos")
    print("4. Menu Antibioticos")
    print("5. Salir")

    opc = int(input("Escoja una opción:\t"))

    if opc == 1: 
        return "Clientes"
    elif opc == 2: 
        return "Facturas"
    elif opc == 3: 
        return "Productos"
    elif opc == 4: 
        return "Antibioticos"
    elif opc == 5:
        return "Salir"

def menuDinamico(opc): 
    
    if opc == "Salir": return opc, 0
    print("\nMenu ", opc)
    print("1. Agregar", opc)
    print("2. Listar", opc)
    print("3. Modificar", opc)
    print("4. Eliminar", opc)

    caso = int(input("Escoja una opción:\t"))
    
    if caso == 1 and opc == "Clientes": 

        params = []
        nombre = str(input("Nombre del Cliente:\t"))
        cedula = str(input("Ingrese la cedula del cliente:\t"))
        params.append(nombre)
        params.append(cedula)
        return params, caso 

    elif caso == 2 and opc == "Clientes": return opc, caso
    elif caso == 3 and opc == "Clientes": return opc, caso
    elif caso == 4 and opc == "Clientes": return opc, caso
    
    elif caso == 1 and opc == "Facturas": 

        params = []
        Cedula = str(input("Ingrese la cedula del comprador: "))
        params.append(Cedula)
        return params, caso 

    elif caso == 2 and opc == "Facturas": return opc, caso
    elif caso == 3 and opc == "Facturas": return opc, caso 
    elif caso == 4 and opc == "Facturas": return opc, caso

    elif caso == 1 and opc == "Productos": 

        params = []
        print("1. Producto de control")
        print("2- Control Fertilizante")
        tipo = int(input("Tipo de producto: "))
        if (tipo == 1): 
            params.append("Control")
        elif(tipo == 2): 
            params.append("Fertilizante")
        ICA = input("Ingrese registro ICA: ")
        Nombre = input("Ingrese el nombre del producto: ")
        Frecuencia = input("Ingrese la frecuencia de aplicación: ")
        Valor = int(input("Ingrese el precio del producto: "))
        params.append(ICA)
        params.append(Nombre)
        params.append(Frecuencia)
        params.append(Valor)
        if tipo == 1: 
            Carencia = input("Ingrese el periodo de carencia: ")
            params.append(Carencia)
        elif tipo == 2: 
            Ultima = input("Ingrese la fecha de ultima aplicacion[dd/mm/aaaa]: ")
            params.append(Ultima)
        return params, caso

    elif caso == 2 and opc == "Productos": return opc, caso

    elif caso == 3 and opc == "Productos": return opc, caso
    elif caso == 4 and opc == "Productos": return opc, caso 

    elif caso == 1 and opc == "Antibioticos": 

        params = []
        Nombre = input("Ingrese el nombre del antibiotico: ")
        Dosis = input("Ingrese la dosis (cantidad): ")
        Valor = int(input("Ingrese el valor: "))
        params.append(Nombre)
        params.append(Dosis)
        print("1. Bovinos")
        print("2. Porcinos")
        Tipo = int(input("Escoja tipo de animal: "))
        if Tipo == 1: 
            params.append("Bovinos")
        elif Tipo == 2: 
            params.append("Porcinos")
        params.append(Valor)
        return params, caso 

    elif caso == 2 and opc == "Antibioticos": return opc, caso
    elif caso == 3 and opc == "Antibioticos": return opc, caso 
    elif caso == 4 and opc == "Antibioticos": return opc, caso 

def mostrarClientes(clientes): 
    for cliente in clientes: 
        print(cliente)

def mostrarFacturas(facturas): 
    print("FACTURAS: ")
    i = 1 
    for f in facturas:
        print("Factura Nro ", i) 
        print (f)
        i = i + 1 

def mostrarProductos(productos):
    i = 1
    for p in productos:
        print(i, " ", p)
        i = i + 1

def mostrarAntibioticos(antibioticos): 
    i = 1
    for a in antibioticos: 
        print(i, " ", a)
        i = i + 1

def error(): 
    print("Cliente no registrado")

def menuFactura(productos, antibioticos): 

    print("\nAgregue productos a la factura: ")
    print("1. Vender producto ")
    print("2. Vender antibiotico")
    print("0. No agregar más productos a la factura")
    item = int(input("Ingrese que va a vender: "))
    
    if item == 0: 
        return 0, 0
    elif item == 1: 
        mostrarProductos(productos)
        producto = int(input("Codigo producto: "))
        return item, producto
    elif item == 2: 
        mostrarAntibioticos(antibioticos)
        antibiotico = int(input("Codigo Antibiotico: "))
        return item, antibiotico
