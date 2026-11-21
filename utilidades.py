def mostrarMenu(listaMenu:list ,titulo:str = None, pregunta:str = "Elija una opcion:"):
    if titulo != None and titulo != "":
        mostrarTitulo(titulo)
    for i in range(len(listaMenu)):
        print(f"{i + 1} - {listaMenu[i]}")
    while True:
        opc = input(pregunta).strip()
        if opc.isdigit() and 1 <= int(opc) <= len(listaMenu):
            break
        else:
            print("Opcion incorrecta.")
    return opc
def mostrarTitulo(titulo):
    print()
    print("-"*len(titulo))
    print(titulo)
    print("-"*len(titulo))
    print()
def validar(precio,stock):
    if precio<= 0 or stock <= 0:
        print("Precio o stock Menor a 0. ")
        return False
    return True 
def recorrerModificacionProducto(codigos, productos, categorias, precios, stocks, texto):
    for i in range(len(codigos)):
        print(f"{codigos[i]} - {productos[i]} - {categorias[i]} - {precios[i]} - {stocks[i]}")
    return int(input(texto))

def recorrerGenerico(codigos,producto , texto):
    for i in range(len(codigos)):
        print(f"{codigos[i]} - {producto[i]}")
    return int(input(texto))


