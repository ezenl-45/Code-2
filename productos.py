import utilidades 
categorias = [
    "Computadoras",
    "Monitores",
    "Perifericos",
    "Componentes",
    "Almacenamiento",
    "Redes",
    "Accesorios"
]

codigos = [
    101, 102, 103, 104, 105, 106,
    107, 108, 109, 110, 111, 112,
    113, 114, 115, 116, 117, 118
]

productos = [
    "Notebook Lenovo IdeaPad",
    "Notebook HP 15",
    'Monitor Samsung 24"',
    'Monitor LG 27"',
    "Mouse Logitech M170",
    "Mouse Gamer Redragon",
    "Teclado Logitech K120",
    "Teclado Mecánico Redragon",
    "Memoria RAM Kingston 16 GB",
    "Placa de video RTX 4060",
    "SSD Kingston 480 GB",
    "SSD Kingston 1 TB",
    "Disco Externo WD 2 TB",
    "Router TP-Link AX10",
    "Switch TP-Link 8 puertos",
    "Webcam Logitech C270",
    "Auriculares HyperX Cloud",
    "Pad Mouse Gamer XL"
]

precios = [
    850000, 920000, 220000, 310000, 35000, 48000,
    42000, 78000, 95000, 680000, 55000, 95000,
    145000, 78000, 52000, 80000, 120000, 25000
]

stocks = [
    5, 3, 8, 2, 20, 4,
    12, 1, 7, 0, 15, 6,
    3, 9, 5, 0, 11, 18
]

