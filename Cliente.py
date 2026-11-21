class Cliente:
    def __init__(self,dni,nombre):
        ##Valida si DNI es digito y si es menor a 0 
        if str(dni).strip().isdigit() and int(dni) > 0:
            self.dni = dni 
        else: 
            raise ValueError("El dni no puede ser nulo, debe ser numerico o mayor a 0")

        ##Valida vacio"" y si nombre es digito tira valueError
        if str(nombre).strip() == "":
            raise ValueError("El nombre no puede ser nulo")
        if str(nombre).isdigit():
            raise ValueError("El nombre no puede ser un numero.") 
        self.dni= dni 
        self.nombre= nombre
    ##Muestra DNI y nombre 
    def __str__(self):
        return f"DNI:{self.dni} -  Nombre:{self.nombre}"