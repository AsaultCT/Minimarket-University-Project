from colorama import Fore



def validacion_identificacion() -> int:

    identificacion:int =-1
    
    while (len(str(identificacion)) > 10 or identificacion < 0 ):
        try:

            identificacion=int(input(Fore.BLUE + "Ingrese su identificación esta debe ser menor o igual a 10 digitos "))


            if (len(str(identificacion)) > 10):
                print(Fore.RED + "La identificación puede tener una longitud máxima de 10 dígitos, intentelo de nuevo")


            if (identificacion < 0):
                 print(Fore.RED + "La identificación debe de ser positiva, intentelo de nuevo")


        except ValueError:
            print(Fore.RED + "Usted ingresó un carácter inválido, intentelo de nuevo")

    print(Fore.GREEN + "La identificación ha sido guardada correctamente")
    return identificacion





def validacion_contrasena()->str:
    contrasena:str = ""
    
    while ( (len(contrasena) <8 or len(contrasena)> 15) or (" " in contrasena) ):
        
            contrasena=input(Fore.BLUE + "Ingrese su contraseña, esta debe tener mínimo 8 carácteres y máximo 15 carácteres, además la contraseña no puede tener un espacio: ")
            if ( len(contrasena) < 8 ):
                print(Fore.RED + "La contraseña debe tener una longitud mínima de 8 carácteres, intentelo de nuevo")
            elif (len(contrasena) > 15):
                print(Fore.RED + "La contraseña puede tener una longitud máxima de 15 carácteres, intentelo de nuevo")
                
            if (" " in contrasena):
                print(Fore.RED + ("La contraseña no puede tener espacios, intentelo de nuevo"))
    print(Fore.GREEN + "\nContraseña guardada\n")
    return contrasena





def validacion_nombre()->str:
    nombre:str=""

    nombre= input(Fore.BLUE + "Ingrese el nombre: ")         
    print(Fore.GREEN + "El nombre se ha guardado correctamente")
    return nombre






def validacion_telefono()->int:
    telefono:int =-1
    
    while (telefono < 0):
        try:
            telefono=int(input(Fore.BLUE + "Ingrese el numero de telefono:"))
            if (telefono < 0):
                print(Fore.RED + "Usted ingreso un numero negativo, ingreselo de nuevo")
            telefono = str(telefono)
            if( len(telefono)>10 or len(telefono)<10):   #Valida que el telefono tenga una longitud exacta de 10 caracteres
                print(Fore.RED + "El numero debe tener exactamente 10 digitos, ingreselo de nuevo")
                telefono=-1
            telefono=int(telefono)
                
        except ValueError:
            print(Fore.RED + "Usted no ingreso un numero, intentelo de nuevo")
            telefono = -1
    print(Fore.GREEN + "El telefono se ha guardado correctamente")
    return telefono




    
def validacion_correo() -> str:
    correo:str=""

    correo=input(Fore.BLUE + "Ingrese el correo electronico:")
    while not ("@" in correo and (".com" in correo or ".co" in correo)): #Esta validacion se encarga de que en el correo aparezca un '@' y un '.co' o '.com'
        correo=input(Fore.RED + "El correo ingresado no es un correo valido, ingreselo de nuevo")

    print(Fore.GREEN + "El correo se ha guardado correctamente")
    
    return correo






def validacion_direccion()->str:
    direccion:str="" 
    direccion=input(Fore.BLUE + "Ingrese la direccion :")
    print(Fore.GREEN + "La direccion se ha guardado correctamente")
    return direccion





def validacion_tipo_identificacion() -> str:
    tipo_identificacion:str=""
    
    while (tipo_identificacion != "cc" and tipo_identificacion != "ti"):
            tipo_identificacion=input(Fore.BLUE + "Ingrese el tipo de documento de identidad, ingrese 'cc' para cedula o 'ti' para tarjeta de identidad: ").lower().strip()
            if (tipo_identificacion != "cc" and tipo_identificacion != "ti"):
                print(Fore.RED + "El tipo de identificación ingresado es inválido, intentelo de nuevo")
    print(Fore.GREEN + "Tipo de identificación guardado")
    return tipo_identificacion






def asignacion_codigo(productos_registrados)->int:
    codigo:int
    codigo=productos_registrados+1
    print(Fore.WHITE + f"El codigo que fue asignado automaticamente es : {codigo}")
    return codigo





