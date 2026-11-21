from datetime import datetime
from ItemVenta import itemVenta
class Venta: 
    def __init__(self,cliente):
        self.cliente = cliente
        self.items = []


    def agreProListItems(self,producto,cantidad):
        ##Recorre la lista items y si encuentra el mismo producto lo retorna 
        for item in self.items:
            if item.producto.codigo == producto.codigo:
                return item.agregarCant(producto,cantidad)
        ## Valida si la cantidad es menor o = al stock del producto para agregarlo a la lista. 
        if cantidad > producto.stock:
            print("Stock insuficiente") 
            return False   
        nuevoItem= itemVenta(producto,cantidad)
        self.items.append(nuevoItem) 
        return True     


    def descontarStock(self):
        for item in self.items:
            item.producto.stock -= item.cantidad

    ##Muestra el total de la venta 
    def total(self):
        total = 0
        for item in self.items:
            total += item.subtotal()
        return total
    def mostrarTotal(self):
        print(f"TOTAL: {self.total():,.0f}")
    ##Muestra los items de los productos cargados hasta el momento. 
    def mostrar(self):
        for item in self.items:
            print(item)
        self.mostrarTotal()

        ##Imprime un ticket estilo kiosco/supermercado chino
    def mostrarTicket(self, numero):
        ancho = 40
        ahora = datetime.now()
        print("")
        print("=" * ancho)
        print("SUPERMERCADO XAOZE MDQ".center(ancho))
        print("Villa del Parque, Buenos Aires".center(ancho))
        print("CUIT: 20-59345593-1".center(ancho))
        print("-" * ancho)
        print(f"Fecha: {ahora:%d/%m/%Y}     Hora: {ahora:%H:%M}")
        print(f"Ticket N°: {numero:04d}")
        print(f"Cliente: {self.cliente.nombre}")
        print(f"DNI: {self.cliente.dni}")
        print("-" * ancho)
        for item in self.items:
            print(item.producto.descripcion[:ancho].upper())
            detalle = f"  {item.cantidad} x {item.precioUnidad:,.0f}"
            importe = f"${item.subtotal():,.0f}"
            print(detalle + importe.rjust(ancho - len(detalle)))
        print("-" * ancho)
        totalTxt = f"${self.total():,.0f}"
        print("TOTAL".ljust(ancho - len(totalTxt)) + totalTxt)
        print("=" * ancho)
        print("NO VALIDO COMO FACTURA".center(ancho))
        print("GRACIAS POR SU COMPRA".center(ancho))
        print("VUELVA PRONTOS!".center(ancho))
        print("=" * ancho)