categorias_producto = [
    "Computadoras",
    "Computadoras",
    "Monitores",
    "Monitores",
    "Perifericos",
    "Perifericos",
    "Perifericos",
    "Perifericos",
    "Componentes",
    "Componentes",
    "Almacenamiento",
    "Almacenamiento",
    "Almacenamiento",
    "Redes",
    "Redes",
    "Accesorios",
    "Accesorios",
    "Accesorios"
]
def menu():
    while True:
        print ("")
        for i in range(len(categorias)):
            categorias[i] = categorias[i].lower()
        utilidades.mostrarTitulo(titulo="Bievenido a WOLX ")
        opc = utilidades.mostrarMenu(["Alta de producto","Modificación de producto","Baja de producto","Consulta de producto",
        "Lista de precios", "Productos por categoría", "Productos con bajo stock","Salir"])
        if opc == "1":
            altaProducto()
        elif opc == "2":
            modificacionProducto()
        elif opc == "3":
            bajaProducto()
        elif opc == "4":
            consultaProducto()
        elif opc == "5":
            listaPrecios()
        elif opc == "6":
            productosPorCategoria()
        elif opc == "7":
            productosBajoStock()
        elif opc == "8":
            print("Gracias por elegirnos!Vuelva pronto.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
def altaProducto():
    utilidades.mostrarTitulo(titulo="Alta Producto.")
    guardar=int(input("Ingrese un codigo: "))
    if not guardar in codigos:
        newProd=input("Nombre del producto: ")
        newPrec=float(input("Precio: "))
        newStock=int(input("Stock disponible: "))
        newCate=input("Que categoria es su producto?: ").lower()
        if utilidades.validar(newPrec,newStock) and newCate in categorias:
            codigos.append(guardar)
            productos.append(newProd)
            precios.append(newPrec)
            stocks.append(newStock)
            categorias_producto.append(newCate)

            print("")
            print("Se ingreso completamente el producto.")
        else: 
            print("Esa categoria no existe.")
    else:  
        print("")
        print("Codigo de producto ya existente. Vuelva a intentarlo")
        print("")
def modificacionProducto():
    utilidades.mostrarTitulo(titulo="Modificar Producto.")
    codExiste= utilidades.recorrerModificacionProducto(codigos,productos,precios,stocks,categorias_producto,texto="Coloque el codigo del producto que desea modificar: ")
    if codExiste in codigos:
        posicion = codigos.index(codExiste)
        print(f"\nProducto: {codigos[posicion]} - {productos[posicion]} - "
              f"{categorias_producto[posicion]} - {precios[posicion]} - {stocks[posicion]}")
     
        

        while True:
            print("-"*30)
            print("Que desea modificar?")
            opcion =utilidades.mostrarMenu(["Nombre del producto","Categoria","Precio", "Stock", "Salir"])
            if opcion == "1":
                nuevoNombre = input("Nombre: ")
                productos[posicion] = nuevoNombre
                print("Nombre modificado correctamente.")
                print("="*10)
            
            elif opcion == "2":
                nuevaCategoria = input("Categoría: ").lower()
                if nuevaCategoria in categorias:
                    categorias_producto[posicion] = nuevaCategoria
                    print("Categoria modificada correctamente.")
                

                else:
                    print("Categoria inexistente.")

                print("="*10)

            elif opcion == "3":
                nuevoPrecio = float(input("Precio: "))
                if utilidades.validar(nuevoPrecio, stocks[posicion]):
                    precios[posicion] = nuevoPrecio
                    print("Precio modificado correctamente.")
                    print("="*10)
                else: 
                    print("")
                    print("Precio no modificado.")
                print("="*10)
            elif opcion == "4":
                nuevoStock = int(input("Stock: "))
                if utilidades.validar(precios[posicion], nuevoStock):
                    stocks[posicion] = nuevoStock
                    print("Stock modificado correctamente.")
                    print("="*10)
                else: 
                     print("")
                     print("Stock no modificado.")
                    
                print("="*10)
            
            elif opcion == "5":
                print("")
                print("Modificación cancelada.")
                print("="*10)
                break
            
            else:
                print("")
                print("Opcion incorrecta.")
                print("="*10)
    else:
        print("")
        print("No existe el producto.")
        print("="*10)
def bajaProducto():
    utilidades.mostrarTitulo(titulo="Baja Producto.")
    while True:
        for i in range (len(codigos)):
            print(f"{codigos[i]} - {productos[i]}")

        baja=utilidades.recorrerGenerico(codigos,productos,texto="Ingrese el codigo del producto que desea eliminar: ")
        if baja in codigos:
                indice = codigos.index(baja)
                print(f"\nProducto elegido: {codigos[indice]} - {productos[indice]} - "
                f"{categorias_producto[indice]} - {precios[indice]} - {stocks[indice]}")

                codigos.pop(indice)
                productos.pop(indice)
                categorias_producto.pop(indice)
                precios.pop(indice)
                stocks.pop(indice)
                print("")
                print("Producto eliminado correctamente.")
                print("="*10)
                break
        else: 
                print("")
                print("Codigo inexistente. Ingrese uno valido")
                print("="*10)
def consultaProducto():
    utilidades.mostrarTitulo(titulo="Consulta Producto.")
    consulta= utilidades.recorrerGenerico(codigos,productos,texto="Ingrese el codigo que desea consultar:")
    if consulta in codigos:
        consultaElegida= codigos.index(consulta)
        print(f"\nProducto consultado: {codigos[consultaElegida]} - {productos[consultaElegida]} - "
                f"{categorias_producto[consultaElegida]} - {precios[consultaElegida]} - {stocks[consultaElegida]}")
        
    else: 
          print("Ese producto no existe.")
          print("="*10)
def listaPrecios():
    utilidades.mostrarTitulo(titulo="Listas Producto.")
    print("| Codigo:", " "* 5,"| Producto: ", " "* 5,"| Categoria: ", " "* 5,"| Precio: ", " "* 5, "|  Stocks: ")
    for i in range(len(codigos)):
        print(f"{codigos[i]} - {productos[i]} - "f"{categorias_producto[i]} - {precios[i]} - {stocks[i]}")
    
    
    input("Continue con enter")
def productosPorCategoria():
    utilidades.mostrarTitulo(titulo="Productos por categoria")

    for c in categorias:
        print(f"- {c}")

    categoriaElegida = input("Ingrese la categoria que desea ver: ")
    print("")
    encontrado = False
    for i in range(len(categorias_producto)):
        if categorias_producto[i].lower() == categoriaElegida.lower():
            print(f"Código: {codigos[i]} | Producto: {productos[i]} | Precio: ${precios[i]} | Stock: {stocks[i]} | Categoria: {categorias_producto[i]}")
            encontrado = True

    if not encontrado:
        print("")
        print("No se encontraron productos en esa categoría.")
        print("="*10) 
def productosBajoStock():
    utilidades.mostrarTitulo(titulo="Productos Bajo Stock.")
    bajo = 5
    stockBajo= []
    for i in range(len(stocks)):
        if int(stocks[i]) <= bajo:
            stockBajo.append(productos[i])
    
    print("Los productos bajo stock son: ")
    if stockBajo:
        for i in stockBajo:
            print(i)
    else:
        print("No hay productos bajo stock.")
        

    print("="*10)
def principal():
    try:
        menu()
    except(ValueError):
        print("No se puede ingresar letras o vacio, Solo numeros.")
    except(ZeroDivisionError):
        print("Error de division por 0")
    except(TypeError):
        print("Error, Reinicie el programa.")
    except(IndexError):
        print("Error, Listas fuera de rango")
    except(KeyboardInterrupt):
        print("Error 666")

principal()
