def asignacion_identificador(ventas_registradas:int)->int:
    identificador:int
    identificador=ventas_registradas + 1
    print(Fore.WHITE + f"El identificador fue asignado automaticamente es : {identificador}")
    return identificador





def validacion_categoria()->str:
    categoria:str=""
    categoria = input(Fore.BLUE + "Categoria del producto: ")
        
    print(Fore.GREEN + "\nLa categoría del producto ha sido guardada\n")
    return categoria





def validacion_costo_adquisicion()->float:
    costo_adquisicion:float=0
    while (costo_adquisicion <= 0):
        try:
            costo_adquisicion=float(input(Fore.BLUE + "Ingrese el costo de adquisición del producto, este debe ser un número mayor a cero estrictamente: "))
            if (costo_adquisicion <= 0):
                print(Fore.RED + "El costo de adquisición del producto debe ser mayor a cero estrictamente, intentelo de nuevo")
            
        except ValueError:
            print(Fore.RED + "Usted no ingresó un número válido, intentelo de nuevo")
    print(Fore.GREEN + "\nEl costo de adquisicion del producto ha sido guardado\n")
    return costo_adquisicion






def validacion_precio_sin_iva(costo_adquisicion)->float:
    precio_sin_iva:float=0
    while (precio_sin_iva <= 0 or (precio_sin_iva < costo_adquisicion)):
        try:
            precio_sin_iva = float(input(Fore.BLUE + "Precio (sin IVA) del producto: "))
            if (precio_sin_iva <= 0):
                print(Fore.RED + "El precio sin IVA tiene que ser positivo, intentelo de nuevo")
            if (precio_sin_iva < costo_adquisicion):
                print(Fore.RED + "El precio sin IVA no puede ser menor al costo de adquisión, intentelo de nuevo")
        except ValueError:
            print(Fore.RED + "Usted no ingresó un número válido, intentelo de nuevo")
    print(Fore.GREEN + "\nEl precio sin iva del producto ha sido guardado\n")
    return precio_sin_iva






def validacion_porcentaje_iva()->float:
    porcentaje_iva:float=-1
    while (porcentaje_iva < 0 or porcentaje_iva >100):
        try:
            porcentaje_iva=float(input(Fore.BLUE + "Ingrese el porcentaje de IVA del producto, este debe ser un número entre 0 y 100: "))
            if (porcentaje_iva < 0):
                print(Fore.RED + "No se admiten porcentajes negativos, intentelo de nuevo")
            if(porcentaje_iva >100):
                print(Fore.RED + "El porcentaje de IVA no puede ser mayor a 100, intentelo de nuevo")
            
        except ValueError:
            print(Fore.RED + "Porcentaje inválido, intente de nuevo")
    print(Fore.GREEN + "\nEl porcentaje de iva del producto ha sido guardado\n")
    return porcentaje_iva






            
            
def validacion_stock() -> int:
    stock:int  = -1
    while (stock < 0):
            try:
                stock = int(input(Fore.BLUE + "Ingrese el stock del producto, este debe ser un número entero mayor o igual a cero: "))
                if (stock < 0):
                    print(Fore.RED + "Usted ingresó un stock inválido, intentelo de nuevo")
            except ValueError:
                print(Fore.RED + "Usted no ingreso un número válido, intentelo de nuevo")
    print(Fore.GREEN + "\nEl stock del producto ha sido guardado\n")

    return stock






def validacion_cantidad() -> int:

    cantidad:int  = -1
    while (cantidad <= 0):
            try:
                cantidad = int(input(Fore.BLUE + "Ingrese la cantidad del producto, este debe ser un número entero mayor a cero: "))
                if (cantidad <= 0):
                    print(Fore.RED + "Usted ingresó una cantidad inválida, intentelo de nuevo")
            except ValueError:
                print(Fore.RED + "Usted no ingreso un número válido, intentelo de nuevo")
    return cantidad






def validacion_stock_min() -> int:
    stock_min:int = -1
    while (stock_min < 0):
        try:
            stock_min = int(input(Fore.BLUE + "Ingrese el stock mínimo del producto, este debe ser un número entero no negativo: "))
            if (stock_min < 0):
                print(Fore.RED + "Usted ingresó un stock mínimmo inválido, intentelo de nuevo")
        except ValueError:
            print(Fore.RED + "Usted no ingresó un número válido, intentelo de nuevo:")
    print(Fore.GREEN + "\nEl stock minimo del producto ha sido guardado\n")
    return stock_min







