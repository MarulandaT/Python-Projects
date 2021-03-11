from crud.crud import validarCliente, getCliente, getProducto, getAntibiotico
from crud.crud import crearFactura, crearCliente, crearProducto, crearAntibiotico
from crud.crud import listaClientes, listaAntibioticos, listaFacturas, listaProductos
from UI.ui import menuPpal, menuDinamico, error, menuFactura
from UI.ui import mostrarClientes, mostrarFacturas, mostrarProductos, mostrarAntibioticos

if __name__ == "__main__":
    
    while True: 
        params, caso = menuDinamico(menuPpal())
        if params == "Salir": 
            break 
        else: 
            if caso == 1: 
                if len(params) == 1: 
                    transaction = validarCliente(params[0]) 
                    if transaction == 1:
                        productos = []
                        antibioticos = []
                        while True: 
                            item, pos_item = menuFactura(listaProductos(), listaAntibioticos())
                            if item == 0: 
                                break 
                            elif item == 1: 
                                productos.append(getProducto(pos_item-1))
                            elif item == 2: 
                                antibioticos.append(getAntibiotico(pos_item-1))
                        crearFactura(productos, antibioticos, getCliente(params[0]))
                    else: 
                        error()
                elif len(params) == 2:
                    crearCliente(params[0], params[1])
                elif len(params) == 4: 
                    crearAntibiotico(params[0], params[1], params[2], params[3])
                elif len(params) == 6: 
                    crearProducto(params[0], params[1], params[2], params[3], params[4], params[5])
            elif caso == 2: 
                if params == "Clientes": mostrarClientes(listaClientes())
                elif params == "Facturas": mostrarFacturas(listaFacturas())
                elif params == "Productos": mostrarProductos(listaProductos())
                elif params == "Antibioticos": mostrarAntibioticos(listaAntibioticos())

