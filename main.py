from Producto import Producto
from Cliente  import Cliente
from Venta import Venta

productos= [
Producto(101, "Notebook Lenovo IdeaPad", 990000, 5),
Producto(102, "Notebook HP 15",	1100000	,3),
Producto(103, "Monitor Samsung 24", 190000,0), ## Producto sin stock 
Producto(104, "Monitor LG 27",240000,2),
Producto(105, "Mouse Logitech M170", 18000,20),
Producto(106, "Mouse Gamer Redragon", 35000	,0), ## Producto sin stock 
Producto(107, "Teclado Logitech K120", 20000,12)]

ventas= []
lista = ["Nueva venta", "Lista de ventas realizadas", "Mostrar Total vendido", "Salir"]

def mostrarLista(productos):
    print("")
    print("="*15,"PRODUCTOS DISPONIBLES","="*15)
    for p in productos:
        if p.tieneStock(): ## Aca utilizamos la funcion de producto si tiene stock para mostrar los productos solo con stock 
            print(p) 

def buscarCodigo(codigo):
    for p in productos: 
        if str(p.codigo) == str(codigo): ##Busca el codigo y si lo encuentra en la lista lo retorna 
            return p 

def main():
    print("="*15,"SISTEMA DE VENTAS DE XAOZE MDQ","="*15)  ##El menu de siempre
    while True: 
        for i in range(len(lista)):
            print(i + 1, " - ",lista[i])
        print("")
        opc = input("Ingrese una opcion: ")
        if opc == "1":
            nuevaVenta()
        elif opc == "2":
            listaVentas()
        elif opc == "3":
            mostrarTotalVendido()
        elif opc == "4":
            print("")
            print("Programa finalizado vuelva pronto!. ")
            print("="*40)
            break
        else: 
            print("")
            print("Opcion invalida.")
            print("="*40)
            continue

def nuevaVenta():
    print("=" * 15, "NUEVA VENTA", "=" * 15)
    dni = input("DNI: ")
    nombre = input("Nombre: ")

    ##declara que un cliente contiene DNI y nombre 
    try:
        unCliente = Cliente(dni, nombre)
    except ValueError as e:
        print(e)
        return
    ##Una venta contiene Uncliente
    unaVenta = Venta(unCliente)
    while True: 
        ##Muestra productos con la funcion mostrarlista 
        mostrarLista(productos)
        ##Validaciones 
        try:
            print("")
            codigo =int(input("Ingrese el codigo del producto:"))
        except ValueError:
            print("")
            print("El codigo debe ser numerico, vuelva a ingresarlo.")
            continue
        ##Mas validaciones 
        prod= buscarCodigo(codigo)       
        if (prod == None):
            print("")
            print("Producto inexistente.")
            continue
        if not prod.tieneStock():
            print("")
            print("Producto sin stock.")
            continue
        try:
            print("")
            cant =int(input("Ingrese la cantidad(0 para cancelar): "))
        except ValueError:
            print("")
            print("La cantidad debe ser numerica.")
            continue
        if cant < 0:
            print("")
            print("La cantidad no puede ser negativa.")
            continue
        elif cant == 0:
            print("")
            print("Producto no agregado")
        else: 
            unaVenta.agreProListItems(prod, cant)

        unaVenta.mostrar()
        confirmar = input("¿Confirmar venta? (s/n) o (c) para continuar cargando productos: ").lower()
        if confirmar == "s":
            if not unaVenta.items:
                print("\nNo hay productos cargados.")
                continue
            unaVenta.descontarStock()
            ventas.append(unaVenta)  
            print("\nVenta registrada.")
            unaVenta.mostrarTicket(len(ventas))
            return
        elif confirmar == "c":
            continue
        else:
            print("\nVenta cancelada.")
            return   
def listaVentas():
    ancho= 40
    print("=" * ancho) 
    print("VENTAS REALIZADAS".center(ancho))
    print("=" * ancho)
    ##Si en la lista ventas valida que hay nada muestra mensaje de ninguna venta.
    if len(ventas) == 0:
        print("")
        print("No hay ventas registradas.")
        print("=" * 15)
        return
    ##Si hay ventas las recorre y las muestra con su respectivo cliente 
    for i in range(len(ventas)):
        print(f"VENTA N° {i + 1}")
        print(f"Cliente: {ventas[i].cliente.nombre}")
        print(f"DNI: {ventas[i].cliente.dni}")
        print("-" * ancho)
        for item in ventas[i].items:
            detalle = f"  {item.cantidad} x {item.producto.descripcion}"
            importe = f"${item.subtotal():,.0f}"
            print(detalle[:ancho - len(importe) - 1].ljust(ancho - len(importe)) + importe)
        print("-" * ancho)
        totalTxt = f"${ventas[i].total():,.0f}"
        print("TOTAL".ljust(ancho - len(totalTxt)) + totalTxt)
        print("=" * ancho)
def mostrarTotalVendido():
    ancho = 40
    print("")
    print("=" * ancho)
    print("TOTAL VENDIDO".center(ancho))
    print("=" * ancho)

    if len(ventas) == 0:
        print("No hay ventas registradas.".center(ancho))
        print("=" * ancho)
        return

    ##Recorre ventas, muestra el importe de cada una y acumula el total
    totalVendido = 0
    for i in range(len(ventas)):
        importe = f"${ventas[i].total():,.0f}"
        detalle = f"Venta {i + 1} - {ventas[i].cliente.nombre}"
        print(detalle[:ancho - len(importe) - 1].ljust(ancho - len(importe)) + importe)
        totalVendido += ventas[i].total()
    print("-" * ancho)
    totalTxt = f"${totalVendido:,.0f}"
    print("TOTAL".ljust(ancho - len(totalTxt)) + totalTxt)
    print("=" * ancho)



























                        




main()