def validacion_opcion_1() -> int:
    opcion1:int=0
    while (opcion1 <1 or opcion1 > 3):         #Este apartado muestra las opciones iniciales del programa, luego pregunta por una eleccion, que es un numero entero de 1 a 3 y la valida
            try:
                opcion1=int(input(Fore.BLUE + "1. Iniciar sesión\n2. Registrarse\n3. Para salir del programa\n: "))
                if (opcion1 <1 or opcion1>3):
                     print(Fore.RED + "Opción inválida, intentelo de nuevo: ")
            except ValueError:
                 print(Fore.RED + "Opción inválida, intentelo de nuevo: ")
    if opcion1==3:
        print(Fore.WHITE + "Saliendo del programa... Vuelva pronto")
    else:
        print(Fore.GREEN + f"\n opción {opcion1} válida \n")
    return opcion1






def validacion_opcion_venta2() -> bool:
    opcion_venta:int=0
    while (opcion_venta <1 or opcion_venta > 2):         #Este apartado permite al usuario elegir si la venta es a credito  o no y valida el dato ingresado
            try:
                opcion_venta=int(input(Fore.BLUE + "1. Venta a credito\n2. Venta de contado \n : "))
                if (opcion_venta <1 or opcion_venta>2):
                     print(Fore.RED + "Opción inválida, intentelo de nuevo: ")
            except ValueError:
                 print(Fore.RED + "Opción inválida, intentelo de nuevo: ")
    if(opcion_venta == 1):
        return True
    else:
        return False

def validacion_abono() -> float:
    abono:float = 0
    
    while(abono <= 0):
        try:
            abono = float(input("Ingrese el monto del abono a registrar: "))
            if abono <= 0:
                print(Fore.RED + "El abono debe ser un número positivo, intentelo de nuevo")
        except ValueError:
            print(Fore.RED + "Ingrese un dato valido")
    return abono


def validacion_tipo_usuario() -> int:
    tipo_usuario:int=0
    while (tipo_usuario <1 or tipo_usuario >3):
        if (tipo_usuario <1 or tipo_usuario >3):
            try:
                tipo_usuario=int(input(Fore.BLUE + "¿Qué tipo de usuario se va a autenticar? \n 1. Administrador \n 2. Cajero \n 3. Cliente\n: "))
                if (tipo_usuario <1 or tipo_usuario >3):
                    print(Fore.RED + "Opción inválida, intentelo de nuevo")
                        
            except ValueError:
                print(Fore.RED + "Opción inválida, intentelo de nuevo: ")
                    
    print(Fore.GREEN+ f"El tipo de usuario {tipo_usuario} ha sido guardado exitosamente")
    return tipo_usuario 






#__________________Validación del código de un producto______________________________

def validacion_codigo(productos_registrados)->int:
    if productos_registrados == 0:
        print(Fore.RED + "No hay productos registrados")
        return -1
    codigo:int=0
    while (codigo <1 or codigo>productos_registrados):
        try:

            codigo=int(input(Fore.BLUE + "Ingrese el código de el producto, este debe ser un número entero positivo:"))

            if (codigo < 1):
                print(Fore.RED + "Código inválido, intente de nuevo")
            elif (codigo > productos_registrados):
                print(Fore.RED + f"Recuerde que los códigos se asignan automaticamente, el código máximo actual es {productos_registrados}, intente de nuevo")
            
        except ValueError:

            print(Fore.RED + "Usted no ingresó un número, intentelo de nuevo")


    print(Fore.GREEN + f"El código {codigo} se ha guardado exitosamente")
    return codigo








def validacion_opcion_venta()->int:
    opcion:int=0
    while opcion <1 or opcion >2:
        try:
            opcion=int(input(Fore.BLUE + "Ingrese :1. Si usted desea seguir agregando productos a la venta \n 2. Si usted desea dejar de agregar productos a la venta\n : "))
            if opcion <1 or opcion >2:
                print(Fore.RED + "La opcion ingresada no esta dentro del intervalo [1,2], ingresela de nuevo")
        except ValueError:
            print(Fore.RED + "Usted no ingreso una opcion valida, ingresela de nuevo")
    print(Fore.GREEN + f"La opcion {opcion} ha sido guardada exitosamente!")
    return opcion
