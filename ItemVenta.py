from Producto import Producto

class itemVenta: 
    def __init__(self,producto,cantidad):
        self.producto = producto
        self.cantidad = cantidad
        self.precioUnidad = producto.precio

    ##Funcion para agregar cantidad a producto    
    def agregarCant(self,producto:Producto,cantidad):
        unaCant = cantidad
        ##Validacion menor a 0 
        try: 
            if unaCant < 0:
                raise ValueError("El numero tiene que ser valido.")
        except ValueError as e:
            print("")
            print(e)
            print("="*40)
            return False
        ##Valida si la cantidad sobrepasa al stock del producto. 
        try:
            if self.cantidad + unaCant > self.producto.stock:
                raise ValueError("Stock insuficiente, Coloque una cantidad acorde.")
        except ValueError as e:
            print("")
            print(e)
            print("="*40)
            return False
        cantidadTotal = self.cantidad + unaCant

        self.producto = producto
        self.cantidad = cantidadTotal
        self.precioUnidad= self.producto.precio   
        return True
    def subtotal(self):
        return self.cantidad * self.precioUnidad
    def __str__(self):
       return f"{self.producto.descripcion} - Cant: {self.cantidad} - Precio: {self.precioUnidad:,.0f} - SubTotal: {self.subtotal():,.0f}"
    