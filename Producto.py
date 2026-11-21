class Producto: 
    def __init__(self,codigo,descripcion,precio,stock):
        self.codigo = codigo
        self.descripcion= descripcion
        self.precio = precio
        self.stock= stock    
    ##Muestra la informacion de producto.
    def __str__(self):
       return f"{self.codigo:<8} - {self.descripcion:<28} - {self.precio:>12,.0f} - {self.stock:>8}"
    
    ##Valida si tiene stock el producto.
    def tieneStock(self):
        return self.stock > 0 
            